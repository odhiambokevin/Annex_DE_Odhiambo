import logging
from logging.handlers import SMTPHandler
import sys
from pathlib import Path
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

def data_quality_check(dataframes, thresholds):
    for df_name, df in dataframes.items():
        if df_name not in thresholds:
            continue
            
        logger.info(f"Starting Quality Check for: {df_name}")
        
        #load the rules for the dataframe in the iteration
        df_rules = thresholds[df_name]
        
        for column, rule in df_rules.items():
            if column not in df.columns:
                logger.warning(f"Column {column} not found in {df_name}")
                continue
            
            #get the null percentage
            null_percentage = df[column].isnull().mean() * 100 #becaue .mean() returns a value between 0 and 1
            limit = rule['limit']
            
            if null_percentage > limit:
                should_stop = rule.get('stop_pipeline', False)

                status_msg = "CRITICAL FAILURE - STOPPING PIPELINE!" if should_stop else "WARNING"
                error_msg = (
                    f"[{status_msg}] Null Threshold Violated in '{df_name}'! "
                    f"Column '{column}' has {null_percentage:.2f}% nulls (Limit: {limit:.2f}%)"
                )

                if should_stop: #stop_pipeline evaluates to True
                    logger.critical(error_msg)
                    break #stop processing this dataframe entirely
                else:#process the dataframe but still alert the admin of exceeded threshold
                    logger.error(error_msg)

            else:
                logger.info(f"Column '{column}' passed ({null_percentage:.2f}%)")
if __name__ == '__main__':
     #get the data
    clean_dfs = get_clean_db_data()

    #threshold limit for specific defined columns
    check_rules = {
        'merged_credit_data': {
            'adjustment_amount': {'limit': 30.00, 'stop_pipeline': False}
        },
        'sales_and_customer_data_sales_details': {
            'loan_price': {'limit': 0.00, 'stop_pipeline': True}
        }
    }

    #run the quality check pipeline
    data_quality_check(clean_dfs, check_rules)