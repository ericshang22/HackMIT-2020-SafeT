import pandas as pd


df = pd.read_excel("CityofToronto_COVID-19_NeighbourhoodData.xlsx", sheet_name="Recent Cases and Rates by Neigh")
print (df.head())