#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import seaborn as sns


# In[10]:


tips = sns.load_dataset("tips")
tips.head()


# In[14]:


sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size")


# In[18]:


sns.scatterplot(x="total_bill", y="tip", data=tips, color = 'r', marker = 'v')


# In[ ]:





# In[ ]:




