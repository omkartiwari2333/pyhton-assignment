#!/usr/bin/env python
# coding: utf-8

# 1. What does an empty dictionary's code look like?

# ans:

# In[2]:


d= {}


# In[3]:


type(d)


# 2. What is the value of a dictionary value with the key "foo" and the value 42?

# In[4]:


d={"foo":42}


# In[7]:


d.values()


# the value of key foo is 42.

# 3. What is the most significant distinction between a dictionary and a list?

# ans: firstly the list is indicated by "[]" and dicitonary is incidated by "{}", dicitonary are in key and values pair and list are in ordered list they are not in pair .

# 4. What happens if you try to access spam["foo"] if spam is {"bar": 100}?

# In[9]:


spam={"bar": 100}


# In[10]:


spam['foo']


# 5. If a dictionary is stored in spam, what is the difference between the expressions "cat" in spam and
# "cat" in spam.keys()?

# In[21]:


spam={"cat":"pet"}


# In[22]:


spam["cat"]


# In[23]:


spam.keys()


# the expression spam['cat'] will check in dictionary whether the key 'cat' is available in the dictionary and then if it is true then it will give the vlaue of the key cat, and on the expression spam.keys() this funciton will give the key in the dictionary  as in ouput but in the form of list.

# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and
# 'cat' in spam.values()?

# In[32]:


spam={"cat":"pet"}


# In[33]:


spam['cat']


# In[34]:


spam.values()


# the expression spam['cat'] will check in the dictionary whether the key cat is present or not if yess then it will give out the value of cat and the expression spam.values('cat') give the values of the key cat inthe form of list.

# 7. What is a shortcut for the following code?
# if 'color' not in spam:
# spam['color'] = 'black'

# In[37]:


spam.setdefault('color','black')


# 8. How do you 'pretty print' dictionary values using which module and function?

# In[38]:


from pprint import pprint

spam = {'color': 'black', 'age': 42}
pprint(spam)


# In[ ]:




