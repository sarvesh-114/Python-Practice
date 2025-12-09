import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('Airbnb_Open_Data.csv')
data.head()

data.columns

data.dtypes

data.info()

data.describe()

data.shape

data.columns

columns_to_keep = ['NAME', 'host id', 'host_identity_verified', 'host name',
       'neighbourhood group', 'neighbourhood', 'lat', 'long', 'country',
       'country code', 'instant_bookable', 'cancellation_policy', 'room type',
       'Construction year', 'price', 'service fee', 'minimum nights',
       'number of reviews', 'last review']

columns_to_drop = ['id', 'reviews per month',
       'review rate number', 'calculated host listings count',
       'availability 365', 'house_rules', 'license']


len(columns_to_keep)

len(columns_to_drop)

df = data[columns_to_keep]

df.head()

#step 1
# data = data.drop(columns = columns_to_drop)
#step 2
data.drop(columns = columns_to_drop, inplace = True)

df.shape

data.shape

data.shape

data.head()

data.rename(columns = {'NAME': 'Name'}, inplace = True)
data.head()

data.columns = data.columns.str.capitalize()

data.head()

data.duplicated().sum()

data['Host name'].duplicated().sum()

data['Host name'].unique()

data['Host name'].nunique()

data['Host name'].value_counts()

data.drop_duplicates(inplace = True)

data.shape

data.duplicated().sum()

data.isnull().sum()

data.isnull().sum().sum()

data.drop(columns = ['Last review'], inplace = True)

data.shape

data.head()

data.dropna(inplace = True)

data.isnull().sum(
)

data.isnull().sum().sum()

data["Host_identity_verified"].value_counts()

data["Host_identity_verified"] = data["Host_identity_verified"].str.upper()

data["Host_identity_verified"].head()

data['Instant_bookable'].apply(lambda x: 1 if x == True else 0)

data['Instant_bookable'] = data['Instant_bookable'].apply(lambda x: 1 if x == True else 0)

data['Instant_bookable']

type(data['Instant_bookable'][5])

data.head()

data.reset_index(inplace = True)


data.head()

data.drop(columns = 'index', inplace = True)

data.head()

type(data['Instant_bookable'][15])

data.shape

data['Price'] = data['Price'].str.replace('$', '')
data['Price'] = data['Price'].str.replace(' ', '')
data['Price'] = data['Price'].str.replace(',', '')
type(data['Price'][1])
data['Service fee'] = data['Service fee'].str.replace('$', '')
data['Service fee'] = data['Service fee'].str.replace(' ', '')
data['Service fee']
data['Price'].astype(int)

data['Service fee'].astype(int)
data.to_csv('Airbnb_Open_Data_Cleaned.csv')
cleaned_data = pd.read_csv('Airbnb_Open_Data_Cleaned.csv')
cleaned_data.head()
