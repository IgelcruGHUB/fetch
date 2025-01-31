import pandas as pd
import json

# Load JSON file 
with open('receipts.json', 'r') as f:
    data_receipts = [json.loads(line) for line in f]  

# Convert to DataFrame
df_receipts = pd.json_normalize(data_receipts)

# Null values

print("Null values")
print(df_receipts.isnull().sum())
# There are many variables with null values

# Duplicates

print("Duplicates")
print(df_receipts['_id.$oid'].duplicated().sum())
# There are no duplicates

# We have to check if every user in a receipt exists in the users database
# Load JSON file 
with open('users.json', 'r') as f:
    data_users = [json.loads(line) for line in f]  

# Convert to DataFrame
df_users = pd.json_normalize(data_users)

# Extract user IDs from receipts and users DataFrames
receipt_user_ids = df_receipts['userId'].unique()  
user_ids = df_users['_id.$oid'].unique()  

# Check which users in receipts are missing in users
missing_users = set(receipt_user_ids) - set(user_ids)

# Print results
if missing_users:
    print("Missing users in users.json for the following user IDs:")
    for user_id in missing_users:
        print(f"- {user_id}")
else:
    print("All users in receipts have corresponding entries in users.json.")
    
# It is important to check what happened with these users




