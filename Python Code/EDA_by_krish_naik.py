import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('zomato.csv', encoding = 'latin-1')

data.head()

data.columns

data.info()

data.describe()

data.isnull().sum()

data.shape

[features for features in data.columns if data[features].isnull().sum() > 0]

sns.heatmap(data.isnull(), yticklabels = False, cbar = False, cmap = 'viridis' )

data2 = pd.read_excel('country-code.xlsx')

pd.merge(data, data2, on = 'Country Code', how = 'left')

final_data = pd.merge(data, data2, on = 'Country Code', how = 'left')

final_data.head()

final_data.dtypes

final_data['Country'].value_counts()

#final_data['Country'].value_counts().index
country_names = final_data['Country'].value_counts().index

#final_data['Country'].value_counts().values
values = final_data['Country'].value_counts().values

plt.pie(values[:3], labels = country_names[:3])
plt.pie(values[:3], labels = country_names[:3], autopct = '%1.3f%%')

final_data.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size()
ratings_data = final_data.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns = {0: 'Rating Count'})

plt.figure(figsize = (8, 5))
sns.barplot(x = 'Aggregate rating', y= 'Rating Count' , data = ratings_data)
plt.xticks(rotation=45)
plt.ylabel("Rating Counts")
plt.xlabel("Ratings")
plt.show()

plt.figure(figsize = (8, 5))
sns.barplot(x = 'Aggregate rating', y= 'Rating Count' , data = ratings_data, hue = 'Rating color',
          palette = ['white', 'red','orange', 'yellow', 'green', 'green'] )
plt.xticks(rotation=45)
plt.gca().set_facecolor('#63666A')
plt.ylabel("Rating Counts")
plt.xlabel("Ratings")
plt.show()

