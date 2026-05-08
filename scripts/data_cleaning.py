from data_profiling import get_database_data,df_value_counts,df_nulls,check_inconsistency,identify_duplicates

#renaming long column names and lowercase all columns (my personal preference to lowercase)
def rename_df_cols(dataframes):
    renamed_df = {}

    #renaming of only long columns names from nps_data
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

# raw_database_df = get_database_data()
renamed_df = rename_df_cols(get_database_data())

# for name,df in renamed_df.items():
#     print("\n")
#     print(f"{"-"*50} DataFrame: {name} {"-"*50}")
#     cols = df.columns.tolist()
#     print(f"Columns ({len(cols)}): {cols}")
#     print("\n")

#delete entire row duplicates
def remove_exact_row_duplicate(dataframes):
    identify_duplicates(dataframes) #get duplicate reports
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

duplicates_removed = remove_exact_row_duplicate(renamed_df)
identify_duplicates(duplicates_removed)


# my_nps = renamed_df['nps_data']
# print(my_nps.columns)