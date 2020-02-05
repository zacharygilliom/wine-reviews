import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np 


# Some basic summary stats to get an idea of how our data is shaped
def summary(df):
	print(df.head())
	print(df.columns)
	print(df.describe())
	print(df.dtypes)
	print(df.count())
	print(df.isna().sum())
	print('The Number of Unique Items in Each Column')
	for col in df.columns:
		print(str(col) + ':' + str(np.count_nonzero(df[col].unique())))


df = pd.read_csv('winemag-data-130k-v2.csv')
summary(df)

# based on the shape of our data, the majority of our price data is under $100.
df = df[df['price'] < 200]

# Plotting some of our location data and a distribution of our price data.
plt.subplot(311)
sns.barplot(x='price', y='region_2', data=df)

plt.subplot(312)
sns.barplot(x='price', y='taster_name', data=df)

plt.subplot(313)
sns.kdeplot(data=df['price'], shade=True)

plt.show()