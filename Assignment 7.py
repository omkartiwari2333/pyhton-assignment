#!/usr/bin/env python
# coding: utf-8

# 1. What is the name of the feature responsible for generating Regex objects?

# Ans. The re.compile() function is responsible for generating Regex objects.

# 2. Why do raw strings often appear in Regex objects?

# Ans. Raw strings are used in Regex objects to avoid excessive escaping of special characters. By using a raw string you can write the pattern more clearly without extra escaping.

# 3. What is the return value of the search() method?

# Ans. Returns a match object if there is a match found in the string, otherwise it returns none.

# 4. From a Match item, how do you get the actual strings that match the pattern?

# Ans. By using group() method we can get the actual strings that match the pattern.

# 5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover?
# Group 2? Group 1?

# Ans. The group 0 covers the entire matched string. Group1 covers the first three digits before the hypen. Group2 covers the remaining seven digits after the hypen.

# 6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell
# a regex that you want it to fit real parentheses and periods?

# Ans. We can use back slash to escape the period and parentheses

# 7. The findall() method returns a string list or a list of string tuples. What causes it to return one of
# the two options?

# Ans. It depends on the pattern. If the pattern has no capturing groups  the findall() function returns a list of strings that match the whole pattern and if the pattern has one capturing group the findall() function returns a list of strings tuples.

# 8. In standard expressions, what does the | character mean?

# Ans. The expressions is known as "pipe" or "vertical bar" and is used as operator used to specify alternative patterns, the expression allows us to define multiple alternative patterns.

# 9. In regular expressions, what does the character stand for?

# Ans. All character execpt those having special meaning in regex.

# 10.In regular expressions, what is the difference between the + and * characters?

# Ans. The "+" matches one or more occurrences of the preceding element while the "*" matches zero or more occurrences of the preceding element in regular expression.

# 11. What is the difference between {4} and {4,5} in regular expression?

# Ans. {4} specifies that preceding element must occur exactly 4 times and {4,5} specifies that the preceding element myst occur at least 4 or atmost 5 times.

# 12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular
# expressions?

# Ans. \d represents any digit character(0-9).
#  \w represents any word character (alphabets, numeric or underscore).
#  \s represents any white space character.

# 13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?

# Ans. \D it represents any non digit character.
# \W represents any non word character.
# \S  represents any non white space character.

# 14. What is the difference between .*? and .*?

# Ans. .*? matches minimal as few characters possible and .* matches maximum  as many characters possible.

# 15. What is the syntax for matching both numbers and lowercase letters with a character class?

# Ans. Syntax for matching both numbers and lowercase letters with charcter class is [0-9a-z].

# 16. What is the procedure for making a normal expression in regex case insensitive?

# Ans. To make a normal expression case sensitive in regex add the flag i after closing the delimiter of the regex pattern.

# 17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd
# argument in re.compile()?

# Ans. The . character normally matches any character except newline and if re.DOTALL is passed as 2nd the dot character matches any character including newline.

# 18. If numReg = re.compile(r'\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4
# hen') return?

# In[3]:


import re

numReg = re.compile(r'\d+')
result = numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')
print(result)


# ans.it will return :'X drummers, X pipers, five rings, X hen'

# 19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?

# Ans. Passing re.VERBOSE as the second argument to re.compile() allow us  to add comments and whitespace within regex pattern for improved readability.

# In[ ]:


20. How would you write a regex that match a number with comma for every three digits? It must
match the given following:
'42'
'1,234'
'6,368,745'


# In[4]:


import re

pattern = r'^\d{1,3}(,\d{3})*$'
numbers = ['42', '1,234', '6,368,745']

for number in numbers:
    if re.match(pattern, number):
        print(f"Match: {number}")
    else:
        print(f"No match: {number}")


# In[ ]:




