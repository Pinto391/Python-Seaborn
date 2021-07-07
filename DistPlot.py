#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


pen=sns.load_dataset("penguins")


# In[3]:


pen


# In[4]:


pen.head()


# In[6]:


sns.distplot(pen.flipper_length_mm,rug=True)


# In[7]:


sns.distplot(pen.flipper_length_mm,kde=False)


# In[8]:


sns.distplot(pen.flipper_length_mm,hist=False)


# In[17]:


sns.distplot(pen.flipper_length_mm,hist_kws={'color':'green'},kde_kws={'color':'red','lw':2})


# In[ ]:




