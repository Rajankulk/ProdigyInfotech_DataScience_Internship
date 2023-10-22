#Libraries
import numpy as np
# numpy is aliased as np
import pandas as pd
# pandas is aliased as pd
import matplotlib.pyplot as plt
# pyplot is aliased as plt
import seaborn as sns
# seaborn is aliased as sns

#dataset
df = pd.read_csv("F:\world bank.csv")
df

#first 5 rows
df.head()

#last 5 rows
df.tail()

#dimensions of data
df.shape

#showing rows
df.columns

#check for data types
df.dtypes

#info. of data
df.info()

#descriptive statistics 
df.describe()

##Data Preprocessing & Cleaning

#check duplicate values
df.duplicated().sum()

#check non-null values
df.isna().sum().any()
df = df.fillna(method="ffill")
df.head()

df.isna().sum().any()

#checking unique values of columns
df["Country Name"].unique()
df["Country Code"].unique()
df["Indicator Name"].unique()
df["Indicator Code"].unique()

#as we can clearly see that Indicator Name & Indicator Code has only single value. so, we will drop these 2 columns.
df.drop(["Indicator Name","Indicator Code","Country Code"], axis = 1, inplace = True)

df.columns

##Data Visualization

#Plotting Hstogram from 1960 to 2022

Cols = ['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']


for i in Cols:
        fig = plt.figure(figsize=(5,5))
        plt.hist(df[i],color='blue',bins=10)
        plt.xlabel(i)
        plt.show()
        
#plotting Bar plot from 1960 to 2022
years = df.columns[1:]

##add the values of each year for all countries
Total = df[years].sum()

plt.figure(figsize=(30,30))
plt.barh(years,Total,color='yellow')
plt.xlabel("Total of the country")
plt.ylabel("Year",size=20)
plt.title("Total count per year",size=20)
plt.show()

##Plotting histogram for indicators of top 10 countries by base year 1960
country_by_1960 = df.sort_values(by='1960').head(10)
country_by_1960

country_by_1960_t = country_by_1960.set_index("Country Name").T
for country_name,data_values in country_by_1960_t.iterrows():
    fig = plt.figure(figsize=(10,5))
    sns.barplot(x=data_values.index,y=data_values.values)
    plt.xlabel("Countries")
    plt.ylabel("Data Values")
    plt.title(f"{country_name} - Data Values from 1960 to 2022")
    plt.xticks(rotation=90)
    plt.show()
    
##Plotting histogram for indicators of top 10 countries by base year 2022
country_by_2022 = df.sort_values(by='2022').head(10)
country_by_2022

country_by_2022_t = country_by_2022.set_index("Country Name").T
for country_name,data_values in country_by_2022_t.iterrows():
    fig = plt.figure(figsize=(10,5))
    sns.barplot(x=data_values.index,y=data_values.values)
    plt.xlabel("Year")
    plt.ylabel("Data Value")
    plt.title(f"{country_name} - Data Values from 1960 to 2022")
    plt.xticks(rotation=90)
    plt.show()
    
###Conclusion : In this task, we have employed the World Development Indicator Dataset, which comprises indicator data for various countries spanning the years from 1960 to 2022. analysis has revealed a consistent trend of year-over-year increases in indicator values. Notably, when I established 1960 as the base year, Monaco emerged as the country with the highest indicator values in the initial years, while in the later years, the Turks and Caicos Islands took the lead. However, when I used 2022 as the base year, the Marshall Islands exhibited the highest indicator values. These observations underscore the dynamic nature of indicator values across different countries, with fluctuations in terms of the country holding the highest indicator values as the years progress.
    