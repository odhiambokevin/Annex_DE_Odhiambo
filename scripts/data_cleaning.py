import os
from datetime import datetime
from pathlib import Path
from decouple import config
from sqlalchemy import create_engine, inspect,text
import pandas as pd
from pandas import NaT
import numpy as np
from data_profiling import get_database_data,df_value_counts,df_nulls,check_inconsistency,identify_duplicates

RUN_PIPELINE_ONCE_A_DAY = config('RUN_PIPELINE_ONCE_A_DAY', default=False, cast=bool)
CLEAN_DATA_SCHEMA = config('CLEAN_DATA_SCHEMA')

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

raw_data = get_database_data()

#renaming long column names and lowercase all columns (my personal preference to lowercase)
def rename_df_cols(dataframes):
    renamed_df = {}

    #renaming of only long columns names from nps_data/this needs to be configured manually after profiling to identify column names
    nps_mapping = {
    'Using a scale from': 'recommend_score',
    'What is the main reason for your': 'recommend_score_reason',
    'What is one thing we could': 'improv_feedb',
    'Are you happy with the quality': 'happy_device_perfomance',
    'Are you happy with the service': 'happy_with_asst',
    'Have you ever experienced a delay': 'payment_update_delay',
    'Have you ever had difficulty getting': 'diff_get_asst',
    '(If Yes) –': 'diff_get_asst_remark',
    'Have you experienced any battery': 'batt_issues',
    'Have you used the MoPhones app (MoApp)': 'used_app_for_acc_mgt',
    'Which communication channel do you prefer': 'prefered_comm_chan',
    'Have you ever had your phone lock despite': 'locked_paid_on_time',
    'Any other Feedback?': 'other_feedb',
    }

    for name, df in dataframes.items():
        #copy so original dictionary data remains
        temporary_df = df.copy()
        
        if name == 'nps_data':
            #check length of column based on nps_mapping then lowercase
            new_columns = []
            for column in temporary_df.columns:
                #set column name to current name
                target_name = column
                
                #check for long column names as per our nps_mappings
                for long_col_name, new_col_name in nps_mapping.items():
                    if column.startswith(long_col_name):
                        target_name = new_col_name
                        break
                
                # new_columns.append(target_name.lower())
                new_columns.append("_".join(target_name.lower().split())) #gets rid of white spaces
            temporary_df.columns = new_columns
            
        else:
            #all other dataframes columns to lowercase
            temporary_df.columns = ["_".join(column.lower().split()) for column in temporary_df.columns]
        
        #storing the new dataframe in the new dictionary
        renamed_df[name] = temporary_df
        
    return renamed_df

clean_cols = rename_df_cols(raw_data)

#delete entire row duplicates
def remove_exact_row_duplicate(dataframes):
    duplicates_removed_df= {}

    print(f"\n{'-'*50} Removing exact row duplicates {'_'*50}")

    for name, df in dataframes.items():
        #identify number of duplicates before removing
        before_count = len(df)
        
        #drop duplicates but keep original dictionary since copy creates a new df
        duplicates_removed = df.drop_duplicates().copy()
        
        after_count = len(duplicates_removed)
        dropped_duplicates_count = before_count - after_count
        
        duplicates_removed_df[name] = duplicates_removed
        
        print(f"Table: {name} | Removed {dropped_duplicates_count} duplicate rows.")
    print(f"{'_'*50} Exact row duplicates removed successfully{'_'*50}\n")
    return duplicates_removed_df

clean_dups = remove_exact_row_duplicate(clean_cols)

def change_data_types(dataframes):
    uniform_datatypes_df = {}

    print("Changing data types...")

    for name, df in dataframes.items():
        temporary_df = df.copy() # we keep the original df unchanged
        
        for col in temporary_df.columns:
            type_counts = temporary_df[col].apply(type).value_counts() #number of count per type
            
           #if multiple types are found, enforce the modal type
            if len(type_counts) > 1:
                #this logic tries to go for second most freq type if most are in the null types
                null_types = {type(None), type(pd.NA), type(NaT)}
                real_types = [t for t in type_counts.index if t not in null_types]

                if not real_types: #this ignores a completely empty column and does not assign it as an empty string
                    print(f"Skipping {col}: No real data types found...")
                    continue

                most_frequent_type = real_types[0]

                print(f"Table [{name}] | Column [{col}]: changing types to {most_frequent_type.__name__}")

                #i handle float exclusively since pandas sees empty cell as float(NaN) not accounting for coordinates,%s
                if most_frequent_type is float:
                    if temporary_df[col].count() == 0:
                        if len(real_types) > 1: #most frequent is float but all are empty but we have other real types
                            most_frequent_type = real_types[1] #goes for second most frequent type
                        else:
                            #we skip the empty skip it
                            continue

                if most_frequent_type is type(NaT) or most_frequent_type is type(None):
                    print(f"Skipping column [{col}] for table [{name}] - it contains only null-like values.")
                    continue

                if 'timestamp' in str(most_frequent_type).lower() or 'datetime' in str(most_frequent_type).lower():
                    temporary_df[col] = pd.to_datetime(temporary_df[col], errors='coerce')

                elif most_frequent_type is float:
                    #this now keeps coordinates as well as percentages decimals which can be ignored by pandas
                    temporary_df[col] = pd.to_numeric(temporary_df[col], errors='coerce')

                elif most_frequent_type is int:
                    #use errors='raise' in production to enforce strict check for numbers so that 12oo can be raised
                    #int64 allows code with integers and Nan run without crashing
                    temporary_df[col] = pd.to_numeric(temporary_df[col], errors='coerce').astype('Int64')
                
                elif most_frequent_type is str:
                    #ensures it is null and not the sring "nan" which pandas does when converting objects to strings
                    temporary_df[col] = temporary_df[col].astype(str).replace('nan', pd.NA) 
                
                else:
                    # Fallback for other types
                    temporary_df[col] = temporary_df[col].astype(most_frequent_type)

        uniform_datatypes_df[name] = temporary_df
        print(f"Finished processing {name} file types")

    print("data type changes successful!")
    return uniform_datatypes_df

clean_data = change_data_types(clean_dups)

print(f"\n\n\n Clean Null Check\n")
check_nulls = df_nulls(clean_data)
def clean_data_pipeline(engine):
    #get raw data from database
    raw_data = get_database_data()

    print("\nData cleanig process started...")
    #data cleaning function called sequentially
    renamed_data = rename_df_cols(raw_data)
    deduplicated_data = remove_exact_row_duplicate(renamed_data)
    final_cleaned_data = change_data_types(deduplicated_data)
    
    #set output folder path
    output_dir = os.path.join("..", "outputs")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
    
    current_date = datetime.now().strftime("%Y-%m-%d") #to add as part of filename

    #i intend to save the final cleaned datasets to a new table in a different schema
    target_schema = CLEAN_DATA_SCHEMA

    with engine.connect() as conn:
        #create the schema if it does not exist
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {target_schema};"))
        #ensure the schema is registered
        conn.commit()
    
    print(f"\nSchema '{target_schema}' verified.")
    
    print(f"\nProcessing {len(final_cleaned_data)} tables...")
    for name, df in final_cleaned_data.items():
        #save first to database
        print(f"Uploading {name} to database -  schema: {target_schema}")
        df.to_sql(
            name=name, 
            con=engine, 
            schema=target_schema, 
            if_exists='replace', # Or 'append' based on your preference
            index=False
        )

        filename = f"{name}_{current_date}_cleaned_summary.csv" #add current date as part of file for easy id
        output_path = os.path.join(output_dir, filename)

        if RUN_PIPELINE_ONCE_A_DAY: #mode to choose write behavior
            #skip this file if it already exists
            if os.path.exists(output_path):
                print(f"Warning:'{filename}' already exists in output folder. Skipping file..\n")
                continue
            #export first 100 rows for sample
            print(f"\nSaving sample 100 rows of each table to {output_dir}...")
            df.head(100).to_csv(output_path, index=False)
            print(f"Exported: {output_path}\n")
        else:
            #mode='a' appends so new info does not overwrite file which is the default behaviour of .to_csv
            #first 100 only for demo. appended rows always go to the bottom and wont appear here due to 100 limit
            print(f"\nSaving sample 100 rows of {name} table to {output_dir}...")
            df.head(100).to_csv(output_path, mode='a',header=False,index=False) #header false prevents getting headers from new files as part of data
            print(f"Exported: {output_path}\n")

    print("\nData cleaning completed successfully!")
    return final_cleaned_data

# if __name__ == "__main__":
#     clean_data_pipeline(engine)