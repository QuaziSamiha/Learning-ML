import matplotlib as plt
import numpy as np
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes()
# print(diabetes.keys())

# dict_keys(['data', 'target', 'frame', 'DESCR', 
# 'feature_names', 'data_filename', 'target_filename', 
# 'data_module'])

# print(diabetes.data)
# print(diabetes.DESCR)

diabetes_X = diabetes.data[:, np.newaxis, 2]
print(diabetes_X)

