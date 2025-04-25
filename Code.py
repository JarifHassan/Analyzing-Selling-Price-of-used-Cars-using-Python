import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

df = pd.read_csv('imports-85.csv', header=None)


print(df.head())

headers = ["symboling", "normalized-losses", "make",
           "fuel-type", "aspiration","num-of-doors",
           "body-style","drive-wheels", "engine-location",
           "wheel-base","length", "width","height", "curb-weight",
           "engine-type","num-of-cylinders", "engine-size",
           "fuel-system","bore","stroke", "compression-ratio",
           "horsepower", "peak-rpm","city-mpg","highway-mpg","price"]

df.columns=headers
print(df.head())


data = df

data.isna().any()
data.isnull().any()

data['city-mpg'] = 235 / df['city-mpg']
data.rename(columns = {'city_mpg': "city-L/100km"}, inplace = True)
print(data.columns)
data.dtypes

data['length'] = data['length']/data['length'].max()
data['width'] = data['width']/data['width'].max()
data['height'] = data['height']/data['height'].max()
# Replace '?' with NaN in the 'price' column
df['price'] = df['price'].replace('?', np.nan)

# Convert the 'price' column to a numeric type.
# 'errors="coerce"' will turn any values that cannot be converted into NaN.
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Drop rows where 'price' is NaN, as linspace cannot handle NaN values.
# Alternatively, you could impute missing values depending on your analysis needs.
df.dropna(subset=['price'], axis=0, inplace=True)

# Reset index after dropping rows
df.reset_index(drop=True, inplace=True)
# --- End of Data Cleaning ---


# Print the head of the DataFrame to verify the column names and cleaned data

bins = np.linspace(min(data['price']), max(data['price']),4)
group_names = ['Low', 'Medium', 'High']
data['price-binned'] = pd.cut(data['price'], bins, labels = group_names, include_lowest= True)

print(data['price-binned'])
plt.hist(data['price-binned'])
plt.show()


pd.get_dummies(data['fuel-type']).head()
data.describe()

plt.boxplot(data['price'])

sns.boxplot(x='drive-wheels', y= 'price', data=data)

plt.scatter(data['engine-size'], data['price'])

plt.title('Scatterplot of Enginesize vs Price')

plt.xlabel('Engine size')

plt.ylabel('Price')

plt.grid()
plt.show()

test = data[['drive-wheels', 'body-style', 'price']]
data_grp = test.groupby(['drive-wheels', 'body-style'],
                        as_index = False).mean()
data_grp

data_pivot = data_grp.pivot(index= 'drive-wheels',
                            columns = 'body-style')
data_pivot
plt.pcolor(data_pivot, cmap = 'RdBu')
plt.colorbar()
plt.show()


data_annova = data[['make','price']]
grouped_annova = data_annova.groupby(['make'])
annova_results_1 = sp.stats.f_oneway(
    grouped_annova.get_group('honda')['price'],
    grouped_annova.get_group('subaru')['price']
)
print(annova_results_1)
sns.regplot(x='engine-size', y= 'price', data=data)
plt.ylim(0,)