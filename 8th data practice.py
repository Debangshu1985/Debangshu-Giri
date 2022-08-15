#!/usr/bin/env python
# coding: utf-8

# In[3]:


y=78
s=13
t=5
f=6
print(y/s+t*f)
type(y/s+t*f)


# In[4]:


y=78
x=97
h=75
e=y-x+h
print(e)
type(e)


# In[5]:


y=78
x=97
h=75
i=y/x*h
print(i)
type(i)


# In[6]:


y=85
e=12
w=y*e
print(w)
type(w)


# In[8]:


y=85
e=12
r=y-e
print(r)
type(r)


# In[7]:


#devide only make float


# In[ ]:


#others three symbol makes integer


# In[9]:


import os


# In[10]:


os.getcwd()


# In[11]:


import pandas as pd


# In[13]:


pd.read_excel(r"C:\Users\user\OneDrive\Desktop\time.xlsx")


# In[14]:


pd.read_excel(r"C:\Users\user\OneDrive\Desktop\time.xlsx")


# In[15]:


pd.read_excel("time.xlsx")


# In[16]:


pd.read_csv(r"C:\Users\user\Desktop\expense.csv")


# In[20]:


pd.read_csv("expense.csv")


# In[21]:


pd.read_csv(r"C:\Users\user\Desktop\expense.tsv")


# In[23]:


pd.read_csv("expense.tsv",sep="\t")


# In[25]:


pd.read_csv("expense.tsv",sep="\t")


# In[26]:


#if excel file convert or copy to note file its may take csv but error come to while code putted sep="\t" example 28 cell


# In[27]:


pd.read_csv("expense.csv")


# In[28]:


pd.read_csv("expense.csv",sep="\t")


# In[29]:


pd.read_csv("https://raw.githubusercontent.com/dsrscientist/dataset1/master/bikes.csv")


# In[30]:


pd.read_csv("bikes.csv")


# In[31]:


pd.read_csv(r"C:\Users\user\bikes.csv")


# In[38]:


pd.read_csv(r"C:\Users\user\file.tsv.txt")


# In[39]:


pd.read_csv("file.tsv.txt")


# In[40]:


pd.read_csv("file.tsv.txt",sep="\t")


# In[ ]:




