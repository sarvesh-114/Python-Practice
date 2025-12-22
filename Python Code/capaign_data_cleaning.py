import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('capaign data.csv')
data.head()

data.shape
data.columns
data.isnull().sum()
data.info()
data.describe()

data.columns = data.columns.str.strip().str.lower().str.replace(' ', '')
data.columns

data.head()
dirty_spend_mask = data['spend'].astype('str').str.contains('\$')
print(data.loc[dirty_spend_mask, ['campaign_id', 'spend']].head(3))
data['spend'] = data['spend'].astype('str').str.replace(r'[^\d.-]', '', regex = True)
print(data.loc[dirty_spend_mask, ['campaign_id', 'spend']].head(3))

data['spend'] = data['spend'].astype('float')
data.info()

data['channel'].nunique()
data['channel'].unique()
data['channel'].value_counts()
cleanup_map = {
    'Tik_Tok' : 'TikTok',
     'Facebok' : 'Facebook',
    'Insta_gram' : 'Instagram',
    'Gogle' : 'Google Ads',
    'E-mail' : 'Email',
    'N/A' : np.nan
}
data['channel'] = data['channel'].replace(cleanup_map)
data['channel'].value_counts()

data['active'].nunique()
data['active'].unique()
data['active'].value_counts()
cleanedup_map = {
    '1' : 'Yes',
    'True' : 'Yes',
    "Y" : 'Yes',
    '0' : 'No',
    'False' : 'No'
}
data['active'] = data['active'].replace(cleanedup_map)
data['active'].value_counts()

data['start_date'].dtype
data['start_date'] = pd.to_datetime(data['start_date'], errors = 'coerce')
data['end_date'] = pd.to_datetime(data['end_date'], dayfirst = True, errors = 'coerce')
data['start_date'].dtype

data = data.loc[:, ~data.columns.duplicated()]
impossible_mask = data['clicks'] > data['impressions']
print(data.loc[impossible_mask, ['campaign_id', 'impressions', 'clicks']].head())

time_travel_mask = data['end_date'] < data['start_date']
print(data.loc[time_travel_mask, ['campaign_id', 'end_date', 'start_date']].head())
data.loc[time_travel_mask, 'end_date'] = data.loc[time_travel_mask, 'start_date'] + pd.Timedelta(days = 30)
print(data.loc[time_travel_mask, ['campaign_id', 'end_date', 'start_date']].head())

Q1 = data['spend'].quantile(0.25)
Q3 = data['spend'].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + (3 * IQR)
outlier_mask = data['spend'] > upper_limit
print(data.loc[outlier_mask, ['campaign_id', 'spend']].head(5))
data.loc[outlier_mask, 'spend'] = upper_limit
print(data.loc[outlier_mask, ['campaign_id', 'spend']].head(5))


