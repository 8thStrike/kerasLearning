from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import numpy as np


dataset=np.loadtxt("Dlinear.csv", delimiter=",")

X=dataset[0:1000,0]
Y=dataset[0:1000,1]

'''
print("X : ")
print(X)

print("Y : ")
print(Y)
'''

#create models
model=Sequential()
model.add(Dense(3, input_dim=1, activation='sigmoid'))
model.add(Dense(3, activation='sigmoid'))
model.add(Dense(1,activation='sigmoid'))

#choosing the optimizer
sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

#compile model
model.compile(loss='mean_squared_error', optimizer=sgd, metrics=['accuracy'])

#fit the model
model.fit(X,Y, epochs=30000, batch_size=100)

scores=model.evaluate(X,Y)
print("\n&s: %.2f%%" %(model.metrics_names[1], scores[1]*100))
print(model.summary())
