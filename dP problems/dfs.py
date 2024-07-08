import pandas as pd

df1 = pd.DataFrame({
    'itemnumber':['112345679','112345321','112345789','112343421'],
    'storenumber':['51','51','51','51'],
    'qty':[1,8,7,10],
    'date':['2024-07-21','2024-07-22','2024-07-21','2024-07-22'],
    })

df2 = pd.DataFrame({
    'itemnumber':['112345679','112345321','112345789','112343421'],
    'storenumber':['51','51','51','51'],
    'qty':[1,8,7,10],
    'date':['2024-07-21','2024-07-22','2024-07-01','2024-07-01'],
    })
df_diff = pd.concat([df1,df2]).drop_duplicates(keep=False).sort_index()
col=['item','store','quantity','planned_date']
df_diff.columns= col
print(len(df_diff))

print(df_diff)