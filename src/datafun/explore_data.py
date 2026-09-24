from pathlib import Path
import pandas as pd

# Define the path to the CSV file 
csv_path = Path("data/raw/life_expectancy_table.csv")

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    print("✅ Dataset loaded successfully!\n")

    # Get number of rows and columns 
    num_rows = df.shape[0]
    num_columns = df.shape[1]

    # Get the column headers as a list
    column_headers = df.columns.tolist()

    # Print out the metrics 
    print(f"📊 Dataset Summary:")
    print(f"• Number of rows:    {num_rows}")
    print(f"• Number of columns: {num_columns}")
    print(f"• Column headers:    {column_headers}\n")

    # Show the first 5 rows of the data
    print("👀 First 5 rows of data:")
    print(df.head())

except FileNotFoundError:
    print(f"❌ Error: Could not find the file at {csv_path}")
    print("Double check that 'life_expectancy_table.csv' is inside your 'data/raw' folder.")
