#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


# In[3]:


train_set = state_union.raw("2005-GWBush.txt")


# In[4]:


print(train_set)


# In[6]:


test_set = state_union.raw("2006-GWBush.txt")


# In[8]:


tokenizer = PunktSentenceTokenizer(train_set) #train the tokenizer


# In[9]:


words = tokenizer.tokenize(test_set) # using trained tokenizer tagging the words with grammer


# In[11]:


tags = []

for word in words:
    out = nltk.word_tokenize(word)
    tags.append(nltk.pos_tag(out))


# In[12]:


print(tags)


# In[ ]:




