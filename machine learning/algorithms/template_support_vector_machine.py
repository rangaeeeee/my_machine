# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load the dataset


# support vector machine algorithm
from sklearn import svm
model = svm.svc()

# split the data into training and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# train the model
model.fit(X_train, y_train)
model.score(X_train, y_train)

# Predict the output
predicted = model.predict(X_test)
