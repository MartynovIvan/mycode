import theano
from theano import tensor as T
import numpy as np

trX = np.linspace(-1, 1, 101)
print(trX)
trY = 2 * trX + np.random.randn(*trX.shape) * 0.33
print(trY)

X = T.scalar()
Y = T.scalar()

def model(X, w):
    return X * w

w = theano.shared(np.asarray(-1000., dtype=theano.config.floatX))
y = model(X, w)

cost = T.mean(T.sqr(y - Y))
gradient = T.grad(cost=cost, wrt=w)
updates = [[w, w - gradient * 0.01]]

train = theano.function(inputs=[X, Y], outputs=cost, updates=updates, allow_input_downcast=True)

for i in range(100):
    for x, y in zip(trX, trY):
        """print (x, y)"""
        v = train(x, y)
        """print (v)"""

"""print(v)"""
zipped = zip(trX, trY)
"""print(list(zipped))"""
        
print (w.get_value()) #something around 2