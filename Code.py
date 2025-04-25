import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

df = pd.read_csv('imports-85.csv')

df = df.iloc[:,1:]

print(df.head())

