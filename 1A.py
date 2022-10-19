#Aditya Putra Pratama/21091397043

#Single Neuron

#Inisialisasi Numpy
import numpy as np

#Inisialisasi Variabel
inputs = [1.0, 1.5, 2.0, 3.5, 3.0, 1.5, 4.0, 2.5, 3.0, 7.2]
weights = [1.2, 3.4, 4.0, 2.4, 1.0, 2.2, 5.0, 3.2, 2.0, 2.0]
bias = 3.5

#Output
outputs = np.dot(weights, inputs) + bias

#PrintOutput
print(outputs)