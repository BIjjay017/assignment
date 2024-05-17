#!/usr/bin/env python
# coding: utf-8

# In[2]:


movies=['Avatar','Avengers','Maze Runner']
movies[2]


# In[3]:


movies.append('Incantation')
movies


# In[4]:


integers=[1,2,3,4,5,6,7,8,9,10]
integers


# In[10]:


sum=0
for i in range(0,len(integers)):
    sum=sum+integers[i]
sum


# In[11]:


mixed=[1,2.2,'a','Apple']
mixed


# In[16]:


mixed.pop(0)
mixed


# In[21]:


week=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
week


# In[19]:


week[2]


# In[22]:


colors=('red','blue','green','black','white')
colors


# In[27]:


check='purple'
if check in colors:
    colors
else:
    print(check +" not in above tuple")


# In[7]:


book={'Title':'Poverty','Authors':'Desmond','Year':2015}
book
book['Year']=2017
book


# In[1]:


fruit_color={"Apple":"red",'banana':'yellow','watermelon':'red'}
fruit_color


# In[4]:


fruit_color["Grape"]='green'
fruit_color


# In[5]:


city_pop={'kathmandu':125000,'kaski':25000,'bhaktapur':45000,'lalitpur':95000}
city_pop


# In[9]:


city_removed='kaski';
if city_removed in city_pop:
    del city_pop[city_removed]
city_pop


# In[ ]:




