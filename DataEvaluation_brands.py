import pandas as pd
import json

# Load JSON file 
with open('brands.json', 'r') as f:
    data_brands = [json.loads(line) for line in f]  

# Convert to DataFrame
df_brands = pd.json_normalize(data_brands)

# Null values

print("Null values")
print(df_brands.isnull().sum())
# There are many variables with null values

# Duplicates

print("Duplicates")
print(df_brands['_id.$oid'].duplicated().sum())
# There are no duplicates

# Checking boolean values

print(df_brands["topBrand"].value_counts(dropna=False))
# Probably the NaN in topBrand should be converted to false

# Checking barcode

invalid_barcodes = df_brands[~df_brands["barcode"].str.isnumeric()]
# All of them are numeric





