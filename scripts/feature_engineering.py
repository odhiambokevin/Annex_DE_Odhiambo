import pandas as pd
from datetime import datetime
from data_profiling import get_clean_db_data

clean_df = get_clean_db_data()

def calculate_age_band(dataframes):
    current_date = datetime.now()
    
    for name, df in dataframes.items():
            if 'date_of_birth' in df.columns:
                #converting dates to handle mixed timezones and remove timezone info
                dob = pd.to_datetime(df['date_of_birth'],format='mixed',errors='coerce',utc=True).dt.tz_localize(None)
                
                #calculating age, i ignore the timezone
                df['age'] = dob.apply(lambda x: current_date.year - x.year - 
                                      #checks if the month and date have passed or not 
                                      ((current_date.month, current_date.day) < (x.month, x.day)) 
                                      if pd.notnull(x) else None)
                
                #create the age bands
                age_bands = [18, 26, 36, 46, 56, float('inf')]
                labels = ['18–25', '26–35', '36–45', '46–55', '55+']
                
                #categorize
                df['age_band'] = pd.cut(df['age'], bins=age_bands, labels=labels, right=False).astype(str)
                
    return dataframes

