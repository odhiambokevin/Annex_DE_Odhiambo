#############################################
ANNEX TECHNOLOGIES - Data Engineer Case Study
#############################################

.. note::
    This is a fictitious case study of a phone company, ABC Phones.

============
Introduction
============
ABC Phones offers smartphones to customers through installment-based credit plans and manages these accounts throughout the repayment period. Customers make regular payments toward their outstanding balances, and credit decisions play a critical role in both portfolio performance and customer experience.

While ABC Phones has systems to process payments and manage accounts, their data engineering and analytics infrastructure is still maturing.

This is a scalable codebase that addresses their current challenges.

===========
Assumptions
===========
The following assumptions are made for this project.
1. The Credit Data will always be accompanied by a relevant definitions file to allow the scripts in data_profiling.py to successfully create the 
resultant tables.
2. There is a "data folder" with the following structure in the root file (Same level as README)

    data folder
    ├── original (the original data from source)
    ├── staging (copy of the original)
    │   ├── Credit Data
    │   │   ├── Credit Data - 01-01-2025.csv
    │   │   ├── Credit Data - 01-01-2025.csv
    │   │   ├── Credit Data - 01-01-2025.csv
    │   │   └── Credit Data - 01-01-2025.csv
    │   ├── NPS Data.xlsx
    │   └── Sales and Customer Data.xlsx
    └── README.md
    

=====
Setup
=====
1. Clone the repo using ""
2. Setup a virtual environment to install the python dependencies. UV with python version 3.12.3 is used.
3. Install the requirements.txt file
4. Have a .env file that reads the environment variables that facilitate database connection

The BASE_DIR variable is used to set the root folder location using the os module as in scripts/data_profiling.py