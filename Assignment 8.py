#!/usr/bin/env python
# coding: utf-8

# 1. Is the Python Standard Library included with PyInputPlus?

# Ans. PyInputPlus is a Python module used for taking inputs with additional validation features. PyInputPlus will keep asking the user for text until they enter valid input.

# 2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?

# Ans. The 'as pypi' code in the import statement saves us from typing pyinputplus each time we want to call a PyInputPlus function.

# 3. How do you distinguish between inputInt() and inputFloat()?

# Ans. "inputInt()" : Accepts an integer value. This also takes additional parameters ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’ for bounds. Returns an int. "inputFloat()" : Accepts a floating-point numeric value. Also takes additional ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’ parameters. Returns a float.

# 4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

# Ans.

# In[1]:


pip install PyInputPlus


# In[2]:



import pyinputplus as pypi

num = pypi.inputInt("Enter a number between 0 and 99: ", min=0, max=99)
print("You entered:", num)


# 5. What is transferred to the keyword arguments allowRegexes and blockRegexes?

# Ans. Allowregexes specifies the pattern that are allowed for input and pyinputplus will only accept values that match at least one of the regular expression and blockregexes specifies the pattern that are blocked for input, pyinputplus will reject the input values that match any of the regular expressions.

# 6. If a blank input is entered three times, what does inputStr(limit=3) do?

# In[ ]:


Ans. It will raise RetryLimitException.


# In[3]:


import pyinputplus as pypi

try:
    value = pypi.inputStr("Enter a value (limit=3): ", limit=3)
    print("You entered:", value)
except pypi.RetryLimitException:
    print("Maximum number of retries reached.")


# 7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?

# Ans. If blank input is entered three times, then the inputStr(limit=3, default='hello') will return the default vlaue as hello.

# In[4]:


value = pypi.inputStr("Enter a value (limit=3, default='hello'): ", limit=3, default='hello')
print("You entered:", value)


# In[ ]:




