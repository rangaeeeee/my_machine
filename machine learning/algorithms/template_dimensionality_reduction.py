# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load the dataset


# Dimensionality Reduction algorithm
from sklearn import decomposition 
model = decomposition.PCA()

# split the data into training and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# train the model
train_reduced = model.fit_transform(X_train)
test_reduced  = model.transform(X_test)
