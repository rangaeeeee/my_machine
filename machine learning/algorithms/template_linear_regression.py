# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the training and test set
from sklearn import datasets
boston = datasets.load_boston()
X = boston.data
y = boston.target

# split the data into train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

# create the dataset for test and train
# import the linear regression model
from sklearn import linear_model
linear = linear_model.LinearRegression()

# train the model using training set
linear.fit(X_train, y_train)
linear.score(X_train, y_train)

# Equation co-efficient and Intercept
print("Co-efficient : \n", linear.coef_)
print("Intercept    : \n", linear.intercept_)

# predict the output
predicted = linear.predict(X_test)
