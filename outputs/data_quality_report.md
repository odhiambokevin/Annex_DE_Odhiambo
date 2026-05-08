# Data Quality Report

This is the Data Quality report for ABC Phones data retrieved from Excel files. Cleaning steps and decisions are also included in this report.

There is an index at the end of this document that shows the results of the profiling script.

## 1. Data Profile Summary
#### NPS Data
- It has 4129 records of which non-nulls are 3985. Since this is a standard questionnaire response we wont' be concerned much about the nulls.
- We also get a general overview of the columns to expect
- The summary is shown below:
- It has used very little memory which is good for resource utilization.

```bash
--- Profiling Summary for: nps_data ---
count                           4129                                        3985.000000              
mean   2025-08-29 20:39:40.324533504                                           6.779172              
min              2025-04-22 15:15:00                                           0.000000              
25%              2025-07-17 17:16:00                                           5.000000              
50%              2025-08-29 03:35:00                                           8.000000              
75%              2025-10-08 08:46:00                                          10.000000              
max              2025-12-27 02:06:00                                          10.000000              
std                              NaN                                           3.386783              
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
#### Sales and Customer Data
- It has 1048575 records.
- We can see some nulls in columns like product type and we might consider whether builing relationships might help rectify this.
- We have used quite some memory since the dataframe is also large. We might consider strategies to rectify this.

```bash
--- Profiling Summary for: sales_and_customer_data ---
                           SALE_DATE      RETURNED                    RETURN_DATE     CASH_PRICE     LOAN_PRICE
count                          20747  20747.000000                           1744   20745.000000   20745.000000
mean   2025-01-24 01:12:23.529185280      0.084012  2025-03-11 20:26:08.807339520   42392.583852   73090.441465
min              2023-02-08 00:00:00      0.000000            2023-03-16 00:00:00    7999.000000   15159.000000
25%              2024-07-25 00:00:00      0.000000            2024-10-16 00:00:00   29999.000000   51259.000000
50%              2025-03-06 00:00:00      0.000000            2025-04-07 00:00:00   37999.000000   67199.000000
75%              2025-08-21 00:00:00      0.000000            2025-08-25 00:00:00   47999.000000   82009.000000
max              2025-12-29 00:00:00      1.000000            2025-12-29 00:00:00  215499.000000  334219.000000
std                              NaN      0.277413                            NaN   19082.531473   31220.699129
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

#### Credit Data
- This dataframe has 71456 entries

```bash
--- Profiling Summary for: merged_credit_data ---
       CUSTOMER_AGE     TOTAL_PAID  TOTAL_DUE_TODAY        BALANCE  ...  OVERPAYMENT_AMOUNT    INITIAL_PAY  TOTAL_PAID_WITH_ADJUSTMENTS_15D  Unnamed: 28
count  71456.000000   71456.000000     71428.000000   71448.000000  ...        71456.000000   71456.000000                     71456.000000          0.0
mean     295.006172   36438.008453     50379.246626   34085.654487  ...           26.759273   12478.943574                     36675.222221          NaN
std      212.042127   27685.899248     30335.827589   28841.245947  ...          642.225410   10404.958680                     28058.289376          NaN
min        0.000000  -20499.000000      3099.000000  -81294.000000  ...            0.000000   -2261.000000                    -20499.000000          NaN
25%      118.000000   14919.000000     28586.500000    8000.000000  ...            0.000000    6739.000000                     15059.000000          NaN
50%      259.000000   29799.500000     45539.000000   32350.000000  ...            0.000000    9219.000000                     30039.000000          NaN
75%      440.000000   49342.250000     67819.000000   51652.500000  ...            0.000000   13049.000000                     49809.000000          NaN
max     1056.000000  222159.000000    334219.000000  205019.000000  ...        91254.000000  131999.000000                    222159.000000          NaN

[8 rows x 23 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 71456 entries, 0 to 71455
Data columns (total 34 columns):
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
 33  Unnamed: 28                      0 non-null      float64
dtypes: float64(14), int64(9), object(11)
memory usage: 18.5+ MB
None
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
#### Sales and Customer Data
#### NPS Data
#### Credit Data
I merged the credit data sheets into one wide table. Some of the sheets *Credit Data - 30-06-2025.csv*, *Credit Data - 30-09-2025.csv* and *Credit Data - 30-12-2025.csv* had a blank column in the 29<sup>th</sup> column. This gave an unmaed column in the database with `Unnamed 28:` appearing as a column. This is identified in data cleaning and the ingestion logic is refactored to drop any columns that pandas names as `Unnamed`.
<br>
<br>
## Index

```bash
--------------------------------------------------
Duplicate analysis for nps_data table
--------------------------------------------------
Total Rows: 4129
Entire Duplicate Rows: 0
                                                         Column  Unique Values  No Duplicates  Has Duplicates
                                                  Submission ID           4129              0           False
                                                  Respondent ID           3756            373            True
                                                   Submitted at           3087           1042            True
                                                        Loan Id           3532            597            True
Using a scale from 0 (not likely) to 10 (very likely), how like             11           4118            True
                        What is the main reason for your score?           1060           3069            True
What is one thing we could do to improve your experience with u           1068           3061            True
 Are you happy with the quality and performance of your device?              2           4127            True
Are you happy with the service and support provided by ABC Phon              2           4127            True
Have you ever experienced a delay in your payment reflecting in              2           4127            True
Have you ever had difficulty getting assistance from ABC Phones              3           4126            True
  (If Yes) – Please describe the challenge you faced and how we           1339           2790            True
Have you experienced any battery-related issues with your MoPho              2           4127            True
Have you used the MoPhones app (MoApp) to manage your account o              3           4126            True
Which communication channel do you prefer when contacting MoPho              5           4124            True
Have you ever had your phone lock despite making a payment on t              2           4127            True
                                            Any other Feedback?           1163           2966            True

------------------------- ENDS -------------------------

```

```bash
--------------------------------------------------
Duplicate analysis for sales_and_customer_data table
--------------------------------------------------
Total Rows: 1048575
Entire Duplicate Rows: 1027827
98.02% of the data consists of exact duplicates.
                  Column  Unique Values  No Duplicates  Has Duplicates
                 SALE_ID          20747        1027828            True
               SALE_DATE            939        1047636            True
                RETURNED              2        1048573            True
             RETURN_DATE            530        1048045            True
               SALE_TYPE              3        1048572            True
                  SELLER            519        1048056            True
             SELLER_TYPE              5        1048570            True
RETURN_POLICY_COMPLIANCE              2        1048573            True
              CASH_PRICE            259        1048316            True
              LOAN_PRICE            930        1047645            True
            CLIENT_MODEL              3        1048572            True
          BUSINESS_MODEL              7        1048568            True
               LOAN_TERM              3        1048572            True
            PRODUCT_NAME            132        1048443            True
                   MODEL             82        1048493            True
                 Loan Id          20691        1027884            True

------------------------- ENDS -------------------------
```

```bash
--------------------------------------------------
Duplicate analysis for merged_credit_data table
--------------------------------------------------
Total Rows: 71456
Entire Duplicate Rows: 0
                         Column  Unique Values  No Duplicates  Has Duplicates
                        LOAN_ID          20742          50714            True
                           DATE              5          71451            True
                   CUSTOMER_AGE            964          70492            True
                     TOTAL_PAID          11106          60350            True
                TOTAL_DUE_TODAY           5569          65887            True
                        BALANCE          10383          61073            True
                  DAYS_PAST_DUE            898          70558            True
                CLOSING_BALANCE           8793          62663            True
                        ADVANCE           2121          69335            True
            BALANCE_DUE_TO_DATE          11025          60431            True
                        ARREARS           8905          62551            True
             BALANCE_DUE_STATUS              3          71453            True
                        PAYMENT            472          70984            True
               EXPECTED_PAYMENT            294          71162            True
                  FIRST_PAYMENT              2          71454            True
         FIRST_EXPECTED_PAYMENT              2          71454            True
              ACCOUNT_STATUS_L1             20          71436            True
              ACCOUNT_STATUS_L2              9          71447            True
                    RETURN_DATE            505          70951            True
                      SALE_DATE            939          70517            True
              CREDIT_CHECK_DONE              4          71452            True
                 PAYMENT_AMOUNT            461          70995            True
              ADJUSTMENT_AMOUNT             17          71439            True
              PREPAYMENT_AMOUNT             26          71430            True
                        DEPOSIT            602          70854            True
                    WEEKLY_RATE            307          71149            True
                  CREDIT_EXPIRY           1051          70405            True
              NEXT_INVOICE_DATE             35          71421            True
                       DISCOUNT            584          70872            True
             OVERPAYMENT_AMOUNT            231          71225            True
               MAX_PAYMENT_DATE            909          70547            True
                    INITIAL_PAY            947          70509            True
TOTAL_PAID_WITH_ADJUSTMENTS_15D          10921          60535            True
                    Unnamed: 28              0          71456            True

------------------------- ENDS -------------------------

```

```bash
--------------------------------------------------
Data inconsistency analysis for nps_data table
--------------------------------------------------

Column: Submission ID

Column: Respondent ID

Column: Submitted at

Column: Loan Id

Column: Using a scale from 0 (not likely) to 10 (very likely), how like
Zeros: 334 rows contain the value 0.

Column: What is the main reason for your score?
Mixed types: found 2 types: \\[<class 'NoneType'> <class 'str'>]

Column: What is one thing we could do to improve your experience with u
Mixed types: found 2 types: \\[<class 'NoneType'> <class 'str'>]

Column: Are you happy with the quality and performance of your device?
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: Are you happy with the service and support provided by ABC Phon
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: Have you ever experienced a delay in your payment reflecting in
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: Have you ever had difficulty getting assistance from ABC Phones
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: (If Yes) – Please describe the challenge you faced and how we
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: Have you experienced any battery-related issues with your MoPho
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: Have you used the MoPhones app (MoApp) to manage your account o
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: Which communication channel do you prefer when contacting MoPho
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: Have you ever had your phone lock despite making a payment on t
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: Any other Feedback?
Mixed types: found 2 types: \\[<class 'NoneType'> <class 'str'>]

------------------------- ENDS -------------------------
```

```bash
--------------------------------------------------
Data inconsistency analysis for sales_and_customer_data table
--------------------------------------------------

Column: SALE_ID
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: SALE_DATE
Mixed types: found 2 types: \\[<class 'pandas._libs.tslibs.timestamps.Timestamp'>
 <class 'pandas._libs.tslibs.nattype.NaTType'>]

Column: RETURNED
Outliers: 1743 potential outliers are 3 stadard dev. away
Zeros: 19004 rows contain the value 0.

Column: RETURN_DATE
Mixed types: found 2 types: \\[<class 'pandas._libs.tslibs.nattype.NaTType'>
 <class 'pandas._libs.tslibs.timestamps.Timestamp'>]

Column: SALE_TYPE
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: SELLER
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]
White space: 1080 rows have whitespaces.

Column: SELLER_TYPE
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: RETURN_POLICY_COMPLIANCE
Mixed types: found 2 types: \\[<class 'NoneType'> <class 'str'>]

Column: CASH_PRICE
Outliers: 431 potential outliers are 3 stadard dev. away

Column: LOAN_PRICE
Outliers: 448 potential outliers are 3 stadard dev. away

Column: CLIENT_MODEL
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: BUSINESS_MODEL
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: LOAN_TERM
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: PRODUCT_NAME
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: MODEL
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: Loan Id
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

------------------------- ENDS -------------------------


```

```bash
--------------------------------------------------
Data inconsistency analysis for merged_credit_data table
--------------------------------------------------

Column: LOAN_ID

Column: DATE

Column: CUSTOMER_AGE
Outliers: 169 potential outliers are 3 stadard dev. away
Zeros: 109 rows contain the value 0.

Column: TOTAL_PAID
Outliers: 1069 potential outliers are 3 stadard dev. away
Zeros: 778 rows contain the value 0.

Column: TOTAL_DUE_TODAY
Outliers: 1225 potential outliers are 3 stadard dev. away

Column: BALANCE
Outliers: 1015 potential outliers are 3 stadard dev. away
Zeros: 15487 rows contain the value 0.

Column: DAYS_PAST_DUE
Outliers: 1276 potential outliers are 3 stadard dev. away
Zeros: 39976 rows contain the value 0.

Column: CLOSING_BALANCE
Outliers: 985 potential outliers are 3 stadard dev. away
Zeros: 24559 rows contain the value 0.

Column: ADVANCE
Outliers: 919 potential outliers are 3 stadard dev. away
Zeros: 59364 rows contain the value 0.

Column: BALANCE_DUE_TO_DATE
Outliers: 1245 potential outliers are 3 stadard dev. away
Zeros: 17726 rows contain the value 0.

Column: ARREARS
Outliers: 1275 potential outliers are 3 stadard dev. away
Zeros: 29846 rows contain the value 0.

Column: BALANCE_DUE_STATUS

Column: PAYMENT
Outliers: 412 potential outliers are 3 stadard dev. away
Zeros: 68297 rows contain the value 0.

Column: EXPECTED_PAYMENT
Outliers: 400 potential outliers are 3 stadard dev. away
Zeros: 62550 rows contain the value 0.

Column: FIRST_PAYMENT
Outliers: 108 potential outliers are 3 stadard dev. away
Zeros: 71348 rows contain the value 0.

Column: FIRST_EXPECTED_PAYMENT
Outliers: 109 potential outliers are 3 stadard dev. away
Zeros: 71347 rows contain the value 0.

Column: ACCOUNT_STATUS_L1

Column: ACCOUNT_STATUS_L2

Column: RETURN_DATE
Mixed types: found 2 types: \\[<class 'NoneType'> <class 'str'>]

Column: SALE_DATE

Column: CREDIT_CHECK_DONE

Column: PAYMENT_AMOUNT
Outliers: 51 potential outliers are 3 stadard dev. away
Zeros: 19 rows contain the value 0.

Column: ADJUSTMENT_AMOUNT
Outliers: 17 potential outliers are 3 stadard dev. away
Zeros: 3142 rows contain the value 0.

Column: PREPAYMENT_AMOUNT
Outliers: 88 potential outliers are 3 stadard dev. away
Zeros: 71367 rows contain the value 0.

Column: DEPOSIT
Outliers: 2237 potential outliers are 3 stadard dev. away

Column: WEEKLY_RATE
Outliers: 792 potential outliers are 3 stadard dev. away

Column: CREDIT_EXPIRY

Column: NEXT_INVOICE_DATE

Column: DISCOUNT
Outliers: 1064 potential outliers are 3 stadard dev. away
Zeros: 65289 rows contain the value 0.

Column: OVERPAYMENT_AMOUNT
Outliers: 183 potential outliers are 3 stadard dev. away
Zeros: 69841 rows contain the value 0.

Column: MAX_PAYMENT_DATE
Mixed types: found 2 types: \\[<class 'str'> <class 'NoneType'>]

Column: INITIAL_PAY
Outliers: 1881 potential outliers are 3 stadard dev. away
Zeros: 8 rows contain the value 0.

Column: TOTAL_PAID_WITH_ADJUSTMENTS_15D
Outliers: 1069 potential outliers are 3 stadard dev. away
Zeros: 1692 rows contain the value 0.

Column: Unnamed: 28
------------------------- ENDS -------------------------
```

```bash
--------------------------------------------------
Frequency analysis for nps_data table
--------------------------------------------------
Top 10 of 4129 unique values
Submission ID
BzK4Q11    1
b59V45Z    1
GxKvYKO    1
A7KP49z    1
81zo6pr    1
xXjxR5J    1
GxKvQ6L    1
rjBykB2    1
5B4KeaM    1
5B4Kp16    1
Name: count, dtype: int64
Top 10 of 3756 unique values
Respondent ID
dByPay    4
0NoGJ6    4
loqJ86    4
q1Kv49    3
xOAA2k    3
EpXlDo    3
kMPqDj    3
oqRGlx    3
Mk1jMk    3
XjbxPP    3
Name: count, dtype: int64
Top 10 of 3087 unique values
Submitted at
2025-07-07 13:38:00    9
2025-07-07 13:40:00    8
2025-10-07 15:20:00    8
2025-04-22 16:25:00    7
2025-07-07 13:48:00    7
2025-08-19 15:12:00    7
2025-07-22 14:10:00    7
2025-10-07 15:30:00    7
2025-10-07 15:31:00    7
2025-11-24 11:24:00    7
Name: count, dtype: int64
Top 10 of 3532 unique values
Loan Id
recUuLe9KNHZD6Mql    5
receahL1GpamBixQH    4
recoTEhguiGXaU0o4    4
recpSgLxWQIXC6qfw    4
recCGoGXWotHLKAQS    4
reczmdCEsi8fe1xHf    4
rec7CFQLCsR52eQAs    4
recObMVtL2N13CosM    4
rec50bP9wtnmjockb    3
rect5BpHLRHHJ1biS    3
Name: count, dtype: int64
Using a scale from 0 (not likely) to 10 (very likely), how like
10.0    1275
8.0      517
9.0      430
0.0      334
5.0      307
7.0      294
1.0      197
6.0      192
3.0      161
NaN      144
4.0      139
2.0      139
Name: count, dtype: int64
Top 10 of 1060 unique values
What is the main reason for your score?
Good service             23
10                       14
Good                     13
Reliable                  8
Good customer service     7
Customer service          6
0                         6
Good services             5
Reliability               5
1                         5
Name: count, dtype: int64
Top 10 of 1068 unique values
What is one thing we could do to improve your experience with u
Nothing             13
Customer service     9
Communication        5
Good                 4
So far so good       4
Battery              4
I don\'t know         3
nothing              3
10                   3
0                    3
Name: count, dtype: int64
Are you happy with the quality and performance of your device?
Yes     1999
None    1502
No       628
Name: count, dtype: int64
Are you happy with the service and support provided by ABC Phon
Yes     2037
None    1521
No       571
Name: count, dtype: int64
Have you ever experienced a delay in your payment reflecting in
None    1760
No      1647
Yes      722
Name: count, dtype: int64
Have you ever had difficulty getting assistance from ABC Phones
None                                         1777
No                                           1460
Yes                                           621
No, I have never looked for customer care     271
Name: count, dtype: int64
Top 10 of 1339 unique values
(If Yes) – Please describe the challenge you faced and how we
No                313
No challenge       77
.                  26
Na                 20
Non                16
Nothing            14
0                  11
Not applicable     10
Nil                10
N/a                 9
Name: count, dtype: int64
Have you experienced any battery-related issues with your MoPho
None    2048
No      1293
Yes      788
Name: count, dtype: int64
Have you used the MoPhones app (MoApp) to manage your account o
None                                          2069
Yes, and I am satisfied with the MoApp        1419
No, I have never used it                       407
Yes, but I am not satisfied with the MoApp     234
Name: count, dtype: int64
Which communication channel do you prefer when contacting MoPho
None                                                 2092
Phone Call – +254 728 444 442 or +254 709 924 404    1046
MoPhones App                                          468
Free SMS – 25044                                      232
Reach Out via a Sales Agent                           232
Self-Service USSD – *789*25044#                        59
Name: count, dtype: int64
Have you ever had your phone lock despite making a payment on t
None    2099
No      1467
Yes      563
Name: count, dtype: int64
Top 10 of 1163 unique values
Any other Feedback?
No            354
.              18
no             16
Good           13
Nothing        13
Non            12
Na             12
N/a            11
Not really     10
Nope            9
Name: count, dtype: int64

------------------------- ENDS -------------------------
```

```bash
--------------------------------------------------
Frequency analysis for sales_and_customer_data table
--------------------------------------------------

Top 10 of 20747 unique values
SALE_ID
recg9SxxjvTdgP6NC    1
rec0P2Z778n8igV9u    1
recbZfItLLouuJj9h    1
recBtxgmMbuLKdANY    1
recspqipYdXTH1lNV    1
recndFA38hbzYWTzP    1
rec5bPiP9ZUdh6kZc    1
recBpBCJ5IVCjq3qL    1
recDUlJnFweXA6s5x    1
recjEN7Hb2IrvEyPs    1
Name: count, dtype: int64
Top 10 of 939 unique values
SALE_DATE
2025-12-02    80
2025-12-23    77
2025-12-05    75
2025-12-24    74
2025-12-04    73
2025-12-08    73
2025-12-09    71
2025-12-01    70
2025-12-19    68
2025-11-15    68
Name: count, dtype: int64
RETURNED
NaN    1027828
0.0      19004
1.0       1743
Name: count, dtype: int64
Top 10 of 530 unique values
RETURN_DATE
2025-05-27    30
2025-04-16    23
2025-12-24    19
2025-01-15    17
2025-04-11    17
2025-04-04    15
2024-07-24    14
2025-12-19    12
2025-04-15    12
2025-01-22    12
Name: count, dtype: int64
SALE_TYPE
None            1027830
Financed          19570
Non Financed        992
Y Lost              183
Name: count, dtype: int64
Top 10 of 519 unique values
SELLER
Christine Muloko            1295
MerryAnn Achieng            1121
Cynthia Mutai                764
Esther Nduta                 719
Naomi Anyango Odhiambo       666
Teresiah Njoroge             612
Joy Vugutsa                  520
Georginah Gathoni Githui     519
Ann Njoki                    509
Stive Opiyo                  452
Name: count, dtype: int64
SELLER_TYPE
None                         1032799
Sales Executive                10517
Telesales Executive             3642
SFM (Sales Force Manager)       1554
Commission Merchant               62
Rider                              1
Name: count, dtype: int64
RETURN_POLICY_COMPLIANCE
None             1046831
out of policy       1260
in policy            484
Name: count, dtype: int64
Top 10 of 259 unique values
CASH_PRICE
28999.0    857
34999.0    825
47499.0    716
44999.0    711
37999.0    600
30999.0    431
42499.0    419
27499.0    405
29999.0    397
35999.0    384
Name: count, dtype: int64
Top 10 of 930 unique values
LOAN_PRICE
45559.0    369
67819.0    352
81069.0    345
68579.0    304
55349.0    303
80259.0    302
44479.0    286
62779.0    273
38259.0    259
66669.0    253
Name: count, dtype: int64
CLIENT_MODEL
None    1027853
1C        16099
3C         4462
2C          161
Name: count, dtype: int64
BUSINESS_MODEL
None             1027828
1P1C               12721
1P3C                3479
Not Available       2111
3P1C                1662
3P3C                 615
1P2C                 132
3P2C                  27
Name: count, dtype: int64
LOAN_TERM
None       1027832
12M          19418
STDHIGH        761
3M             564
Name: count, dtype: int64
Top 10 of 132 unique values
PRODUCT_NAME
Samsung-Note-10-Plus-256GB          1953
Samsung-Note-20-128GB               1643
Samsung-Note-20-Ultra-128GB         1290
Samsung-Galaxy-S10-128GB            1179
Samsung-Galaxy-S20-Plus-5G-128GB    1138
Samsung-Galaxy-S20-Ultra-128GB      1069
Samsung-Galaxy-S21-Plus-5G-128GB     843
Samsung-Galaxy-A16-128GB             819
Samsung-Galaxy-S9-64GB               816
Samsung-Galaxy-S21-Ultra-128GB       735
Name: count, dtype: int64
Top 10 of 82 unique values
MODEL
Note-10-Plus          1985
Note-20-Ultra         1696
Note-20               1663
Galaxy-S10            1206
Galaxy-S20-Plus-5G    1153
Galaxy-S20-Ultra      1079
iPhone-11              884
Galaxy-S21-Ultra       879
Galaxy-S21-Plus-5G     867
Galaxy-A16             819
Name: count, dtype: int64
Top 10 of 20691 unique values
Loan Id
rec1s8Oc6qhMCGKZ2    2
reckeATieWqnKWWsr    2
recv1o61rctP3nHaR    2
recjYyRXvCYuPvpRK    2
recJA81Oa7JlNaMXI    2
recFD8CU3Fm74IGki    1
recwqWm9ApPWwLGoa    1
recwanM5b0yvixIeD    1
recx3co3tDKsIo1qM    1
recGX7TPUY8sgpEIy    1
Name: count, dtype: int64

------------------------- ENDS -------------------------
```

```bash
--------------------------------------------------
Frequency analysis for merged_credit_data table
--------------------------------------------------

Top 10 of 20742 unique values
LOAN_ID
reczZiie22UfW6jzq    5
recoCxWzNTQF7jgS4    5
recq1FuuNTWKCjUnt    5
recHv9vm8MRIoucaK    5
rec073uULkAuo8WHd    5
recO51dbu9mZjQmr7    5
recMddek1KX4wKbwk    5
rec1bGKeiCnKNykYR    5
recVaDK3Nos2ayWj8    5
recd00s0dNRqhJ1ay    5
Name: count, dtype: int64
DATE
12/30/2025    20742
9/30/2025     16864
6/30/2025     13891
3/31/2025     11024
1/1/2025       8935
Name: count, dtype: int64
Top 10 of 964 unique values
CUSTOMER_AGE
25    250
28    238
26    233
21    222
27    212
24    206
12    204
33    201
39    200
60    197
Name: count, dtype: int64
Top 10 of 11106 unique values
TOTAL_PAID
0        778
44379    275
47499    236
67719    236
44479    229
80159    226
57299    217
45459    214
43479    197
18839    168
Name: count, dtype: int64
Top 10 of 5569 unique values
TOTAL_DUE_TODAY
44479.0    1429
45559.0    1201
57399.0     917
67819.0     801
39339.0     727
80259.0     707
43479.0     571
40899.0     551
45039.0     491
63159.0     439
Name: count, dtype: int64
Top 10 of 10383 unique values
BALANCE
0.0         15487
37740.0       200
70380.0       149
60180.0       134
55080.0       123
123930.0      120
39270.0       118
59670.0        99
129540.0       92
43860.0        89
Name: count, dtype: int64
Top 10 of 898 unique values
DAYS_PAST_DUE
0     39976
1       609
4       309
3       296
2       265
5       219
6       184
7       181
14      131
21      130
Name: count, dtype: int64
Top 10 of 8793 unique values
CLOSING_BALANCE
0.0         24559
37740.0       200
70380.0       148
60180.0       134
55080.0       121
123930.0      120
39270.0       118
59670.0        98
129540.0       92
43860.0        85
Name: count, dtype: int64
Top 10 of 2121 unique values
ADVANCE
0.0      59364
1.0        808
10.0       325
20.0       267
100.0      197
30.0       188
40.0       172
60.0       148
200.0      133
50.0       133
Name: count, dtype: int64
Top 10 of 11025 unique values
BALANCE_DUE_TO_DATE
 0.0        17726
-100.0       4717
 1.0          808
 10.0         325
 20.0         267
 100.0        197
 30.0         188
 40.0         172
-37740.0      165
 60.0         148
Name: count, dtype: int64
Top 10 of 8905 unique values
ARREARS
0.0        29846
100.0       4717
37740.0      165
600.0        129
1080.0       121
1180.0       101
950.0         97
80.0          90
500.0         89
90.0          88
Name: count, dtype: int64
BALANCE_DUE_STATUS
Arrears       41610
up to date    17754
advance       12092
Name: count, dtype: int64
Top 10 of 472 unique values
PAYMENT
0       68297
1000       93
1300       73
200        71
1380       66
850        63
1180       63
500        59
950        58
1160       51
Name: count, dtype: int64
Top 10 of 294 unique values
EXPECTED_PAYMENT
0.0       62550
1180.0      294
1380.0      278
1080.0      257
740.0       243
1160.0      238
950.0       223
850.0       194
780.0       184
1300.0      171
Name: count, dtype: int64
FIRST_PAYMENT
0    71348
1      108
Name: count, dtype: int64
FIRST_EXPECTED_PAYMENT
0    71347
1      109
Name: count, dtype: int64
ACCOUNT_STATUS_L1
Existing Active                                  20211
Paid Off Loan                                    12137
Write Off                                        11816
New Active                                        4180
First Payment Default                             4160
Paid Off Cash                                     3276
First Month Default without inventory over 30     3208
Cancelled Returned past 3 mths                    3141
Blocked 31-60                                     1638
Inactive 01-07                                    1612
First 2 days Return                               1452
Blocked 61-90                                     1268
Inactive 15-30                                     992
First Month Default with inventory                 636
Cancelled Returned in 3 mths                       537
Inactive 08-14                                     534
Lost Write Off                                     413
First Month Default without inventory 01-07        194
First Month Default without inventory 08-14         43
Demo                                                 8
Name: count, dtype: int64
ACCOUNT_STATUS_L2
Active      24391
Paid Off    15413
PAR 30      15135
Return       5766
FPD          4160
FMD          3208
Inactive     1806
PAR 7        1569
Unknown         8
Name: count, dtype: int64
Top 10 of 505 unique values
RETURN_DATE
00:00.0      1744
5/27/2025     113
4/16/2025      88
1/15/2025      67
4/4/2025       60
4/11/2025      60
7/24/2024      56
9/4/2024       48
1/22/2025      47
2/10/2025      45
Name: count, dtype: int64
Top 10 of 939 unique values
SALE_DATE
7/3/2024      300
6/28/2024     285
7/5/2024      275
12/24/2024    250
7/6/2024      245
7/1/2024      240
12/20/2024    235
7/19/2024     235
7/9/2024      225
6/29/2024     215
Name: count, dtype: int64
CREDIT_CHECK_DONE
Y LOAN    67329
Y CASH     3443
Y LOST      676
Z DEMO        8
Name: count, dtype: int64
Top 10 of 461 unique values
PAYMENT_AMOUNT
1000.0    93
1300.0    73
200.0     71
1380.0    66
850.0     63
1180.0    63
500.0     59
950.0     58
1160.0    51
1400.0    49
Name: count, dtype: int64
ADJUSTMENT_AMOUNT
NaN        68293
0.0         3142
10130.0        2
6010.0         2
6560.0         2
2055.0         2
4300.0         2
6940.0         1
2120.0         1
10040.0        1
3950.0         1
22020.0        1
1590.0         1
5480.0         1
13750.0        1
2570.0         1
3080.0         1
19385.0        1
Name: count, dtype: int64
Top 10 of 26 unique values
PREPAYMENT_AMOUNT
0        71367
6269         5
11649        5
26209        5
48499        5
33499        5
26999        5
5200         5
9879         5
29499        5
Name: count, dtype: int64
Top 10 of 602 unique values
DEPOSIT
8499.0     4195
4999.0     3885
5499.0     2991
7499.0     2964
7999.0     2845
4499.0     2015
5999.0     1900
10999.0    1642
9999.0     1465
5399.0     1106
Name: count, dtype: int64
Top 10 of 307 unique values
WEEKLY_RATE
740.0     2390
1180.0    2233
950.0     2093
1380.0    2068
780.0     1890
1160.0    1859
1080.0    1713
770.0     1675
850.0     1472
670.0     1459
Name: count, dtype: int64
Top 10 of 1051 unique values
CREDIT_EXPIRY
1/2/2026      868
1/1/2026      807
12/31/2025    786
10/3/2025     784
1/3/2026      773
7/4/2025      711
10/4/2025     685
12/30/2025    680
1/5/2026      669
10/6/2025     664
Name: count, dtype: int64
Top 10 of 35 unique values
NEXT_INVOICE_DATE
1/2/2026      3522
1/5/2026      3344
1/3/2026      3305
12/31/2025    3295
1/6/2026      3203
1/1/2026      3115
10/3/2025     2936
10/1/2025     2691
10/4/2025     2678
10/6/2025     2659
Name: count, dtype: int64
Top 10 of 584 unique values
DISCOUNT
0.0      65289
100.0     3954
99.0        82
600.0       70
90.0        64
80.0        59
500.0       48
60.0        42
95.0        17
50.0        16
Name: count, dtype: int64
Top 10 of 231 unique values
OVERPAYMENT_AMOUNT
0.0      69841
10.0        87
1.0         74
100.0       59
50.0        49
20.0        48
740.0       47
0.4         41
40.0        35
680.0       33
Name: count, dtype: int64
Top 10 of 909 unique values
MAX_PAYMENT_DATE
12/29/2025    2199
12/27/2025    2105
12/24/2025    2076
12/26/2025    2034
12/25/2025    1944
12/28/2025    1670
12/23/2025    1665
12/22/2025     782
8/30/2024      595
12/21/2025     414
Name: count, dtype: int64
Top 10 of 947 unique values
INITIAL_PAY
5779     1745
8659     1615
6739     1390
9879     1370
8399     1063
5169      930
8949      920
10399     892
6379      835
6899      815
Name: count, dtype: int64
Top 10 of 10921 unique values
TOTAL_PAID_WITH_ADJUSTMENTS_15D
0        1692
44379     275
47499     238
44479     228
80159     224
67719     219
57299     217
45459     214
43479     198
39239     159
Name: count, dtype: int64
Unnamed: 28
NaN    71456
Name: count, dtype: int64

------------------------- ENDS -------------------------
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
Using a scale from 0 (not likely) to 10 (very l)...             144            3.49
Submission ID                                                    0            0.00
Submitted at                                                     0            0.00
Loan Id                                                          0            0.00
Respondent ID                                                    0            0.00

Total Rows: 4129
------------------------- ENDS -------------------------


```

```bash
-------------------------------------------------
Missing values report for sales_and_customer_data table
--------------------------------------------------
                          Missing Values  Percentage (%)
BUSINESS_MODEL                   1027828           98.02
CASH_PRICE                       1027830           98.02
CLIENT_MODEL                     1027853           98.02
LOAN_PRICE                       1027830           98.02
LOAN_TERM                        1027832           98.02
Loan Id                          1027879           98.03
MODEL                            1027830           98.02
PRODUCT_NAME                     1027830           98.02
RETURNED                         1027828           98.02
RETURN_DATE                      1046831           99.83
RETURN_POLICY_COMPLIANCE         1046831           99.83
SALE_DATE                        1027828           98.02
SALE_ID                          1027828           98.02
SALE_TYPE                        1027830           98.02
SELLER                           1027905           98.03
SELLER_TYPE                      1032799           98.50

Total Rows: 1048575

------------------------- ENDS -------------------------
```

```bash
--------------------------------------------------
Missing values report for merged_credit_data table
--------------------------------------------------
                                 Missing Values  Percentage (%)
ACCOUNT_STATUS_L1                             0            0.00
ACCOUNT_STATUS_L2                             0            0.00
ADJUSTMENT_AMOUNT                         68293           95.57
ADVANCE                                       0            0.00
ARREARS                                       0            0.00
BALANCE                                       8            0.01
BALANCE_DUE_STATUS                            0            0.00
BALANCE_DUE_TO_DATE                          28            0.04
CLOSING_BALANCE                               8            0.01
CREDIT_CHECK_DONE                             0            0.00
CREDIT_EXPIRY                                 0            0.00
CUSTOMER_AGE                                  0            0.00
DATE                                          0            0.00
DAYS_PAST_DUE                                 0            0.00
DEPOSIT                                       8            0.01
DISCOUNT                                      0            0.00
EXPECTED_PAYMENT                              1            0.00
FIRST_EXPECTED_PAYMENT                        0            0.00
FIRST_PAYMENT                                 0            0.00
INITIAL_PAY                                   0            0.00
LOAN_ID                                       0            0.00
MAX_PAYMENT_DATE                            749            1.05
NEXT_INVOICE_DATE                             0            0.00
OVERPAYMENT_AMOUNT                            0            0.00
PAYMENT                                       0            0.00
PAYMENT_AMOUNT                            68293           95.57
PREPAYMENT_AMOUNT                             0            0.00
RETURN_DATE                               64570           90.36
SALE_DATE                                     0            0.00
TOTAL_DUE_TODAY                              28            0.04
TOTAL_PAID                                    0            0.00
TOTAL_PAID_WITH_ADJUSTMENTS_15D               0            0.00
Unnamed: 28                               71456          100.00
WEEKLY_RATE                                   8            0.01

Total Rows: 71456

------------------------- ENDS -------------------------
```

