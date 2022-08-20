#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.read_excel(r"C:\Users\user\Desktop\6511.XLSX")


# In[6]:


pd.read_excel("6511.XLSX")


# In[7]:


import os


# In[8]:


os.getcwd()


# In[9]:


import keyword


# In[10]:


print(keyword.kwlist)


# In[11]:


True is True


# In[12]:


False is False


# In[13]:


1 is 0


# In[14]:


True and False


# In[16]:


True and False is False


# In[17]:


False is False and False


# In[18]:


pd.read_csv(r"C:\Users\user\Advertising.csv")


# In[19]:


pd.read_csv("advertising.csv")


# In[21]:


pd.read_csv("https://raw.githubusercontent.com/dsrscientist/DSData/master/Advertising.csv")


# In[23]:


pd.read_csv(r"C:\Users\user\file.tsv.txt")


# In[25]:


pd.read_csv("file.tsv.txt",sep="\t")


# In[ ]:




