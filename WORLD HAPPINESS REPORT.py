#!/usr/bin/env python
# coding: utf-8

#  #  Author: Ayush Kakar
#   
# 
#  

#  

# #  Titanic - Machine Learning From Disaster - Dataset (World Happiness Report-2021)

# In[23]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[24]:


data=pd.read_csv('world-happiness-report-2021.csv')


# In[25]:


data


# In[26]:


data.columns


# In[27]:


data1=data[['Country name','Regional indicator','Ladder score','Logged GDP per capita',
         'Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption',
         'Ladder score in Dystopia']]


# In[28]:


data1.shape


# In[29]:


data1.isnull().sum()


# # Country Name Vs Ladder Score

# In[30]:


plt.figure(figsize=(30,10))
sns.barplot(data=data1,x='Country name',y='Ladder score')
plt.xticks(rotation=90)


# In[31]:


data1.corr()[['Ladder score']].sort_values(by='Ladder score',ascending=False)


# # Country Name Vs Freedom to make life choices

# In[32]:


plt.figure(figsize=(20,6))
sns.barplot(data=data1,x='Country name',y='Freedom to make life choices')
plt.xticks(rotation=120)


# In[33]:


data1.corr()[['Freedom to make life choices']].sort_values(by='Freedom to make life choices',ascending=False)


# # Country Name Vs GDP

# In[34]:


plt.figure(figsize=(30,10))
sns.barplot(data=data1,x='Country name',y='Logged GDP per capita')
plt.xticks(rotation=120)


# In[ ]:





# In[35]:


data1.corr()[['Logged GDP per capita']].sort_values(by='Logged GDP per capita',ascending=False)


# # GDP Vs Ladder score

# In[36]:


plt.figure(figsize=(30,10))
sns.barplot(data=data1,x='Logged GDP per capita',y='Ladder score')
plt.xticks(rotation=120)


# # Country Name Vs Generosity

# In[37]:


plt.figure(figsize=(30,10))
sns.barplot(data=data1,x='Country name',y='Generosity')
plt.xticks(rotation=120)


# In[38]:


data1.corr()[['Generosity']].sort_values(by='Generosity',ascending=False)


# # as we can see that GDP,HEATH,Social Support,Freedom to make life choices are positively correlated to happiness score but nobality(generosity)is negatively correlated with happiness score ie it is inversely proportional

# In[39]:


top_10_happiest=data1.sort_values(by='Ladder score',ascending=False).head(10)
top_15_unhappiest=data1.sort_values(by='Ladder score',ascending=False).tail(15)


# # Most Happiest Country( Country name Vs Ladder Score)

# In[41]:


plt.figure(figsize=(20,6))
sns.barplot(data=data1,x=top_10_happiest['Country name'],y=top_10_happiest['Ladder score'])


# # Thus we can see that Finland is the happiest country in the world¶

# # Most Unhappiest Country( Country name Vs Ladder Score)

# In[42]:


plt.figure(figsize=(20,6))
sns.barplot(data=data1,x=top_15_unhappiest['Country name'],y=top_15_unhappiest['Ladder score'])


# # Thus we can see that Afghanistan is the most unhappiest country in the world
# 

# In[ ]:





# In[ ]:





# In[ ]:




