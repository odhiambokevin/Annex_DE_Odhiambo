import os
from pathlib import Path
from decouple import config
import pandas as pd
from io import StringIO
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
    root_files = ['NPS Data.xlsx', 'Sales and Customer Data.xlsx']
    for file in root_files:
        file_path = os.path.join(BASE_DIR / 'data' / 'staging' / file)
                      
        if os.path.exists(file_path):
            table_name = file.replace('.xlsx', '').replace('csv', '').replace(' ', '_').replace("-", "_").lower()
            print(f"Uploading: {table_name}...")           
            df = pd.read_excel(file_path)
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Uploaded: {table_name}")
        else:
            print("File does not exist")


    #processing Credit Data folder by merging all the csv files in there
    credit_folder = os.path.join(BASE_DIR / 'data' / 'staging' / 'Credit Data') #base folder for credit data
    credit_frames = []

    if os.path.exists(credit_folder):
        for file in os.listdir(credit_folder):
            file_path = os.path.join(credit_folder, file)
            
            #merge all csv files in the credit data folder
            if file.endswith('.csv'):
                temporary_df = pd.read_csv(file_path)
                credit_frames.append(temporary_df)
            
            #process the definitions excel separately
            elif file == 'Credit Data Definitions.xlsx':
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

if __name__ == "__main__":
    # ingest_data()
    print("Database upload complete.")

def get_database_data():
    inspector = inspect(engine) # to query the database in case we are not sure of exact table names in db

    # tables_ns = inspector.get_table_names(schema='public') #table name space we can limit schema access here as necessary for security
    #tables_ns = ["public.sales", "public.nps", "public.credit"] we can filter specific tables like this to use less memory
    tables_ns = ["nps_data"]
    
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

# -----------------------DATA CLEANING------------------------------------------------------------------

#statistical overview of our data frames
if raw_database_df:
    for name, df in raw_database_df.items():
        print(f"\n--- Profiling Summary for: {name} ---")
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
            'Missing Values': no_of_nulls,
            'Percentage (%)': null_percent.round(2)
        })
 
        print(null_summary)    
        print(f"\nTotal Rows: {len(df)}")
        print(f"{'-'*50}")

#Frequency Analysis
def df_value_counts(dataframes):
    for name, df in dataframes.items():
        print(f"\n{'-'*50}")
        print(f"Frequency Analysis for {name} table")
        print(f"{'-'*50}\n") #
        
        for col_name, col_data in df.items():
            if col_data.nunique() > 20: #covers highly unique columns eg ids
                print(f"Top 10 of {col_data.nunique()} unique values")
                print(col_data.value_counts().head(10))
            else:
                print(col_data.value_counts(dropna=False))
                print(f"{'-'*30}")
