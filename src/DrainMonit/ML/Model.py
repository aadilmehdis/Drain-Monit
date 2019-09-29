import numpy as np
import matplotlib.pyplot as plt


def prediction(X):

    '''
    X input array 4 x N matrix
        X[0] = elevation(m), X[1] = radius**2, X[2] = angle, X[3] = sqrt(Rainfall)
    Y output 1 x N matrix
        Y = water flow rate
    '''
    p = np.random.randint(12,high=14)*1000
    W = np.array([ 2.5, -25,  12.5,  250, p    ])
    Y = W @ X
    return Y


def regression(Y, X, learning_rate):

    '''
    X input array 4 x N matrix
        X[0] = elevation(m), X[1] = radius**2, X[2] = angle, X[3] = sqrt(Rainfall)
    Y output 1 x N matrix
        Y = water flow rate
    '''
    Xin = np.vstack((X,np.ones((1,X.shape[1]))))
    w = np.random.rand(5)* 10
    print(X.shape)
    for i in range(10000):

        Loss = np.mean((Y - w @ Xin)**2)
        w = w - (learning_rate*(Y - w @ Xin) @ (-Xin).T / X.shape[1])
        print(Loss)

    return w


if __name__ == "__main__":

    Data = np.genfromtxt('training_data_pipe.csv', delimiter = ',')
    print(Data.shape)
    rate = 0.000002
    # w = regression(Data[:80000,0].T, Data[:80000,1:5].T,rate)
    w = np.array([ 1.50697917, -0.98934085,  4.96066003,  9.62241236,  8.97676327])
    print(w)
    # datin = np.hstack((Data[80000,1:5],np.ones(())))
    print(np.mean((Data[80000:,0].T -  w @ np.hstack((Data[80000:,1:5],np.ones((Data[80000:,1:5].shape[0],1)))).T)**2))
