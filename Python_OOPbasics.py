#!/usr/bin/env python
# coding: utf-8

# Different ways of slicing lists

# In[5]:


List1 = [12,14,23,67,90,7]
#print the list
print(List1[::])


# In[9]:


#use the list index , in this case, index values range from 0 to 5 or -1 to 
#print a slice of the list starting with element at index 2 and all the elements excluding index 5
print(List1[2:5])
#print a slice of the list starting with element at index 2 and all the elements excluding index -2
print(List1[2:-2])
#print a slice of the list at index -6
print(List1[-6])
print(List1[-1])
#print type of object
type(List1[0:1])


# In[47]:


#print every element in the list
print("entire list:" , List1[::])
#print a slice of the list in reverse
#starting with the element at index 2 and every second element in the reverse direction
print(List1[2::-2])
#the optional values are start, stop and step for traversing the list
#default values for start is 0. for stop is length of the list. for step is 1.
#a negative step means list is traversed in the reverse direction
print(List1[1:7:2])
print(List1[:-9:-2])
#returns an object of type list
type(List1[2::-2])


# In[ ]:




