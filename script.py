import pandas as pd

# Loading csv file as a dataframe
file_path = "dataset_filtered 1(in).csv"
df = pd.read_csv(file_path, encoding='utf-8')

# Display the first 10 rows
print(df.head(10))

# Get the dataset information
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Display summary statistics
print(df.describe())