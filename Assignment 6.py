#!/usr/bin/env python
# coding: utf-8

# 1. What are escape characters, and how do you use them?

# ans Escape characters are used to do specific task in the programming like for new line to givr space before starting the line or to put quotes "" in the lines .
# some of the escape characters are \n,\t,\". \n stands for new line, \t stands for tab , \" stands for puting the characters in the quotes.

# 2. What do the escape characters n and t stand for?

# ans: n stands for new line and t stands for tab space before the starting character.
# 

# 3. What is the way to include backslash characters in a string?

# In[11]:


print("This is a string with a single backslash: \\.")


# 4. The string "How's Moving Castle" is a correct value. Why isn't the single quote character in the
# word Howl's not escaped a problem?

# ans: the string "How's Moving Castle" is correct value because while using single quote in a word it confuses the programming where to start and end if we use the single quote in the double quote then the program can understand the code otherwise it will show error

# 5. How do you write a string of newlines if you don't want to use the n character?

# In[13]:


print("""we can use the triple code in the string ofr the new line.""")


# 6. What are the values of the given expressions?
# 'Hello, world!'[1]
# 'Hello, world!'[0:5]
# 'Hello, world!'[:5]
# 'Hello, world!'[3:]

# In[14]:


'Hello, world!'[1]


# In[15]:


'Hello, world!'[0:5]


# In[16]:


'Hello, world!'[:5]


# In[17]:


'Hello, world!'[3:]


# 7. What are the values of the following expressions?
# 'Hello'.upper()
# 'Hello'.upper().isupper()
# 'Hello'.upper().islower()
# 

# In[22]:


'Hello'.upper()


# In[23]:


'Hello'.upper().isupper()


# In[24]:


'Hello'.upper().islower()


# 8. What are the values of the following expressions?
# 'Remember, remeber, the fifth of July'.split()
# '-'.join('There can only one'.split())

# In[25]:


'Remember, remeber, the fifth of July'.split()


# In[26]:


'-'.join('There can only one'.split())


# 9. What are the methods for right-justifying, left-justifying, and centering a string?

# In[5]:


s = "Hello, world!"


# In[8]:


s.rjust(20)


# In[9]:


s.ljust(20)


# In[10]:


s.center(20)


# 10. What is the best way to remove whitespace characters from the start or end?
# 

# In[11]:


s = "  Hello, world!"


# In[12]:


s.rstrip()


# In[13]:


s = "Hello, world!     "


# In[14]:


s.lstrip()


# In[ ]:


s.lstript() and s.rstrip() is the best way to rremove the white space from starting or ending

