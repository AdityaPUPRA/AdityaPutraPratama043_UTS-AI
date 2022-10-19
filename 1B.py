#Aditya Putra Pratama/21091397043

#Multi Neuron

#Inisialisasi Numpy
import numpy as np

#Inisialisasi Variabel
inputs = [3.6, 7.3, 2.1, 5.6, 3.1, 1.0, 2.5, 1.9, 4.3, 6.0]
weights = [
    [1.3, 5.3, 7.1, 5.7, 8.5, 3.2, 1.4, 5.0, 2.3, 4.0],
    [2.4, 5.2, 4.4, 2.0, 4.6, 7.0, 5.5, 1.5, 9.0, 4.5],
[2.0, 1.8, 4.5, 2.0, 4.0, 2.5, 4.5, 3.0, 2.5, 8.5],
[2.0, 5.7, 3.0, 1.0, 2.0, 4.0, 2.0, 4.5, 1.5, 6.5],
[4.3, 5.0, 4.2, 2.6, 3.7, 4.8, 3.0, 4.0, 3.0, 6.0],
]
biases = [3.0, 1.0, 2.5, 4.5, 1.5]

#Output
outputs = np.dot(weights, inputs) + biases

#PrintOutput
print(outputs)