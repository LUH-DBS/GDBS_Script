#!/usr/bin/env python
# coding: utf-8

# # sql test

# In[1]:


get_ipython().system('pip install sqlalchemy==1.3.9')
get_ipython().system('pip install ipython-sql')


# In[2]:


import sys
sys.executable


# In[3]:


get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:///imdb.db')


# In[4]:


get_ipython().run_line_magic('sql', "SELECT name FROM actor WHERE name LIKE '%Krug%'")

