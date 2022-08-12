#!/usr/bin/env python
# coding: utf-8

# In[1]:


d=76
f=4
r=8
j=6
h=7
x=d/f*j-r+h
print(x)


# In[3]:


import os


# In[4]:


os.getcwd()


# In[5]:


import pandas as pd


# In[6]:


pd.read_excel(r"C:\Users\user\Desktop\data.xlsx")


# In[7]:


pd.read_csv(r"C:\Users\user\Desktop\Skyserver.csv")


# In[8]:


pd.read_csv(r"C:\Users\user\Desktop\team.tsv")


# In[9]:


pd.read_csv("team.tsv")


# In[10]:


pd.read_csv("Skyserver.csv")


# In[11]:


pd.read_excel("data.xlsx")


# In[18]:


pd.read_csv("data.tsv",sep="\t")


# In[19]:


pd.read_csv("team.tsv",sep="\t")?


# In[23]:


pd.read_csv("https://raw.githubusercontent.com/dsrscientist/dataset1/master/Social_Network_Ads.csv")


# In[26]:


pd.read_csv(r"C:\Users\user\Desktop\Social_Network_Ads.csv")


# In[28]:


pd.read_csv("Social_Network_Ads.csv")


# In[ ]:




