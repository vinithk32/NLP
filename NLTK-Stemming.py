#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


# In[2]:


ps = PorterStemmer()
words = ["close","closing","closed","closer","closely"]


# In[5]:


for word in words:
    print(ps.stem(word))


# In[ ]:




