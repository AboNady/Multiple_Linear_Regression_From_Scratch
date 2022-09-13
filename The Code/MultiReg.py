#Please refer to the README File for the full formulas and explanation

import time #To Calculate the execution time
import numpy as np #To deal with Math
import pandas as pd #To handle the data's part
import matplotlib.pyplot as plt #To Draw the graphs

strt = time.time() #Calculate the time


#------------------------------------------------------------


def costfunc(x,y,thetas):  

    pred = x * thetas.T
    sm = np.sum(    (np.power( (pred-y) , 2 ))   )
    c =  sm   /    (2 * (x.shape[0]) ) #x.shape[0] is the same len(x)
    return c



#------------------------------------------------------------


def Gradientdes(x,y, thetas, alpha,iters):

    parameters = int( thetas.ravel().shape[1]  )
    
    
    for i in range(iters):
        #    30 2    2 1
        pred = x * thetas.T 
        for e in range(parameters):

            term = np.multiply( ( pred - y) ,x[: , e] )
            
            thetas[0,e] = thetas[0,e] - (   (alpha/len(x) )       * np.sum(term)          )
            
        cosf.append( costfunc(x, y, thetas) )
        
    return thetas


#------------------------------------------------------------


#Import the Dataset file. A txt file
datas = pd.read_csv(r'C:\Users\NADY\Desktop\d5.txt', header = None , names=['Xdata0','Xdata1','Ydata'] ) #Write your path here

#Data Normalization
datas =  ( datas - datas.mean() ) /  ( datas.std() )
datas.insert(0,'Ones',1)

cosf = [] #An empty list for the cost function, so I can draw the graph of the Cost Function

#We have the data as 97*2, So, I want to choose specific columns 
x = datas.iloc[: , : -1]
y = datas.iloc[: , -1] 

#Convert it into a matrix form, so we can handle and multiply it easily 
#NOTE: if did not multiply the data with 0.1 there will be
x = np.matrix(x.values) 
# I needed to transpose y, otherwise, it will not work properly, try it
y = np.matrix(y.values).T
thetas =np.matrix( np.zeros( (x.shape[1]) ) )

#------------------------------------------------------------


alpha = 0.01 #Step Size
iters = 600 # Number of iterations

equation = Gradientdes(x, y, thetas, alpha, iters)

#Xnew is to draw the fit line values, so find the Max and Min Points to draw the line between them as X values
xnew = np.linspace(x.min(), x.max() , 5)

#The Y of the predicted fit line
f = equation[0,0] + ( equation[0,1] * xnew ) + ( equation[0,2] * xnew )



end = time.time()


cosf =  np.array(cosf) #I multiplied it to have smaller values for the cost function. However, you can skip this step

#------------------------------------------------------------

#Just print the values
print('\nThe equation is [c+mx1+mx2] : ', equation)


print('\nThe Cost Function value : ' , cosf[-1])


#------------------------------------------------------------


#Draw the Dataset and The Fit line in the same Graph 
fig, ax = plt.subplots(figsize=(5,5))
#The Fit line
ax.plot(xnew, f, 'r', label='Prediction')
#The Dataset
ax.scatter(np.array(x[:,1]) ,np.array(y) , label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('X1')
ax.set_ylabel('y')
ax.set_title('X1 vs. Y')



#------------------------------------------------------------


#Draw the Dataset and The Fit line in the same Graph 
fig, ax = plt.subplots(figsize=(5,5))
#The Fit line
ax.plot(xnew, f, 'r', label='Prediction')
#The Dataset
ax.scatter(np.array(x[:,2]) ,np.array(y) , label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('x2')
ax.set_ylabel('y')
ax.set_title('X2 vs. Y')



#------------------------------------------------------------

 
# draw error graph
fig, ax = plt.subplots(figsize=(5,5))
ax.plot( np.arange(iters) , cosf , 'r')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost Value')
ax.set_title('Error vs. Training Epoch')

#------------------------------------------------------------


print('\nThe Excuation time is : ',end-strt,'Second')

