import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()
# print(diabetes.keys())

# dict_keys(['data', 'target', 'frame', 'DESCR', 
# 'feature_names', 'data_filename', 'target_filename', 
# 'data_module'])

# print(diabetes.data)
# print(diabetes.DESCR)

# diabetes_X = diabetes.data[:, np.newaxis, 2]
diabetes_X = diabetes.data
# print(diabetes_X)

# taking last 30 data for training
diabetes_X_train = diabetes_X[:-30]
# taking fist 30 data for testing
diabetes_X_test = diabetes_X[-30:]

# x axis = features
# y axis = labels

diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_predicted = model.predict(diabetes_X_test)

print("Mean squared error is: ", mean_squared_error(diabetes_y_test, diabetes_y_predicted))
print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)

# plt.scatter(diabetes_X_test, diabetes_y_test)
# plt.plot(diabetes_X_test, diabetes_y_predicted)
# plt.show()
