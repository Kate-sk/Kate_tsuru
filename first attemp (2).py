#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import csv
import time


# In[2]:


get_ipython().run_line_magic('matplotlib', 'notebook')

# fig parameters
fig = plt.figure()
ax = fig.add_subplot(111)
ax = p3.Axes3D(fig)
#fig.show()

# Setting the axes properties
ax.set_xlim3d([-2.0, 2.0])
ax.set_xlabel('X')

ax.set_ylim3d([-2.0, 2.0])
ax.set_ylabel('Z')

ax.set_zlim3d([0.0, 2.0])
ax.set_zlabel('Y')

ax.set_title('3D Trajectory')


# In[3]:


#%run Live_data_collection.ipynb


# In[4]:


#filename
filename = 'my_live_data_new.csv'
open(filename,'w')


# In[5]:


#data reading
def read_me(file):
    f=pd.read_csv(file)
    lst=['X','Y','Z']
    f.columns=lst
    return f


# In[6]:


#f.get_values()
#A=f.get_values().astype(np.float)
#ax.scatter(A[:][0],A[:][1],A[:][2], color='b')


# In[7]:


#cleaning data
def clean_me(f): 
    f['X']=f['X'].str.replace("(", "")
    f['Z']=f['Z'].str.replace(")", "")


# In[8]:


#making array
def array_me(f):
    X = np.array(f['X']).astype(np.float)
    Y = np.array(f['Y']).astype(np.float)
    Z = np.array(f['Z']).astype(np.float)
    return X,Y,Z


# In[ ]:


i=0
x, y, z = [], [], []
#x=0
#y=0
#z=0

#run Live_data_collection
get_ipython().run_line_magic('run', 'Live_data_collection.ipynb')
time.sleep(1)


#infinite cycle 
while True:    
    f = read_me(filename)
    clean_me(f)
    X,Y,Z = array_me(f)
    #print(F)
    #for word in F:    
        #x.append(word[0])
        #y.append(word[1])
        #z.append(word[2])
    x.append(X[i])
    y.append(Z[i])
    z.append(Y[i])
    
    #x=X[i]
    #y=Y[i]
    #z=Z[i]
    
    ax.scatter(x, y, z, color='r')
    ax.plot(x, y, z, color='b')    
    fig.canvas.draw()
    #fig.show()
    
    #    ax.set_xlim(left=max(0, i-50), right=i+50)
    #    dt=t[i+1]-t[i]+0.01
    t=0.05
    time.sleep(t)
    i += 1 


# 
