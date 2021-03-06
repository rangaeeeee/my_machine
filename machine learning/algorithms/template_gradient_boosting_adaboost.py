# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load the dataset


# Gradient Boosting and Adaboost algorithm
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(n_estimators = 100, learning_rate = 1.0, max_depth = 1, random_state = 0)

# split the data into training and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# train the model
model.fit(X_train, y_train)
model.score(X_train, y_train)

# Predict the output
predicted = model.predict(X_test)
