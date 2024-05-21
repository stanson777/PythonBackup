import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("IHME_GBD_2010_MORTALITY_AGE_SPECIFIC_BY_COUNTRY_1970_2010.csv")


print(df.info())

print(df.head())





unique_years=df['Year'].unique().tolist()

print(unique_years)
kolumny=df.columns
df['Number of Deaths']=df['Number of Deaths'].str.replace(",","").astype(int)
grouped=df.groupby(['Country Name','Year'])['Number of Deaths'].mean()




print(grouped)


df_countries={}


for (country,year),mean in grouped.items():
    if country not in df_countries:
        df_countries[country]=pd.DataFrame({'Year':[year],'Number of Deaths':[mean]})
    else:
        new_data = pd.DataFrame({'Year': [year], 'Number of Deaths': [mean]})
        df_countries[country] = pd.concat([df_countries[country], new_data], ignore_index=True)

print(df_countries['Afghanistan'])




