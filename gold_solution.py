# -*- coding: utf-8 -*-
"""gold_solution

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kc42QtsdD6kcLElNvfFmGPWc98Jfkkiy

# IMPORTING LIBRARIES
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')
from sklearn.linear_model import LinearRegression

"""# INITIAL DATA PROCESSING """

df = pd.read_csv("gold_price.csv", parse_dates=True, index_col='Date')

df.head()

df.describe()

df.info

df['Return'] = df['USD (PM)'].pct_change() * 100
df['Lagged_Return'] = df.Return.shift()
df = df.dropna()
train = df['2001':'2018']
test = df['2019']

"""# CREATE TRAIN AND TEST SET"""

# Create train and test sets for dependent and independent variables
X_train = train["Lagged_Return"].to_frame()
y_train = train["Return"]
X_test = test["Lagged_Return"].to_frame()
y_test = test["Return"]

"""# DEVELOP MODELS AND PREDICTION"""

#PREDICTION
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

#VISUALISITION
import matplotlib.pyplot as plt
out_of_sample_results = y_test.to_frame()
# Add a column of "out-of-sample" predictions to that dataframe:  
out_of_sample_results["Out-of-Sample Predictions"] = model.predict(X_test)
out_of_sample_results.plot(subplots=True, title='Gold prices, USD')
plt.show()