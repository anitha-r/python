#!/usr/bin/env python
# coding: utf-8

# In[82]:


list1 = [ 2135, 'c', 39, 'Apple',0,39,0.25]
print(list1)


# In[83]:


##wont sort because the list is not homogenous
list1.sort()


# In[84]:


#check if a value is in the list. Returns True or False
print('c' in list1)


# In[85]:


list2= [6,5,4,3,2]
list2.sort()
list2


# In[86]:


#returns the index of the element
#searches the string in the first parameter from index in the 2nd and 3rd parameter and returns the value at the index 
print(list2.index(2))           
print(list2.index(4, 0, 6))


# In[87]:


print(list2*3)


# In[88]:


print(list1.count(39))


# In[89]:


print(min(list2))


# In[90]:


list3=['a','b','c','d']
print(max(list3))


# In[91]:


print(list2[:4])
print(list1[:])


# In[92]:


#to delete an element at the index listed as parameter
print(list3)
list3.pop(0)
print(list3)


# In[93]:


list2.insert(2,44)
print(list2)
#removes the first matching value
list2.remove(44)
list2


# In[67]:


#creating a list using a simple logic
list4 = [x*3 for x in range(10)]
list4


# In[94]:


print(list2 + list3)


# In[95]:


#returns the position that the value occurs in the list
print(list4.index(9))


# In[96]:


#count the occurrence of the parameter value
print(list1.count('8'))


# In[76]:


print(sum(list4))
print(sum(list2 + list3))


# In[ ]:




