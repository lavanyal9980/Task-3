import pandas as pd 
import numpy as np

df = pd.read_csv(r"C:\Users\Lavanya\Downloads\archive1\train.csv")

print(df.head())

print(df.describe())

print(df.info())

print(df.isnull().sum())

df['Postal Code'] = df['Postal Code'].fillna(0)

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

df_yearly_sales = df.groupby('Year')['Sales'].sum().reset_index()

df_yearly_sales['YoY Growth'] = df_yearly_sales['Sales'].pct_change() * 100

print(df_yearly_sales)



