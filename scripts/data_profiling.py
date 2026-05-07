import os
from pathlib import Path
from decouple import config
import pandas as pd
from sqlalchemy import create_engine, inspect

# to create an example subfolder use os.makedirs(BASE_DIR / 'example2', exist_ok=True)
BASE_DIR = Path(__file__).resolve().parent.parent

#database connection string variables set from .env file
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')

#connect to and from database using sqlalchemy and psycopg2
conn_string = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(conn_string)

def ingest_data():
    #Sales and Customer data and NPS data files
    files_folder = os.path.join(BASE_DIR / 'data' / 'staging')
    
    if os.path.exists(files_folder):
        for file in os.listdir(files_folder):
            file_path = os.path.join(files_folder, file)
            if os.path.isfile(file_path) and file.endswith(('.xlsx', '.xls', '.csv')): #to ignore folder in files_folder
                table_name = file.replace('.xlsx', '').replace('csv', '').replace(' ', '_').replace("-", "_").lower()
                print(f"Uploading: {table_name}...")
                if file.endswith('.csv'): # read .csv files
                    df = pd.read_csv(file_path)
                else:
                    df = pd.read_excel(file_path) #other excel file types
                df.to_sql(table_name, engine, if_exists='replace', index=False)
                print(f"Uploaded: {table_name}")
            else:
                print(f"{file} is either a directory or not in allowed format")
                print(f"...skipping\n")

    #processing Credit Data folder by merging all the csv files in there
    credit_folder = os.path.join(BASE_DIR / 'data' / 'staging' / 'Credit Data') #base folder for credit data
    credit_frames = []

    if os.path.exists(credit_folder):
        for file in os.listdir(credit_folder):
            file_path = os.path.join(credit_folder, file)
            table_name = file.replace('.xlsx', '').replace('csv', '').replace(' ', '_').replace("-", "_").lower()
            
            #merge all csv files in the credit data folder
            if file.endswith('.csv'):
                print(f"Uploading: {table_name}...")
                temporary_df = pd.read_csv(file_path)
                credit_frames.append(temporary_df)
            
            #process the definitions excel separately
            elif file == 'Credit Data Definitions.xlsx':
                print(f"Uploading: {table_name}...")
                df_definitions = pd.read_excel(file_path)
                df_definitions.to_sql('credit_data_definitions', engine, if_exists='replace', index=False)
                print("Uploaded: credit_data_definitions")

        #combine and upload merged credit data file
        if credit_frames:
            merged_credit_df = pd.concat(credit_frames, ignore_index=True)
            merged_credit_df.to_sql('merged_credit_data', engine, if_exists='replace', index=False)
            print(f"Uploaded merged credit data: {len(credit_frames)} files merged")
    else:
        print("Credit Data folder does not exist")


def get_database_data():
    inspector = inspect(engine) # to query the database in case we are not sure of exact table names in db

    tables_ns = inspector.get_table_names(schema='public') #table name space we can limit schema access here as necessary for security
    #tables_ns = ["merged_credit_data", "sales",] we can filter specific tables like this to use less memory
    # tables_ns = ["merged_credit_data"]
    
    dataframes = {} #this will hold our converted tables as data frames

    print(f"{len(tables_ns)} tables found - tables: {tables_ns}")

    try:
        for table in tables_ns:
            print(f"Loading {table}...")
            #we load individual tables to our data frame dictionary
            dataframes[table] = pd.read_sql_table(table, engine, schema='public')
            
        return dataframes
    
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        engine.dispose() #we close all database connections

raw_database_df = get_database_data()

# -----------------------DATA PROFILING------------------------------------------------------------------

#statistical overview of our data frames
if raw_database_df:
    for name, df in raw_database_df.items():
        print(f"\n{'-'*25} Profiling Summary for: {name} {'-'*25}")
        print(df.describe())
        print(df.info())

#Missing values Analysis
def df_nulls(dataframes):
    for name, df in dataframes.items():
        print(f"\n{'-'*50}")
        print(f"Missing values report for {name} table")
        print(f"{'-'*50}")
        
        # Calculate number of nulls
        no_of_nulls = df.isnull().sum()
        
        # Calculate percentages of nulls
        null_percent = (df.isnull().sum() / len(df)) * 100
        
        # Merge into results into a summary table
        null_summary = pd.DataFrame({
            'Missing Values': no_of_nulls.sort_values(ascending=False),
            'Percentage (%)': null_percent.round(2).sort_values(ascending=False)
        })
 
        print(null_summary)    
        print(f"\nTotal Rows: {len(df)}")
        print(f"\n{'-'*25} ENDS {'-'*25}")

#Frequency Analysis
def df_value_counts(dataframes):
    for name, df in dataframes.items():
        print(f"\n{'-'*50}")
        print(f"Frequency analysis for {name} table")
        print(f"{'-'*50}\n") #
        
        for col_name, col_data in df.items():
            if col_data.nunique() > 20: #covers highly unique columns eg ids
                print(f"Top 10 of {col_data.nunique()} unique values")
                print(col_data.value_counts().head(10))
            else:
                print(col_data.value_counts(dropna=False))
        print(f"\n{'-'*25} ENDS {'-'*25}")

#Identifying duplicates
def identify_duplicates(dataframes):
    for name, df in dataframes.items():
        print(f"\n{'-'*50}")
        print(f"Duplicate analysis for {name} table")
        print(f"{'-'*50}")

        #Identify entire row contents that are duplicates
        total_rows = len(df)
        no_of_duplicate_row = df.duplicated().sum()
        
        print(f"Total Rows: {total_rows}")
        print(f"Entire Duplicate Rows: {no_of_duplicate_row}") #can help to identify ingestion discrepancy in pipeline
        
        if no_of_duplicate_row > 0:
            percentage = (no_of_duplicate_row / total_rows) * 100
            print(f"{percentage:.2f}% of the data consists of exact duplicates.") #:.2f ensure trailing zeros included
        
        #Identify column level duplicated
        column_summary = []
        for col in df.columns:
            no_of_unique = df[col].nunique()
            is_unique = no_of_unique == total_rows
            column_summary.append({
                'Column': col,
                'Unique Values': no_of_unique,
                'No Duplicates': total_rows - no_of_unique,
                'Has Duplicates': not is_unique
            })
        
        #Display summary table
        column_summary_df = pd.DataFrame(column_summary)
        print(column_summary_df.to_string(index=False))
        print(f"\n{'-'*25} ENDS {'-'*25}")

#Asses data inconsistency
def check_inconsistency(dataframes):
    for name, df in dataframes.items():
        print(f"\n{'-'*50}")
        print(f"Data inconsistency analysis for {name} table")
        print(f"{'-'*50}")

        for col in df.columns:
            print(f"\nColumn: {col}")
            
            #Assess mix of data types
            types_in_col = df[col].apply(type).unique() #checks for all different data types in a column
            if len(types_in_col) > 1:
                print(f"Mixed types: found {len(types_in_col)} types: {types_in_col}")

            #Check for white spaces
            if df[col].dtype == 'object':
                whitespace_count = df[col].apply(lambda x: isinstance(x, str) and (x != x.strip())).sum()
                if whitespace_count > 0:
                    print(f"White space: {whitespace_count} rows have whitespaces.")

            #checking for outliers in numbers
            if pd.api.types.is_numeric_dtype(df[col]):
                mean = df[col].mean()
                std = df[col].std()
                outliers = df[(df[col] - mean).abs() > 3 * std][col] #3 standard deviation away needs extra probing
                if not outliers.empty:
                    print(f"Outliers: {len(outliers)} potential outliers are 3 stadard dev. away")

            #empty values
            zeros = (df[col] == 0).sum()
            if zeros > 0:
                print(f"Zeros: {zeros} rows contain the value 0.")
        print(f"\n{'-'*25} ENDS {'-'*25}")


if __name__ == "__main__":
    # pass #uncomment the lines below to run the function calls
    ingest_data()
    # identify_duplicates(raw_database_df)
    # check_inconsistency(raw_database_df)
    # df_value_counts(raw_database_df)
    # df_nulls(raw_database_df)