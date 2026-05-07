from data_profiling import get_database_data

raw_database_df = get_database_data()

#statistical overview of our data frames
if raw_database_df:
    for name, df in raw_database_df.items():
        print(f"\n--- Profiling Summary for: {name} ---")
        print(df.describe())
        print(df.info())