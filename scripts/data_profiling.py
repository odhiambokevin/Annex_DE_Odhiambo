import os
from pathlib import Path
from decouple import config
import pandas as pd
from io import StringIO
from sqlalchemy import create_engine

# to create an example subfolder use os.makedirs(BASE_DIR / 'example2', exist_ok=True)
BASE_DIR = Path(__file__).resolve().parent.parent

#database connection string variables set from .env file
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')

#connect to database using sqlalchemy and psycopg2
conn_string = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(conn_string)

def ingest_data():
    #Sales and Customer data and NPS data files
    root_files = ['NPS Data.xlsx', 'Sales and Customer Data.xlsx']
    for file in root_files:
        file_path = os.path.join(BASE_DIR / 'data' / 'staging' / file)
                      
        if os.path.exists(file_path):
            table_name = file.replace('.xlsx', '').replace('csv', '').replace(' ', '_').replace("-", "_").lower()            
            df = pd.read_excel(file_path)
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f"Uploaded: {table_name}")
        else:
            print("File does not exist")


    #process Credit Data folder by merging all the csv
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
    ingest_data()
    print("Database upload complete.")
