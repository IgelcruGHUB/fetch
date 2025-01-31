import pandas as pd
import json

# Load JSON file 
with open('users.json', 'r') as f:
    data_users = [json.loads(line) for line in f]  

# Convert to DataFrame
df_users = pd.json_normalize(data_users)

# Null values

print("Null values")
print(df_users.isnull().sum())
# signUpSource, state and lastLogin.$date have null values

# Duplicates

print("Duplicates")
print(df_users['_id.$oid'].duplicated().sum())
# There are many duplicates (id should be unique), the data needs to be cleaned

# Checking issues with dates

df_users['createdDate'] = pd.to_datetime(df_users['createdDate.$date'], unit='ms')
print(df_users['createdDate'].describe())
# Everything falls in the expected range

# Check categorical values

print(df_users['role'].value_counts())
print(df_users['signUpSource'].value_counts())
print(df_users['state'].value_counts())



