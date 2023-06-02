#!/usr/bin/env python
# coding: utf-8

# 1. How do you distinguish between shutil.copy() and shutil.copytree()?

# Ans. shutil.copy() will copy a single file and shutil.copytree() will copy an entire folder and every folder and file contained in it.

# 2. What function is used to rename files??

# Ans.shutil.move will rename files.

# 3. What is the difference between the delete functions in the send2trash and shutil modules?

# Ans. shutil.rmtree() function irreversibly deletes files and folders. send2trash will send folders and files to computer's trash or recycle bin instead of permanently deleting them.

# 4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is
# equivalent to File objects’ open() method?

# Ans. ZipFile method is equivalant to File objects' open() method.

# 5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf
# or .jpg). Copy these files from whatever location they are in to a new folder.

# In[ ]:


Ans. 


# In[4]:


import os, shutil

def selectiveCopy(folder, extensions, destFolder):
    folder = os.path.abspath(folder)
    destFolder = os.path.abspath(destFolder)
    print('Looking in', folder, 'for files with extensions of', ', '.join(extensions))
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension in extensions:
                fileAbsPath = foldername + os.path.sep + filename
                print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)

extensions = ['.php', '.py']
folder = 'randomFolder'
destFolder = 'selectiveFolder'
selectiveCopy(folder, extensions, destFolder)


# In[ ]:




