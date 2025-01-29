import pandas as pd
import csv

# Set the file path
file_path = 'rawdata1.csv'


# Read the file using Pandas
data = pd.read_csv(file_path, na_values=['no data'],)

# Remove special characters
data = data.replace({r'\#': '', r'\*': ''}, regex=True)

# Drop rows with missing data
data = data.dropna()


# Convert ALL columns to numeric where possible
for col in data.columns:
    data[col] = pd.to_numeric(data[col], errors='ignore')

# Identify numeric columns again (after conversion)
numeric_cols = data.select_dtypes(include=['number']).columns

# Round to 2 decimal places (keeping them as floats)
data[numeric_cols] = data[numeric_cols].apply(lambda x: x.round(1))




cleaned_file_path = 'cleandata1.csv'
data.to_csv(cleaned_file_path, index=False)


print("Clean data file saved to:", cleaned_file_path)

