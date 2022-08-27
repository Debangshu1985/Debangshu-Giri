#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


os.getcwd()


# In[3]:


print(type)


# In[4]:


import keyword


# In[5]:


print(keyword.kwlist)


# In[6]:


True is True


# In[7]:


False is False


# In[8]:


False is True


# In[9]:


True is False


# In[11]:


True and False


# In[12]:


False and True


# In[14]:


False+124 is True*124


# In[16]:


p=78
r=13
t=98
j=55
s=66
y=(p/r)+s-(t+j)
print(y)
type(y)


# In[17]:


w=(p+r+t+j+s)
print(w)
type(w)


# In[18]:


import pandas as pd


# In[19]:


pd.read_excel(r"C:\Users\user\Attendance.xlsx")


# In[20]:


pd.read_excel('Attendance.xlsx')


# In[21]:


pd.read_csv(r"C:\Users\user\empl.csv")


# In[23]:


pd.read_csv('empl.csv')


# In[24]:


pd.read_csv(r"D:\data 1\file.tsv.txt")


# In[28]:


pd.read_csv(r"D:\data 1\file.tsv.txt",sep="\t")


# In[32]:


pd.read_csv(r"https://raw.githubusercontent.com/dsrscientist/DSData/master/bank_additional_data.csv")


# In[ ]:




