#!/usr/bin/env python
# coding: utf-8

# In[10]:


#reference:https://www.geeksforgeeks.org/python-normal-distribution-in-statistics/

from scipy.stats import norm
#A normal continuous random variable.#
a, b = 2.5, 7.5
c = norm(a, b)

print (c)


# In[60]:


import numpy as np
quantile = np.arange (0.01, 2, 0.1)

# Random Variates
R = norm.rvs(a, b)
print ("Random Variates : \n", R)

# PDF
R = norm.pdf(a, b, quantile)
print ("\nProbability Distribution : \n", R)


# In[47]:


import numpy as np
import matplotlib.pyplot as plt
	
distribution = np.linspace(0, np.minimum(c.dist.b, 10))
print("Distribution : \n", distribution)
	
plot = plt.plot(distribution, c.pdf(distribution))


# In[59]:


import matplotlib.pyplot as plt
import numpy as np
	
x = np.linspace(-10, 3, 150)
	
# Varying positional arguments
y1 = norm.pdf(x, 1, 3)
y2 = norm.pdf(x, 6, 2)
plt.plot(x, y1, "c1", x, y2, "r--")


# In[ ]:




