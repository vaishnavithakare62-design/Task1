# Step 1: Load the Data

import pandas as pd

# Load CSV file
df = pd.read_csv("mall customer segmentation.csv")

# Display the first 5 rows
print(df.info())
print(df.head())

#Step 2: Inspect the Data
print(df.head())
print(df.info())
print(df.isnull().sum())

#Step 3: Remove Duplicate Rows
df = df.drop_duplicates()

#Step 4: Standardize Text Values
# Clean 'Gender' values
df['Gender'] = df['Gender'].str.strip().str.lower()

#Step 5: Rename Columns to Be Uniform
# Clean column names: lowercase, remove spaces
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

#Column names after renaming:
['customerid', 'gender', 'age', 'annual_income_(k$)', 'spending_score_(1-100)']
#You can also simplify further:
df.rename(columns={
    'customerid': 'customer_id',
    'annual_income_(k$)': 'annual_income_k',
    'spending_score_(1-100)': 'spending_score'
}, inplace=True)

#Step 6: Check and Fix Data Types
# Check data types
print(df.dtypes)
# Ensure 'age' is int and create a sample date column for demonstration
df['age'] = df['age'].astype(int)
# Optional: Add a dummy date column (if needed)
import pandas as pd
df['join_date'] = pd.date_range(start='2020-01-01', periods=len(df), freq='7D')
#Convert date to dd-mm-yyyy:
df['join_date'] = pd.to_datetime(df['join_date']).dt.strftime('%d-%m-%Y')

#Step 7: Export the Cleaned Data
df.to_csv("Cleaned_Mall_Customers.csv", index=False) 
