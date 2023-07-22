#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


car=pd.read_csv(r"C:\Users\Rishiraj Saha\Downloads\2. Cars Data1.csv")


# In[3]:


car


# In[4]:


car.head()


# In[5]:


car.shape


# In[6]:


car.isnull().sum()


# In[7]:


car['Cylinders'].fillna(car['Cylinders'].mean())


# In[8]:


car


# In[9]:


car.head


# In[10]:


car['Make'].value_counts()


# In[11]:


car['Origin'].isin(['Asia','Europe'])


# In[12]:


car[car['Weight'] > 4000]


# In[13]:


car['Cylinders'].fillna(car['Cylinders'].mean())


# In[17]:


car.head(2)


# # TO INCREASE ALL VALUES OF MPG_CITY BY THREE

# In[18]:


car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3)


# In[19]:


car


# In[ ]:




