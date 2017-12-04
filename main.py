from keras.models import Sequential
from keras.layers import Dense
import numpy

#fix random seed for reproducibility
numpy.random.seed(7)

#load data : pima indians dataset
dataset= numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
X=dataset[:,0:8]
Y=dataset[:,8]


#create models
model=Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1, activation='sigmoid'))
