'''
Created on Sep 1, 2017

@author: bob
'''
import numpy as np
from pylab import meshgrid
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize
import matplotlib.pyplot as plt


rng = np.random
N=2 # number of different points for regression; I am only allowing values of -1 and 1
Xarray=10*rng.randn(N)
print("Xvalues ",Xarray,"\nshape of Xarray ",Xarray.shape)
V= rng.randint(size=N, low=0, high=2)
V=2*V-1  #note that the constant 2 is broadcast through the array as it should in linear algebra
print("values taken on ",V, "\nshape of V \n",V.shape)


def cost(w,b):
    costArray= np.abs(((w*Xarray+b)-V)) # taking square here to eventually take sum of squares
    return costArray.sum()
#print (cost(1,1))

def costWrapper(Avar):# just a wrapper function for sciPy
    return cost(Avar[0],Avar[1]) # I think I can give it an ordered pair

#
#vcostWrapper= np.vectorize(costWrapper)  #did not work wanted to be able to work on array of pairs
    
#
#print("usingwrapper ", costWrapper([1,1]))
#find the minimum from sciPy ; sort of ridiculous for square as is normal regression you can solve analytically
res = minimize(costWrapper,[.5,.5],method='Nelder-Mead')# this method doesnt use derivatives

print(" the actual minimimum values of w, b  are ",res.x[0],res.x[1])
print("the minimum it reached is ",res.fun)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# !!!!!!!!!!!!!!!!! should change -.8 to 1 to really see more correct graph !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
w= np.arange(res.x[0]-1,res.x[0]-.8,.05)  #change from 1 to -.8 to see arrays
b= np.arange(res.x[1]-1,res.x[1]-.8,.05) 
W,B= meshgrid(w,b) #grid of points
print("\n W array\n",W,"\n and shape of W \n",W.shape)
print("\nB array\n",B,"\n and shape of B \n",B.shape)
#===============================================================================
# Ztemp= list(zip(np.ravel(W),np.ravel(B)))
# Ztemp= np.array(Ztemp)
# print ("just zipped arrays as list of pairs \n",Ztemp, "\n and length of list \n",len(Ztemp))
# ZtempA= vcostWrapper(Ztemp,1)
# 
# 
# ZtempA= ZtempA.reshape(W.shape)
# print("\n reshaped array of z values \n",ZtempA)
#===============================================================================

zs=np.array([cost(w,b)for w,b in zip(np.ravel(W),np.ravel(B))]) #note is iterator
Z = zs.reshape(W.shape)
print(" \n  the Z after applying function \n",Z,"\n and shape of Z \n",Z.shape)   

ax.plot_surface(W, B, Z)
    
ax.set_xlabel('W Label')
ax.set_ylabel('B Label')
ax.set_zlabel('Z Label')
    
plt.show()


    