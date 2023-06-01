#!/usr/bin/env python
# coding: utf-8

# # ARRAY

# In[1]:


import numpy as np


# In[2]:


num=np.array([1,2,3,4,5])


# In[3]:


num


# In[4]:


print(num)


# In[5]:


num[3]


# In[6]:


num.dtype


# In[7]:


num.shape


# In[8]:


num=np.array([12.3,32.5])
num


# In[9]:


print(num)


# In[10]:


num.dtype


# In[11]:


num=np.array([20,93,"hiii",56])


# In[12]:


num


# In[13]:


print(num)


# In[14]:


num.dtype


# In[15]:


chr(70)


# In[16]:


ord('D')


# In[17]:


greet=['heelo','welcome']
greet
print(greet)


# In[18]:


greet[1]*10


# In[19]:


num = np.array([23, 34, 55, 78])
x = [23, 34, 55, 78]


# In[20]:


x*2


# In[21]:


num*2


# In[22]:


num>90


# In[23]:


65 in num


# In[24]:


np.empty(2)


# In[25]:


list(range(20,2,-2))


# In[26]:


list


# In[27]:


np.arange(1,10,0.25)


# In[28]:


num.mean()


# In[29]:


num.argmax()


# In[30]:


num.sort()


# In[31]:


num


# In[32]:


np.linspace(1,4,6)


# # Multidimentional Array

# In[33]:


x=np.array([[1,2,6],[3,4,7],[8,7,9]])
x


# In[34]:


print(x)


# In[35]:


x.shape


# In[36]:


x.size


# In[37]:


x[1][1]


# In[38]:


x.reshape(3,3)


# In[39]:


x.reshape(3,-1)


# In[40]:


x.flatten()


# # Series operation on Pandas

# In[41]:


import pandas as pd


# In[42]:


s=pd.Series([12,13,14,51])


# In[43]:


s


# In[44]:


type(s)


# In[45]:


s.size


# In[46]:


s=pd.Series([23,34,67,94],index=range(100,104))


# In[47]:


s


# # dataframe

# In[48]:


x = pd.Series([1,2,3])
y = pd.Series(['Robin','Barney','Ted'])
z = pd.Series([89,54,78])


# In[49]:


df = pd.DataFrame(
{
    'Roll_no' : x,
    'Name' : y,
    'Marks' : z,
    
})


# In[50]:


df


# In[51]:


df.columns #column names


# In[52]:


import pandas as pd
import numpy as np


# In[53]:


x=np.array([1,2,3,4,4,5,6])


# In[54]:


np.mean(x)


# In[55]:


np.median(x)


# In[ ]:




