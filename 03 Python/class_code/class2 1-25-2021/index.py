#!/usr/bin/env python
# coding: utf-8

# In[1]:


mesage = "Hello Python Crash Course reader!"


# In[2]:


type(mesage)


# In[3]:


help(mesage.count)


# In[4]:


get_ipython().run_line_magic('pinfo', 'mesage.count')


# In[5]:


get_ipython().run_line_magic('pinfo2', 'mesage.count')


# In[6]:


get_ipython().set_next_input('?mesage.count');get_ipython().run_line_magic('pinfo', 'mesage.count')


# In[ ]:


get_ipython().run_line_magic('pinfo', 'mesage.count')


# In[7]:


get_ipython().run_line_magic('pinfo', 'mesage.count')


# In[8]:


get_ipython().run_line_magic('pinfo2', 'mesage.count')


# In[9]:


print(mesage)


# ### Combining or Concatenating Strings

# In[10]:


first_name = "Isfhan"


# In[11]:


last_name = "Ahmed"


# In[12]:


full_name = first_name + " " + last_name
print(full_name)
full_name


# In[13]:


# + - / * % > < != == === is opreator 
'a'+'c'


# In[14]:


name = 'isfhan'
print(name)
name


# In[15]:


name = "isfhan"
print(name)
name


# In[16]:


name = '''isfhan'''
print(name)
name


# In[17]:


detail = """
name :- Isfhan ahmed
fatherName :- Dildar ahmed
"""
print(detail)
detail


# In[18]:


detail = """
Saylani mass IT traing program
Course : Saylani Ai batch-2
name :- Isfhan ahmed
fatherName :- Dildar ahmed
rollNumber : 12546 batch : 2
"""
print(detail)


# In[19]:


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


# In[20]:


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


# In[21]:


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


# In[22]:


name


# In[25]:


name = name.upper()


# In[26]:


name


# In[30]:


get_ipython().system('ls -la')


# In[31]:


get_ipython().system('pwd')


# In[34]:


game = "Gta     "


# In[35]:


print(game)


# In[37]:


game.rstrip()


# In[38]:


movie = "bac k to future "


# In[39]:


number_with_power = 3 ** 3


# In[40]:


number_with_power


# In[42]:


(2 + 3) ** 4


# In[43]:


float_number = 4.56


# In[44]:


type(float_number)


# In[46]:


float_number_one = 4.36 


# In[47]:


float_number_two = 8.36


# In[50]:


answer = float_number_one float_number_two


# In[51]:


answer


# ### Arithmetic operators

# ##### + , - ,  / ,  * ,  %  ,  // , ** is opreator 

# In[53]:


2+5


# In[54]:


'1'+'1'


# In[55]:


55 + 96.6


# In[56]:


'1'+1


# In[57]:


int('1')+1


# In[59]:


'string '*5


# In[62]:


22/7


# In[63]:


a=2


# In[64]:


b=2


# In[65]:


id(a)


# In[66]:


id(b)


# In[67]:


a is b


# In[ ]:





# In[ ]:




