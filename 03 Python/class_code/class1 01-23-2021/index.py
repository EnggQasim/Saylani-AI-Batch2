#!/usr/bin/env python
# coding: utf-8

# In[4]:


mesage = "Hello Python Crash Course reader!"


# In[6]:


type(mesage)


# In[13]:


help(mesage.count)


# In[14]:


get_ipython().run_line_magic('pinfo', 'mesage.count')


# In[ ]:


get_ipython().run_line_magic('pinfo2', 'mesage.count')


# In[ ]:


get_ipython().set_next_input('?mesage.count');get_ipython().run_line_magic('pinfo', 'mesage.count')


# In[15]:


get_ipython().run_line_magic('pinfo', 'mesage.count')


# In[ ]:


get_ipython().run_line_magic('pinfo2', 'mesage.count')


# In[2]:


print(mesage)


# ### Combining or Concatenating Strings

# In[17]:


first_name = "Isfhan"


# In[18]:


last_name = "Ahmed"


# In[22]:


full_name = first_name + " " + last_name
print(full_name)
full_name


# In[32]:


# + - / * % > < != == === is opreator 
'a'+'c'


# In[26]:


name = 'isfhan'
print(name)
name


# In[27]:


name = "isfhan"
print(name)
name


# In[28]:


name = '''isfhan'''
print(name)
name


# In[31]:


detail = """
name :- Isfhan ahmed
fatherName :- Dildar ahmed
"""
print(detail)
detail


# In[33]:


detail = """
Saylani mass IT traing program
Course : Saylani Ai batch-2
name :- Isfhan ahmed
fatherName :- Dildar ahmed
rollNumber : 12546 batch : 2
"""
print(detail)


# In[34]:


name = 'JohnDoe' 
father_name = 'johnCena'
roll_number = 45678

detail = """
Saylani mass IT traing program
Course : Saylani Ai batch-2
Name : {name} 
FatherName : {father_name}
RollNumber : {roll_number} batch : 2
"""
print(detail)


# In[35]:


name = 'JohnDoe' 
father_name = 'johnCena'
roll_number = 45678

detail = f"""
Saylani mass IT traing program
Course : Saylani Ai batch-2
Name : {name} 
FatherName : {father_name}
RollNumber : {roll_number} batch : 2
"""
print(detail)


# In[36]:


name = 'JohnDoe' 
father_name = 'Obama'
roll_number = 45678

detail = f"""
Saylani mass IT traing program
Course : Saylani Ai batch-2
Name : {name} 
FatherName : {father_name}
RollNumber : {roll_number} batch : 2
"""
print(detail)


# In[ ]:




