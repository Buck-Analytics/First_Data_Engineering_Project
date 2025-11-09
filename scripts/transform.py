import pandas as pd

df = pd.read_csv("data/seattle-weather.csv")

##Basic Abfragen
print(df.head())
print(df.info())
print(df.describe())

#Fehlende Werte - Keine Missing Values
print(df.isnull().sum())

#Datentyp überprüfen
print(df.dtypes)