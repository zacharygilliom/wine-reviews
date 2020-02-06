import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np 


# Some basic summary stats to get an idea of how our data is shaped
def summary(df):
	print(df.head())
	print(df.columns)
	print(df.describe())
	print('************ data types ************')
	print(df.dtypes)
	print('************ Count of each column ************')
	print(df.count())
	print('************ Count of NA Values ************')
	print(df.isna().sum())
	print('***** The Number of Unique Items in Each Column *****')
	for col in df.columns:
		print(str(col) + ':\n' + str(np.count_nonzero(df[col].unique())) + '\n')


def plot(df):
	# Plotting some of our location data and a distribution of our price data.
	plt.subplot(311)
	sns.barplot(x='price', y='region_2', data=df)

	plt.subplot(312)
	sns.barplot(x='price', y='taster_name', data=df)

	plt.subplot(313)
	sns.kdeplot(data=df['price'], shade=True)

	plt.show()


def df_country(df, country):
	df = df[df['country'] == country]
	summary(df)
	plot(df)
	return df


def get_unique(df):
	print('\n**** Unique values for country ****')
	print(df['country'].unique())
	print('\n**** Unique values for region 1 ****')
	print(df['region_1'].unique())
	print('\n**** Unique values for region 2 ****')
	print(df['region_2'].unique())
	print('\n**** Unique values for province ****')
	print(df['province'].unique())
	print('\n**** Unique values for taster name ****')
	print(df['taster_name'].unique())


def hist_plots(df):
	a = df['taster_name'].unique()
	print(a)
	b = range(1, len(df['taster_name'].unique()))
	print(list(b))
	c = len(df['taster_name'].unique())
	print(c)
	for i, j in zip(a, b):
		print(i, j)
		df1 = df[df['taster_name'] == i]
		plt.subplot(c, 1, j)
		sns.kdeplot(data=df1['price'], shade=True)
	plt.show()

df = pd.read_csv('winemag-data-130k-v2.csv')
# summary(df)

# based on the shape of our data, the majority of our price data is under $100.
# df = df[df['price'] < 200]

# summary(df)

# print(df_country(df, 'US'))
# plot(df)

# get_unique(df)

hist_plots(df)
