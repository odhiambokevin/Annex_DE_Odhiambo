import sys
import logging
from logging.handlers import SMTPHandler
from pathlib import Path
from datetime import datetime
import pandas as pd
from decouple import config,Csv
from data_profiling import get_clean_db_data

#to help is setting logging file path
BASE_DIR = Path(__file__).resolve().parent.parent

#logging config
logger = logging.getLogger("qualityCheckLogger")
logger.setLevel(logging.DEBUG)

ADMIN_EMAIL = config('ADMIN_EMAIL',cast=Csv()) #list of admin emails to send critical error messages to

#formatter
formatter = logging.Formatter(fmt='%(name)s: %(asctime)s %(levelname)s: - %(message)s')

#what appears on terminal
console_handler = logging.StreamHandler(stream=sys.stdout)
console_handler.setFormatter(formatter)

#what goes to a file - currenlty ignored by git
file_handler = logging.FileHandler(filename='logs.txt')
file_formatter = file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def setup_email_alert(logger, admin_email):
    #configure the email handler
    mail_handler = SMTPHandler(
        mailhost=(config("EMAIL_HOST"), 587), #(Host, Port) #
        fromaddr=config("EMAIL_HOST_USER"),
        toaddrs=admin_email,
        credentials=(config('EMAIL_HOST_USER'), config('EMAIL_HOST_PASSWORD')),
        secure=(),
        subject="Annex ABC Data: Quality Check Failed"
    )

    #email set for errors and above
    mail_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('''
    Loger: %(name)s
    Time: %(asctime)s
    Module: %(module)s
    Line: %(lineno)d
    Message: %(message)s
    ''')
    #set email alert logger
    mail_handler.setFormatter(formatter)

    logger.addHandler(mail_handler)

setup_email_alert(logger, ADMIN_EMAIL)

def check_nulls(df, df_name, rules):
    for column, rule in rules.items():
        if column not in df.columns:
            logger.warning(f"Column '{column}' not found in {df_name}")
            continue
            
        null_percentage = df[column].isnull().mean() * 100
        limit = rule['limit']
        
        if null_percentage > limit:
            should_stop = rule.get('stop_pipeline', False)
            status_msg = "CRITICAL FAILURE" if should_stop else "WARNING"
            error_msg = (
                f"[{status_msg}] Null Threshold Violated in '{df_name}'!\n"
                f"Column '{column}' has {null_percentage:.2f}% nulls (Limit: {limit:.2f}%)"
            )
            
            if should_stop:
                logger.critical(error_msg)
                return False #stop processing this dataframe entirely
            else:
                logger.error(error_msg)
                
    return True

def check_ranges(df, df_name, rules):
    for column, rule in rules.items():
        if column not in df.columns:
            logger.warning(f"Column '{column}' not found in {df_name}")
            continue

        if 'age_range' in rule:
            min_age, max_age = rule['age_range'] #get the min and max ranges for age

            #values outside set threshold
            out_of_range_values = (df[column] < min_age) | (df[column] > max_age)
            violation_count = out_of_range_values.sum()

            if violation_count > 0:
                #percentage of values outside range
                violation_percent = (violation_count / len(df)) * 100
                should_stop = rule.get('stop_pipeline', False) #deaults to False
                status_msg = "CRITICAL FAILURE" if should_stop else "WARNING"
                
                error_msg = (
                    f"[{status_msg}] Range Violation in '{df_name}'!\n"
                    f"Column '{column}' has {violation_count} records ({violation_percent:.2f}%) "
                    f"outside allowed range [{min_age}-{max_age}]."
                )
                if should_stop:
                    logger.critical(error_msg)
                    return False
                else:
                    logger.error(error_msg)
    return True

def data_quality_check(dataframes, check_rules):
    #ignore if the dataframe  is not in rule check
    for df_name, df in dataframes.items():
        if df_name not in check_rules:
            continue
            
        logger.info(f"\nStarting Quality Check for: {df_name}")
        rules = check_rules[df_name]

        #check if dataframe qualifies for null checks
        if 'null_checks' in rules:
            passed_nulls = check_nulls(df, df_name, rules['null_checks'])
            if not passed_nulls: #should_stop has evaluated to True
                logger.warning(f"Skipping remaining checks for '{df_name}' due to critical null failure.\n")
                continue  #this moves to process next dataframe for nulls

        #check if dataframe qualifies for range check
        if 'range_checks' in rules:
            check_ranges(df, df_name, rules['range_checks'])

if __name__ == '__main__':
     #get the data
    clean_dfs = get_clean_db_data()

    #quality check rules for tables/datframes and specific columns
    check_rules = {
        'merged_credit_data': {
            'null_checks': {
                'adjustment_amount': {'limit': 30.00, 'stop_pipeline': False}
            },
            'range_checks': {
                'customer_age': {'age_range': (18, 90)}
            }
        },
        'sales_and_customer_data_sales_details': {
            'null_checks': {
                'loan_price': {'limit': 0.00, 'stop_pipeline': True}
            }
        },
    }


    #run the quality check pipeline
    data_quality_check(clean_dfs, check_rules)