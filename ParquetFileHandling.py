import pandas as pd
#reading from a CSV file and writing the contents to a PARQUET file
def write_parquet_file():
    df = pd.read_csv('C:/Users/anith/blog/customer2 - Copy.csv')
    df.to_parquet('Customer2.parquet')
write_parquet_file()

#reading from a PARQUET file
df = pd.read_parquet('Customer2.parquet')
print(df)