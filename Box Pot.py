#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


pen=sns.load_dataset('penguins')


# In[5]:


pen.head()


# In[6]:


pen.describe()


# In[7]:


sns.boxplot(pen.bill_length_mm)


# In[8]:


sns.boxplot(y=pen.bill_length_mm,x=pen.island)


# In[10]:


sns.boxplot(y=pen.bill_length_mm,x=pen.island,hue=pen.sex)


# In[ ]:




