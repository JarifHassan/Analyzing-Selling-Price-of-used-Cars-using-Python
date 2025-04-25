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