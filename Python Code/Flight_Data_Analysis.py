import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

 df = pd.read_csv("airlines_flights_data.csv")
df.head()

df.shape

df.info()

df.describe()

# Data Cleaning

df = df.drop(columns = 'index')

categorical_columns = ["airline", "stops", "departure_time", "stops", "class"]
def value_counts(columns):
    for cols in columns:
        print(f"Value counts of {cols}")
        print(df[cols].value_counts())

value_counts(categorical_columns)

# Flights with most and least duration point
df[df["duration"] ==49.830000]

df[df["duration"] ==0.830000]

columns = df.columns
def value_counts(columns):
    for cols in columns:
        print(f"There are total {df[cols].isnull().sum()} Null values in {cols} column")

value_counts(columns)

# Q1 What are the ailines in dataset, accompanied with their frequencies
sns.countplot(data = df, x = "airline")
plt.xlabel("Airlines")
plt.ylabel("Counts")
plt.title("Frequqncy of Airlines")
df["airline"].value_counts()

#Q2 show bar graphs representing the departure time and arival time
sns.countplot(data = df, x = "departure_time")
plt.xlabel("departure_time")
plt.ylabel("Counts")
plt.title("Frequqncy of departure_time")
df["departure_time"].value_counts()

sns.countplot(data = df, x = "arrival_time")
plt.xlabel("arrival_time")
plt.ylabel("Counts")
plt.title("Frequqncy of arrival_time")
df["arrival_time"].value_counts()

plt.figure(figsize = (9, 5))
plt.subplot(1,2,1)
df["source_city"].value_counts(ascending = True).plot(kind = "bar")
plt.subplot(1,2,2)
df["destination_city"].value_counts(ascending = True).plot(kind = "bar")

#Q4 Does the price varies with airlines?
print(df.groupby('airline')["price"].mean().round().sort_values(ascending = True))
plt.barh(df.groupby('airline')["price"].mean().round().index.sort_values(ascending = True)
,df.groupby('airline')["price"].mean().round().values)

#Option 2
sns.catplot(
    data = df,
    x = 'airline',
    y = 'price',
    kind = 'bar',
    palette = 'rocket',
    hue = 'class'
)
plt.show()

# Q5 Does the ticket prices chage based on the departure and arrival time
df.groupby('departure_time')['price'].mean().round()
plt.figure(figsize = (8, 5))
sns.catplot(
    data = df,
    x = 'departure_time',
    y = 'price',
    kind = 'bar',
    palette = 'rocket'
)
plt.show()

df.groupby('arrival_time')['price'].mean().round()
sns.catplot(
    data = df,
    x = 'arrival_time',
    y = 'price',
    kind = 'bar',
    palette = 'rocket'
)
plt.show()

# Q6 Does the ticket prices chage based on the source and destination time
df.groupby('source_city')['price'].mean()
df.groupby('destination_city')['price'].mean()

sns.relplot(x = 'destination_city', y = 'price', data = df, col = 'source_city', kind = 'line')
sns.relplot(x = 'source_city', y = 'price', data = df, col = 'destination_city', kind = 'line')
