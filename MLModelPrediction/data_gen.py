import numpy as np
import matplotlib.pyplot as plt


'''
input Rainfall (mm)
input Angle (degrees)
input Radius(m)
input elevation(m)


output average flow rate (volume mm/ second)
'''

elevation = 500 + np.random.rand(20) * 300
Radius_pipe = 3 + np.random.rand(20) * 10
angle = np.random.rand(20) * 60
Rainfall = 250 + np.random.rand(5000) * 400

X = np.array([[]])
Y = np.array([[]])

W = [1.5, -1, 5, 10]

for i in range(5000):
    for j in range(20):
        
        temp = np.array([[elevation[j], Radius_pipe[j]**2, angle[j],np.sqrt(Rainfall[i])]])
        if j == 0 and i == 0:
            X = temp
            # print(temp)
            Y = W @ temp.T + np.random.rand(1) * 10
        else:    
            X = np.vstack((X,temp))
            Y = np.vstack((Y, W @ temp.T + np.random.rand(1)*10)) 

Total_data = np.hstack((Y,X))
np.savetxt('training_data_pipe.csv',Total_data, delimiter = ',')

