#!/usr/bin/env python
# coding: utf-8

# 1.What are the two values of the Boolean data type? How do you write them

# ans. the two values of boolean data type are true and false. 

# In[4]:


a = True 


# In[6]:


a


# In[7]:


type(a)


# 2. What are the three different types of Boolean operators?

# ans. the three types of boolean operators are :
#     1. and
#     2. or 
#     3.not

# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
# values for the operator and what it evaluate ).

# ans.Truth Table for AND
# A B output
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1
# Truth Table for OR
# A B output
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1
# Truth Table for NOT
# A output
# 0 1
# 1 0

# 4. What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5>4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)

# In[10]:


(5>4) and (3==5)


# In[16]:


not(5>4)


# In[12]:


(5>4) or (3==5)


# In[13]:


not ((5>4) or (3==5))


# In[14]:


(True and True) and (True == False)


# In[15]:


(not False) or (not True)


# 5. What are the six comparison operators?

# ans. ==, !=, <, >, <=, and >=

# 6. How do you tell the difference between the equal to and assignment operators?Describe a
# condition and when you would use one.

# ans. the equal to operator is used to compare the two values and assignment operator is used to assign an value to the variable ex: 5==5 and a= 5  

# 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('ham')
# print('ham')
# 
# 

# In[20]:


spam = 0
if spam == 10:
    print('eggs')  #first block
if spam > 5:
    print('bacon')# second block
else:
    print('ham')
    print('ham')
    print('ham')# thrid block
    


# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.

# In[27]:


spam = int(input("Enter a number: "))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings")


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')


# In[ ]:


ans. one must press Ctrl + c 


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')


# ans.break means it will stop the execution after meeting its require meant in the code written by the user and in continue it will keep on going till the condition is met after the condition is being met it will again go to the start of the loop.

# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# In[28]:


for i in range(10):
    print(i)


# In[29]:


for i in range(0,10):
    print(i)


# In[33]:


for i in range(0,10,1):
    print(i)


# for loop in range(10): it will print the numbers till 0 to 9 according to the index of 10
#     in(0,10): it will also print the same thing but user can set the upper bound according to its requirement
#         and in (0,10,1) it will do addition till index number 10 for example. 0+1=1 and soo

# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
# program that prints the numbers 1 to 10 using a while loop.

# In[35]:


for i in range(0,11):
    print(i)


# In[1]:


a = 1
while (a<=10):
    print(a)
    a+=1


# 13. If you had a function named bacon() inside a module named spam, how would you call it after
# importing spam?

# In[ ]:


spam.bacon()

