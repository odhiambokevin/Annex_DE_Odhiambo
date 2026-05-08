# Data Quality Report

This is the Data Quality report for ABC Phones data retrieved from Excel files. Cleaning steps and decisions are also included in this report.

There is an index at the end of this document that shows the results of the profiling script.

## 1. Data Profile Summary
#### NPS Data
```bash
------------------------- Profiling Summary for: nps_data -------------------------
                        Submitted at  Using a scale from 0 (not likely) to 10 (very likely), how like
count                           4129                                        3985.000000              
mean   2025-08-29 20:39:40.324533504                                           6.779172              
min              2025-04-22 15:15:00                                           0.000000              
25%              2025-07-17 17:16:00                                           5.000000              
50%              2025-08-29 03:35:00                                           8.000000              
75%              2025-10-08 08:46:00                                          10.000000              
max              2025-12-27 02:06:00                                          10.000000              
std                              NaN                                           3.386783   
```
```bash
------------------------- Descriptive Summary for: nps_data -------------------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4129 entries, 0 to 4128
Data columns (total 17 columns):
 #   Column                                                           Non-Null Count  Dtype         
---  ------                                                           --------------  -----         
 0   Submission ID                                                    4129 non-null   object        
 1   Respondent ID                                                    4129 non-null   object        
 2   Submitted at                                                     4129 non-null   datetime64[ns]
 3   Loan Id                                                          4129 non-null   object        
 4   Using a scale from 0 (not likely) to 10 (very likely), how like  3985 non-null   float64       
 5   What is the main reason for your score?                          1183 non-null   object        
 6   What is one thing we could do to improve your experience with u  1134 non-null   object        
 7   Are you happy with the quality and performance of your device?   2627 non-null   object        
 8   Are you happy with the service and support provided by ABC Phon  2608 non-null   object        
 9   Have you ever experienced a delay in your payment reflecting in  2369 non-null   object        
 10  Have you ever had difficulty getting assistance from ABC Phones  2352 non-null   object        
 11  (If Yes) – Please describe the challenge you faced and how we    1960 non-null   object        
 12  Have you experienced any battery-related issues with your MoPho  2081 non-null   object        
 13  Have you used the MoPhones app (MoApp) to manage your account o  2060 non-null   object        
 14  Which communication channel do you prefer when contacting MoPho  2037 non-null   object        
 15  Have you ever had your phone lock despite making a payment on t  2030 non-null   object        
 16  Any other Feedback?                                              1753 non-null   object        
dtypes: datetime64[ns](1), float64(1), object(15)
memory usage: 548.5+ KB
None
```
```bash
--------------------------------------------------
Missing values report for nps_data table
--------------------------------------------------
                                                    Missing Values  Percentage (%)
What is one thing we could do to improve your e...            2995           72.54
What is the main reason for your score?                       2946           71.35
Any other Feedback?                                           2376           57.54
(If Yes) – Please describe the challenge you fa...            2169           52.53
Have you ever had your phone lock despite makin...            2099           50.84
Which communication channel do you prefer when ...            2092           50.67
Have you used the MoPhones app (MoApp) to manag...            2069           50.11
Have you experienced any battery-related issues...            2048           49.60
Have you ever had difficulty getting assistance...            1777           43.04
Have you ever experienced a delay in your payme...            1760           42.63
Are you happy with the service and support prov...            1521           36.84
Are you happy with the quality and performance ...            1502           36.38
Using a scale from 0 (not likely) to 10 (very l...             144            3.49
Submission ID                                                    0            0.00
Submitted at                                                     0            0.00
Loan Id                                                          0            0.00
Respondent ID                                                    0            0.00

Total Rows: 4129

------------------------- ENDS -------------------------
```
#### Sales and Customer Data
```bash
------------------------- Profiling Summary for: sales_and_customer_data -------------------------
                           SALE_DATE      RETURNED                    RETURN_DATE     CASH_PRICE     LOAN_PRICE
count                          20747  20747.000000                           1744   20745.000000   20745.000000
mean   2025-01-24 01:12:23.529185280      0.084012  2025-03-11 20:26:08.807339520   42392.583852   73090.441465
min              2023-02-08 00:00:00      0.000000            2023-03-16 00:00:00    7999.000000   15159.000000
25%              2024-07-25 00:00:00      0.000000            2024-10-16 00:00:00   29999.000000   51259.000000
50%              2025-03-06 00:00:00      0.000000            2025-04-07 00:00:00   37999.000000   67199.000000
75%              2025-08-21 00:00:00      0.000000            2025-08-25 00:00:00   47999.000000   82009.000000
max              2025-12-29 00:00:00      1.000000            2025-12-29 00:00:00  215499.000000  334219.000000
std                              NaN      0.277413                            NaN   
```
```bash
------------------------- Descriptive Summary for: sales_and_customer_data -------------------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1048575 entries, 0 to 1048574
Data columns (total 16 columns):
 #   Column                    Non-Null Count  Dtype         
---  ------                    --------------  -----         
 0   SALE_ID                   20747 non-null  object        
 1   SALE_DATE                 20747 non-null  datetime64[ns]
 2   RETURNED                  20747 non-null  float64       
 3   RETURN_DATE               1744 non-null   datetime64[ns]
 4   SALE_TYPE                 20745 non-null  object        
 5   SELLER                    20670 non-null  object        
 6   SELLER_TYPE               15776 non-null  object        
 7   RETURN_POLICY_COMPLIANCE  1744 non-null   object        
 8   CASH_PRICE                20745 non-null  float64       
 9   LOAN_PRICE                20745 non-null  float64       
 10  CLIENT_MODEL              20722 non-null  object        
 11  BUSINESS_MODEL            20747 non-null  object        
 12  LOAN_TERM                 20743 non-null  object        
 13  PRODUCT_NAME              20745 non-null  object        
 14  MODEL                     20745 non-null  object        
 15  Loan Id                   20696 non-null  object        
dtypes: datetime64[ns](2), float64(3), object(11)
memory usage: 128.0+ MB
None
```
```bash
--------------------------------------------------
Missing values report for sales_and_customer_data table
--------------------------------------------------
                          Missing Values  Percentage (%)
RETURN_DATE                      1046831           99.83
RETURN_POLICY_COMPLIANCE         1046831           99.83
SELLER_TYPE                      1032799           98.50
SELLER                           1027905           98.03
Loan Id                          1027879           98.03
CLIENT_MODEL                     1027853           98.02
LOAN_TERM                        1027832           98.02
SALE_TYPE                        1027830           98.02
PRODUCT_NAME                     1027830           98.02
LOAN_PRICE                       1027830           98.02
MODEL                            1027830           98.02
CASH_PRICE                       1027830           98.02
SALE_DATE                        1027828           98.02
SALE_ID                          1027828           98.02
RETURNED                         1027828           98.02
BUSINESS_MODEL                   1027828           98.02

Total Rows: 1048575

------------------------- ENDS -------------------------
```
#### Credit Data
```bash
------------------------- Profiling Summary for: merged_credit_data -------------------------
       CUSTOMER_AGE     TOTAL_PAID  TOTAL_DUE_TODAY        BALANCE  ...      DISCOUNT  OVERPAYMENT_AMOUNT    INITIAL_PAY  TOTAL_PAID_WITH_ADJUSTMENTS_15D
count  71456.000000   71456.000000     71428.000000   71448.000000  ...  71456.000000        71456.000000   71456.000000                     71456.000000
mean     295.006172   36438.008453     50379.246626   34085.654487  ...    376.308411           26.759273   12478.943574                     36675.222221
std      212.042127   27685.899248     30335.827589   28841.245947  ...   3074.511940          642.225410   10404.958680                     28058.289376
min        0.000000  -20499.000000      3099.000000  -81294.000000  ...      0.000000            0.000000   -2261.000000                    -20499.000000
25%      118.000000   14919.000000     28586.500000    8000.000000  ...      0.000000            0.000000    6739.000000                     15059.000000
50%      259.000000   29799.500000     45539.000000   32350.000000  ...      0.000000            0.000000    9219.000000                     30039.000000
75%      440.000000   49342.250000     67819.000000   51652.500000  ...      0.000000            0.000000   13049.000000                     49809.000000
max     1056.000000  222159.000000    334219.000000  205019.000000  ...  86870.000000        91254.000000  131999.000000                    222159.000000
```
```bash
------------------------- Descriptive Summary for: merged_credit_data -------------------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 71456 entries, 0 to 71455
Data columns (total 33 columns):
 #   Column                           Non-Null Count  Dtype  
---  ------                           --------------  -----  
 0   LOAN_ID                          71456 non-null  object 
 1   DATE                             71456 non-null  object 
 2   CUSTOMER_AGE                     71456 non-null  int64  
 3   TOTAL_PAID                       71456 non-null  int64  
 4   TOTAL_DUE_TODAY                  71428 non-null  float64
 5   BALANCE                          71448 non-null  float64
 6   DAYS_PAST_DUE                    71456 non-null  int64  
 7   CLOSING_BALANCE                  71448 non-null  float64
 8   ADVANCE                          71456 non-null  float64
 9   BALANCE_DUE_TO_DATE              71428 non-null  float64
 10  ARREARS                          71456 non-null  float64
 11  BALANCE_DUE_STATUS               71456 non-null  object 
 12  PAYMENT                          71456 non-null  int64  
 13  EXPECTED_PAYMENT                 71455 non-null  float64
 14  FIRST_PAYMENT                    71456 non-null  int64  
 15  FIRST_EXPECTED_PAYMENT           71456 non-null  int64  
 16  ACCOUNT_STATUS_L1                71456 non-null  object 
 17  ACCOUNT_STATUS_L2                71456 non-null  object 
 18  RETURN_DATE                      6886 non-null   object 
 19  SALE_DATE                        71456 non-null  object 
 20  CREDIT_CHECK_DONE                71456 non-null  object 
 21  PAYMENT_AMOUNT                   3163 non-null   float64
 22  ADJUSTMENT_AMOUNT                3163 non-null   float64
 23  PREPAYMENT_AMOUNT                71456 non-null  int64  
 24  DEPOSIT                          71448 non-null  float64
 25  WEEKLY_RATE                      71448 non-null  float64
 26  CREDIT_EXPIRY                    71456 non-null  object 
 27  NEXT_INVOICE_DATE                71456 non-null  object 
 28  DISCOUNT                         71456 non-null  float64
 29  OVERPAYMENT_AMOUNT               71456 non-null  float64
 30  MAX_PAYMENT_DATE                 70707 non-null  object 
 31  INITIAL_PAY                      71456 non-null  int64  
 32  TOTAL_PAID_WITH_ADJUSTMENTS_15D  71456 non-null  int64  
dtypes: float64(13), int64(9), object(11)
memory usage: 18.0+ MB
None
```
```bash

--------------------------------------------------
Missing values report for merged_credit_data table
--------------------------------------------------
                                 Missing Values  Percentage (%)
PAYMENT_AMOUNT                            68293           95.57
ADJUSTMENT_AMOUNT                         68293           95.57
RETURN_DATE                               64570           90.36
MAX_PAYMENT_DATE                            749            1.05
TOTAL_DUE_TODAY                              28            0.04
BALANCE_DUE_TO_DATE                          28            0.04
DEPOSIT                                       8            0.01
CLOSING_BALANCE                               8            0.01
BALANCE                                       8            0.01
WEEKLY_RATE                                   8            0.01
EXPECTED_PAYMENT                              1            0.00
LOAN_ID                                       0            0.00
DAYS_PAST_DUE                                 0            0.00
ADVANCE                                       0            0.00
CUSTOMER_AGE                                  0            0.00
TOTAL_PAID                                    0            0.00
DATE                                          0            0.00
ACCOUNT_STATUS_L1                             0            0.00
FIRST_EXPECTED_PAYMENT                        0            0.00
FIRST_PAYMENT                                 0            0.00
PAYMENT                                       0            0.00
ARREARS                                       0            0.00
BALANCE_DUE_STATUS                            0            0.00
CREDIT_CHECK_DONE                             0            0.00
SALE_DATE                                     0            0.00
PREPAYMENT_AMOUNT                             0            0.00
ACCOUNT_STATUS_L2                             0            0.00
NEXT_INVOICE_DATE                             0            0.00
CREDIT_EXPIRY                                 0            0.00
DISCOUNT                                      0            0.00
OVERPAYMENT_AMOUNT                            0            0.00
INITIAL_PAY                                   0            0.00
TOTAL_PAID_WITH_ADJUSTMENTS_15D               0            0.00
Total Rows: 71456
```
## 2. Data Cleaning
### 2.1 Column names
All column names in the dataset are set to lowercase. From experience, this makes writing sql queries and transformation logic in warehouses for modularity easier.

`NPS Data` had very lengthy column names as it was a survey. I shortened them to capture the framing as faithfully as possible. The main goal is keeping them short.

Renaming of column names with spaces eg `submitted at` to `submitted_at` is done for consistency with the data. `loan id` in `sales and customer` data becomes `loan_id`

The `"_".join(col.lower().split())` used in the cleaning script ensures multiple spaces are accounted for in cleaning so that `submmitted at` and `submitted` &nbsp; `at` will both default to `submitted_at`.

Sample output
```bash
-------------------------------------------------- DataFrame: sales_and_customer_data --------------------------------------------------
Columns (16): ['sale_id', 'sale_date', 'returned', 'return_date', 'sale_type', 'seller', 'seller_type', 'return_policy_compliance', 'cash_price', 'loan_price', 'client_model', 'business_model', 'loan_term', 'product_name', 'model', 'loan_id']

-------------------------------------------------- DataFrame: nps_data --------------------------------------------------
Columns (17): ['submission_id', 'respondent_id', 'submitted_at', 'loan_id', 'recommend_score', 'recommend_score_reason', 'improv_feedb', 'happy_device_perfomance', 'happy_with_asst', 'payment_update_delay', 'diff_get_asst', 'diff_get_asst_remark', 'batt_issues', 'used_app_for_acc_mgt', 'prefered_comm_chan', 'locked_paid_on_time', 'other_feedb']
```
### 2.2 Duplicate data
#### Sales and Customer Data
This dataset has **1,027,827** duplicate rows which have exact same data as identified by the `identify_duplicates` function. It may be an issue with ingestion logic. All the exact duplicate rows are dropped.

The new dataset has 20748 rows. It is now easier to query indepth the 1 duplicate row in `sale_id`.

sample output
```bash
-------------------------------------------------- Removing exact row duplicates ----------------------------------------
Table: sales_and_customer_data | Removed 1027827 duplicate rows.
Table: nps_data | Removed 0 duplicate rows.
Table: credit_data_definitions | Removed 0 duplicate rows.
Table: merged_credit_data | Removed 0 duplicate rows.
__________________________________________________ Exact row duplicates removed ----------------------------------------

--------------------------------------------------
Duplicate analysis for sales_and_customer_data table
--------------------------------------------------
Total Rows: 20748
Entire Duplicate Rows: 0
                  Column  Unique Values  No Duplicates  Has Duplicates
                 sale_id          20747              1            True
               sale_date            939          19809            True

```
### 2.3 Inconsistent data
I have used a function `change_data_types` that converts all the data types in a column in all loaded excel files to the most frequent data type for that column. For demonstration and time constraints, I have used `errors='coerce'` but in production I intend to use`errors='raise'` so that sensitive numerical columns for money are not harmonized. For instance `12oo` should raise an error as it could be `1,200`.

In the function `change_data_types`, floats are treaded uniquely. Pandas see an empty cell as a float. So these can be ignored since internally it sees them as NaN. I have factored this in the logic so that if there are 90 empty cells in a column with 100 rows and 10 integers, the logic goes for the second most frequent valid data type for conversion. It would check for these empty cells then go for int as the data type for the column. While previously the empty cells (Float) would force the column to be ignored and status quo (Mixed data types) would hold.

#### Credit Data
I merged the credit data sheets into one wide table. Some of the sheets *Credit Data - 30-06-2025.csv*, *Credit Data - 30-09-2025.csv* and *Credit Data - 30-12-2025.csv* had a blank column in the 29<sup>th</sup> column. This gave an unnamed column in the database with `Unnamed 28:` appearing as a column. This is identified in data cleaning and the ingestion logic is refactored to drop any columns that pandas names as `Unnamed`.