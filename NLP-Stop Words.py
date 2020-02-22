#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[2]:


stop_words = set(stopwords.words("english"))


# In[3]:


print(stop_words)


# In[10]:


example_sentence = "This is an example showing of stop word filteration with the help of nltk.corpus"


# In[11]:


words = word_tokenize(example_sentence)


# In[12]:


print(words)


# In[13]:


filtered_words = []


# In[14]:


for word in words:
    if word not in stop_words:
        filtered_words.append(word)


# In[15]:


print(filtered_words)


# In[16]:


filtered_words = [word for word in words if not word in stop_words]
print(filtered_words)


# In[ ]:




