from pathlib import Path
import pandas as pd

# 1. Define the path to your CSV file using relative paths
# This safely points to data/raw/Salary_dataset.csv relative to your repo root
csv_path = Path("data/raw/life_expectancy_table.csv")

try:
    # 2. Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    print("✅ Dataset loaded successfully!\n")

    # 3. Get rows and columns using df.shape (returns a tuple: (rows, columns))
    num_rows = df.shape[0]
    num_columns = df.shape[1]

    # 4. Get the column headers as a list
    column_headers = df.columns.tolist()

    # 5. Print out the metrics cleanly
    print(f"📊 Dataset Summary:")
    print(f"• Number of rows:    {num_rows}")
    print(f"• Number of columns: {num_columns}")
    print(f"• Column headers:    {column_headers}\n")

    # 6. Show the first 5 rows to peek at the data
    print("👀 First 5 rows of data:")
    print(df.head())

except FileNotFoundError:
    print(f"❌ Error: Could not find the file at {csv_path}")
    print("Double check that 'life_expectancy_table.csv' is inside your 'data/raw' folder.")
