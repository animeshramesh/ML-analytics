__author__ = 'Animesh'

# Imports
from utils import load_model
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
import numpy as np
import math as pymath
from utils import math


epochs = 500

# Get the dataset in the required format
input_matrix = np.array(load_model.load_model())
params = math.normalize_matrix(input_matrix)
rain = np.array(params[:, -1:].tolist()).reshape(-1, 1)


# Initialize the layer sizes
input_size = params.shape[1]
hidden_size = input_size
target_size = rain.shape[1]

# Feed the data to the network
ds = SupervisedDataSet(input_size, target_size)
ds.setField('input', params)
ds.setField('target', rain)
net = buildNetwork(input_size, hidden_size, target_size, bias=True)

# Now the magic happens
trainer = BackpropTrainer(net, ds)

# Write the errors to a file
f = open('errors', 'w')
for i in range(epochs):
    mse = trainer.train()    # returns the error for the corresponding epoch
    rmse = pymath.sqrt(mse)  # obtain the Root Mean Square Error
    print "training RMSE, epoch {}: {}".format(i + 1, rmse)
    f.write(str(rmse) + '\n')

# Test it on the data set
result = net.activateOnDataset(ds)
for i in range(len(result)):
    print result[i], rain[i], " --> ", rain[i] - result[i]
