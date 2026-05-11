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

def risk_category(dataframe):
    #for arreas and days past due use their max and min values to segment the data
    min_arrears, max_arrears = dataframe['arrears'].min(), dataframe['arrears'].max()
    min_days_pd, max_days_pd = dataframe['days_past_due'].min(), dataframe['days_past_due'].max()

    #calculate ranges
    range_arr = max_arrears - min_arrears
    range_days_pd = max_days_pd - min_days_pd

    def classify(client):
        #first payment default is high risk
        if client['account_status_l1'] == 'First Payment Default':
            return 'High Risk'
        
        # 2. Normalize values to a 0.0 - 1.0 scale
        # (Current Value - Min) / Range
        #
        score_arrears = (client['arrears'] - min_arrears) / range_arr if range_arr > 0 else 0
        score_days_pd = (client['days_past_due'] - min_days_pd) / range_days_pd if range_days_pd > 0 else 0
        
        #get highest risk factor in either column
        final_score = max(score_arrears, score_days_pd)
        
        #classify based on score
        if final_score > 0.66:   #top 33%
            return 'High Risk'
        elif final_score > 0.33:
            return 'Medium Risk'
        else:                   #bottom 33% of the range
            return 'Low Risk'
    dataframe['risk_category'] = dataframe.apply(classify, axis=1)
    return dataframe
