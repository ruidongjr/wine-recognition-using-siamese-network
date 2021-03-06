#%% Import libraries
import os
import numpy as np
import helper


#%% Define some params
FACE_DATA_PATH = "./dataset/wine"

NUMPY_DATA_PATH = './dataset/numpy'
X_data_name = 'X_data.npy'
Y_data_name = 'Y_data.npy'

TOTAL_SAMPLE_SIZE = 20000
RESIZE_DIMENSION = (100, 150)


#%% Main
X, Y = helper.get_data(FACE_DATA_PATH, RESIZE_DIMENSION, TOTAL_SAMPLE_SIZE)

## save the data
if not os.path.exists(NUMPY_DATA_PATH):
  os.mkdir(NUMPY_DATA_PATH)

np.save(os.path.join(NUMPY_DATA_PATH, X_data_name), X)
np.save(os.path.join(NUMPY_DATA_PATH, Y_data_name), Y)