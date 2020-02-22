#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("vinith")


# In[2]:


import nltk  #importing nltk


# In[ ]:


#nltk.download() # Download all packages required for natural language processing


# In[ ]:


from nltk import word_tokenize


# In[ ]:


text = "hi vinith how are you? how is your work going. what about your family."
word_tokenize(text)


# In[8]:


print(word_tokenize(text))


# In[10]:


print(text)


# In[13]:


from nltk import sent_tokenize
print(sent_tokenize(text))


# In[ ]:




