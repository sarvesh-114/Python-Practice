import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('bios.csv')
data.head()

data.columns

data.shape

data.info()

data['Used name'] = data['Used name'].str.replace('•', ' ')
data['Full name'] = data['Full name'].str.replace('•', ' ')
data['Roles'] = data['Roles'].str.replace('•', ' ')
data[['Height', 'Weight']] = data['Measurements'].str.split('/', expand = True)
data.drop(columns = ['Measurements'], inplace = True)
data.rename(columns = {
    'Height' : 'Height_CM',
    'Weight' : 'Weight_KG'
}, inplace = True)
data['Height_CM'] = data['Height_CM'].str.replace('cm', '')
data['Weight_KG'] = data['Weight_KG'].str.replace('kg', '')

