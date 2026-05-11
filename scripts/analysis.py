import pandas as pd
from data_profiling import get_clean_db_data

clean_df = get_clean_db_data()

def delinquency_rate(dataframes):
    results = {}
    print("-" * 50)
    print("   DELINQUENCY RATES REPORT   ")
    print("-" * 50)
    found_any = False
    for name, df in dataframes.items():
        if 'merged_credit' in name:

            found_any = True

            #confirm the column exists in the dataframe
            if 'days_past_due' in df.columns:
                total_rows = len(df)
                
                #no account with days_past_due or column is blank, this prevents a division by zero error
                if total_rows == 0:
                    rate_str = "0.00%"
                else:
                    #customers with days_past_due > 0 values Nan are filled with zero
                    delinquent_count = (df['days_past_due'].fillna(0) > 0).sum()
                    
                    #percentage deliquency
                    rate = (delinquent_count / total_rows) * 100
                    rate_str = f"{rate:.2f}%"

                results[name] = rate_str
                # Print each result as we find it
                print(f"{name:<20} : {rate_str}")

            else:
                print(f"{name:<20} : Error - 'days_past_due' missing")
    if not found_any:
        print("No matching 'merged_credit' dataframes found.")
        
    print("-" * 50)
    return results

def loss_rate(dataframes):
    
    print("-" * 50)
    print("   LOSS RATE REPORT   ")
    print("-" * 50)

    loss_results = {}

    for name, df in dataframes.items():
        #look for datasets with 'merged_credit' in the name
        if 'merged_credit' in name:
            #confirm the columns needed for calculations exist
            if 'account_status_l1' in df.columns and 'closing_balance' in df.columns:
                
                #portfolio value is sum of all closing balances
                total_portfolio_value = df['closing_balance'].sum()
                
                # write off values where status is 'Write off')
                write_off_values = df['account_status_l1'] == 'Write Off'
                total_write_off_value = df.loc[write_off_values, 'closing_balance'].sum()
                
                #percentage
                if total_portfolio_value > 0:
                    loss_percentage = (total_write_off_value / total_portfolio_value) * 100
                else:
                    loss_percentage = 0.00
                
                formatted_rate = f"{loss_percentage:.2f}%"
                loss_results[name] = formatted_rate
                
                print(f"{name:<25} : {formatted_rate}")
            else:
                #check if any columns needed are missing
                missing = [col for col in ['account_status_l1', 'closing_balance'] if col not in df.columns]
                print(f"{name:<25} : Missing columns {missing}")

    print("-" * 45)
    return loss_results