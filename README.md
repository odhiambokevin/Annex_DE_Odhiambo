![GitHub last commit](https://img.shields.io/github/last-commit/odhiambokevin/Annex_DE_Odhiambo)

# ANNEX TECHNOLOGIES - Data Engineer Case Study

> [!Note]
> This is a fictitious case study of a phone company, ABC Phones.
> Fucntion calls are commented out at the end of data_profiling.py file. Uncomment and run as needed.
> Call the function `ingest_data()` in the `scripts/data_profiling.py` once. Comment it out once database is populated.

## Introduction
ABC Phones offers smartphones to customers through installment-based credit plans and manages these accounts throughout the repayment period. Customers make regular payments toward their outstanding balances, and credit decisions play a critical role in both portfolio performance and customer experience.

While ABC Phones has systems to process payments and manage accounts, their data engineering and analytics infrastructure is still maturing.

This is a scalable codebase that addresses their current challenges.
## Assumptions
The following assumptions are made for this project.
1. The Credit Data will always be accompanied by a relevant definitions file to allow the scripts in data_profiling.py to successfully create the 
resultant tables.
2. There is a "data folder" with the following structure in the root file (Same level as README)
3. Excel data needed for analysis are in `sheet1` as import always ignores other sheets in the workbook. Other data sheets will be factored for indepth engineering in production mode.

```
root folder
    ├── data folder
    │   ├── original (original data)
    │   └── staging (copy of original data)
    │       ├── NPS Data.xlsx
    │       ├── Sales and Customer Data.xlsx
    │       └── credit data folder
    │           ├── Credit Data - 01-01-2025.csv
    │           └── Credit Data - 01-02-2025.csv
    └── README.md
```

## Setup
1. Clone the repo using `git clone https://github.com/odhiambokevin/Annex_DE_Odhiambo.git`
2. Setup a virtual environment to install the python dependencies. UV with python version 3.12.3 is used.
3. Install the dependencies in the requirements.txt file. UV is used in this case `uv pip install -r requirements.txt`. To install UV check out this [link](https://docs.astral.sh/uv/getting-started/installation/)
4. Have a .env file that reads the environment variables that facilitate database connection.
5. Ensure to install the `ydata_profiling` package in your environemnt. Refer [here](https://docs.profiling.ydata.ai/latest/getting-started/installation/)

The BASE_DIR variable is used to set the root folder location using the `os module` as in `scripts/data_profiling.py`

## Cleaning Script
The cleaning script uses an order, in line with python's interpreted nature. For instance, the first step involves cleaning all the column names by standardizing them. These datasets with clean columns are used in the subsquent steps. The output of a preceeding step is used as the input in the proceeding step.

For ease of demonstration, stale datasets are kept in the code for producability of the steps. Of course this behavious would change for a production level database.

### Cleaning sequence
```mermaid
flowchart TD
    Columns renamed --> Exact Row Duplicates Removed --> Data Types Changed --> Output Sample CSV
```
