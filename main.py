import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np 

sns.set_style('darkgrid')
sns.set_palette("GnBu_d")


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
	get_unique(df)

# Useful to find the number of unique values for some of our categorical variables to get an idea of the shape of our dataset.
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


# Given the NA values in our countries column, it would be easier to just remove the rows that don't have a country value.
def clean_country_na(df):
	df.dropna(subset=['country'], inplace=True)
	return df

# We will use the next two functions to create the histogram plot of all of our wine tasters and countres.  
# We wil plot all of them on the same axis and we will only plot the top values.
def hist_plots_taster_name(df):
	a = get_v_counts(df, 'taster_name')
	b = range(1, len(a) + 1)
	c = len(a)
	for i, j in zip(a, b):
		sns.kdeplot(data=df[df['taster_name'] == i]['points'], shade=False, label=i, kernel='gau')
	plt.title('KDE Plots of Points for the top Wine Tasters by number of reviews')
	plt.xlabel('Points')
	plt.ylabel('KDE Distribution')


def hist_plots_country(df):
	a = get_v_counts(df, 'country')
	b = range(1, len(a) + 1)
	c = len(a)
	for i, j in zip(a, b):
		sns.kdeplot(data=df[df['country'] == i]['points'], shade=False, label=i, kernel='gau')
	plt.title('KDE Plots of Points for the top Countries by number of reviews')
	plt.xlabel('Points')
	plt.ylabel('KDE Distribution')

# want to find the top column values in all the rows, regardless of how many distinct values there are.
def get_top_v(df, col):
	sum_list = []
	for w in df[col].unique():
		df1 = df[df[col] == w]
		sum_list.append(df1.shape[0])
	total = sum(sum_list)
	avg = total / (1.25 * np.count_nonzero(df[col].unique()))
	return avg

# Add the top values to a list
def get_v_counts(df, col):
	top_v = []
	for v in df[col].unique():
		df1 = df[df[col] == v]
		if df1.shape[0] > get_top_v(df, col):
			top_v.append(v)
	return top_v

# Create our figures, subplots, and some formatting
def plot(df):
	df = clean_country_na(df)
	figure, axes = plt.subplots(nrows=2, ncols=1)
	plt.subplot(211)
	hist_plots_country(df)
	plt.subplot(212)
	hist_plots_taster_name(df)
	figure.tight_layout(pad=0.5)
	plt.show()

# Load in our dataset
df = pd.read_csv('winemag-data-130k-v2.csv')

# First we want to print some summary stats of our dataset
summary(df)

# PLotting our data
plot(df)

