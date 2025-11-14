import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('train.csv')
df.head()

# Problem Statement A retail company “ABC Private Limited” wants to understand the customer
# purchase behaviour (specifically, purchase amount) against various products of different 
# categories. They have shared purchase summary of various customers for selected high volume 
# products from last month. The data set also contains customer demographics (age, gender, 
# marital status, city_type, stay_in_current_city), product details (product_id and product category) 
# and Total purchase_amount from last month.
# Now, they want to build a model to predict the purchase amount of customer against various 
# products which will help them to create personalized offer for customers against different products.

test = pd.read_csv('test.csv')
test.head()

data = pd.concat([train, test], ignore_index=True)
data.head()

data.info()

data.describe()

data.drop(['User_ID'],axis = 1, inplace = True)
data.head()

data.shape

data.isnull().sum()

data['Gender'] = data['Gender'].map({'F' : 0, 'M' : 1})
