#!/usr/bin/env python
# coding: utf-8

# 1. What exactly is []?

# ans: It is used to define empty list and it is also used to define list as in l= [1,2,3].

# 2. In a list of values stored in a variable called spam, how would you assign the value "hello" as the
# third value? (Assume [2, 4, 6, 8, 10] are in spam.)

# ans:

# In[2]:


spam=[2,4,6,8,10]


# In[4]:


spam[2]


# In[5]:


spam[2]= "hello"


# In[6]:


spam


# 3. What is the value of spam[int(int('3' * 2) / 11)]?

# In[7]:


spam=['a','b','c','d']


# In[8]:


spam[int(int('3'*2)/11)]


# the value of spam = 'd'

# 4. What is the value of spam[-1]?

#  ans:

# In[11]:


spam[-1]


# 5. What is the value of spam[:2]?

# ans:
# 

# In[12]:


spam[:2]


# 6. What is the value of bacon.index("cat")?

# ans:
# 

# In[13]:


bacon=[3.14,'cat',11,'cat',True]


# In[14]:


bacon.index('cat')


# the value of bacon.index('cat') is 1

# 7. How does bacon.append(99) change the look of the list value in bacon?

# In[15]:


bacon.append(99)


# In[16]:


bacon


# bacon.append(99) will add the integer 99 in the bacon list at the end of the list.

# 8. How does bacon.remove('cat') change the look of the list in bacon?

# In[17]:


bacon.remove('cat')


# In[18]:


bacon


# the bacon.remove('cat') will remove the first occuring string cat from the list.

# 9. What are the list concatenation and list replication operators?

# ans: The list concatenation operator is +, and the list replication operator is *. List concatenation is used to join the lists to form a new list and list replication is used to repeat a list for the given number to form new list  

# In[19]:


list1 = [1, 2, 3]
list2 = [4, 5, 6]    
list3 = list1 + list2


# In[20]:


list3


# In[21]:


list4=[1, 2, 3]
list5= list4*2


# In[22]:


list5


# 10. What is difference between the list methods append() and insert()?

# In[23]:


list1


# In[25]:


list1.insert(3,4)


# In[26]:


list1


# The difference between append() and insert() is that isert will help to insert a value at desired index in the list where as append only allows to add the value at the end of the list.

# 11. What are the two methods for removing items from a list?

# ans: the two methods are list.remove() and del list[]

# 12. Describe how list values and string values are identical.

# ans: Both string and list have length of characters an items in them. they can be index, sliced , concatenated.
# looping fucntion can be used in both of them.

# 13. What's the difference between tuples and lists?

# ans:list is mutable and tuple is immutable. their syntax is different for list "[]" is  used and for tuple "()" is used. The list has many built in function where as tuple does not have many built in function because it is immutable.

# 14. How do you type a tuple value that only contains the integer 42?

# In[32]:


t=(42,)


# In[33]:


t


# In[34]:


type(t)


# 15. How do you get a list values tuple form? How do you get a tuple values list form?

# In[22]:


l1=[1,2,3,4,5]


# In[23]:


mylist=tuple(l1)


# In[24]:


mylist


# In[1]:


t=(4,5,6,7)


# In[3]:


t2=list(t)


# In[4]:


t2


# 16. Variables that contain list values are not necessarily lists themselves. Instead, what do they
# contain?

# variables that contains list values are type of variable where the values is stored as a form of list eg. l=[1,2,34] the values are list but not the variable it is used to store the values.

# 17. How do you distinguish between copy.copy() and copy.deepcopy()?

# copy.copy() copies the original value but if the values is changed in the copied then original values will also change and copy.deepcopy() copies the original values and stores into new variable so that if values are changed original values are not affected my it
