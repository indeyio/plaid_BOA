import requests
import json
import pandas as pd

# Having done all the stuff with Plaid API we send a request and go on
r = requests.get('http://127.0.0.1:5000/transactions')
data = json.loads(r.text)

transactions_dict = data['transactions']

# for key, value in transactions_dict.items():
#     print(key, value)

# Here are raw transactions that I was meant to upload to Google Sheets
raw_transactions = transactions_dict['transactions']

# print(len(raw_transactions))
df = pd.DataFrame.from_dict(raw_transactions)
# print(df.info())

df_needed = df[['date', 'category', 'amount']]
# print(df_needed)

df_needed['income/expense'] = df.amount.apply(lambda x: 'income' if x<0 else 'expense')
df_needed.amount = df_needed.amount.abs()
df_needed = df_needed.reindex(columns=['income/expense','date','category','amount'])
df_needed = df_needed.sort_values(['income/expense','date'])
print(df_needed)
# df_needed.to_csv('1st_attempt.csv', index=False)



