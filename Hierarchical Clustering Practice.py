#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[8]:


data = pd.read_csv('C:\\Users\\Asus\\Desktop\\MachineLearning-Coursera\\Hierarchical Clustering Project\\Country clusters standardized.csv', index_col = 'Country')
data


# In[9]:


x_scaled = data.copy()
x_scaled = x_scaled.drop(['Language'], axis=1)
x_scaled


# ## Plot the Data

# In[10]:


sns.clustermap(x_scaled, cmap='mako')


# In[ ]:




