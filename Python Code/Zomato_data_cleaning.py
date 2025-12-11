import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')

data = pd.read_csv(r"C:\Users\sarvesh jathar\Downloads\archive (1)\zomato.csv")
data.head()

data.info()

data.shape

'''
Data Cleaning:
Deleting redundant columns.
Renaming the columns.
Dropping duplicates.
Cleaning individual columns.
Remove the NaN values from the dataset
Check for some more Transformations 
'''

columns_to_drop = ['url', 'address', 'votes',
       'phone', 'location', 'rest_type', 'cuisines', 'reviews_list', 'menu_item',
       'listed_in(type)', 'listed_in(city)']

columns_to_keep = ['name', 'online_order', 'book_table', 'rate', 'dish_liked', 
                   'approx_cost(for two people)']

data.shape
len(columns_to_drop)
len(columns_to_keep)

modify_data = data[columns_to_keep]

modify_data.head()

data.drop(columns = columns_to_drop, inplace = True)

data.columns

data.columns.str.capitalize()

data.rename(columns = {'name' : 'Name'})

data.columns = data.columns.str.capitalize()

data.head()
