
# coding: utf-8

# # Basic Data Types

# 1. Numbers
# 2. String
# 3. List
# 4. Tuple
# 5. Dictionary
# 6. Sets

# In[1]:


# Numbers
# 1. Integers
# 2. Floats
# 3. Complex 
x = 456  # Integer
y = 3.14 #Float
z = 3.14+6j # Complex
print('X = ',type(x),x)
print('Y = ',type(y),y)
print('Z= ',type(z),z)


# In[3]:


x = input("Enter a value : ")
x = int(x)
print("Type of value = ",type(x))
print(x)


# In[4]:


x = 'single quoted string'
y = "double qouted string"
z = """HI 
This is multiline String.
        Define in triple quotes"""
print(x)
print(y)
print(z)


# In[5]:


print("He said,\"Python is Awesome\"")


# In[6]:


print("He said,'Python is Awesome'")


# In[10]:


s = "Python"
k = len(s)
print("Length of Python ",k)
print(s)
print(s[3])
print(s[2])


# In[11]:


s = "Hello World"
print(len(s))
print(s[6:11])


# In[16]:


s = "Python is Interpreted Language"
x = s[10:21]
y = s[:21]
z = s[21:]
p = s[:]
print(s)
print(x)
print(y)
print(z)
print(p)
print(s)


# In[18]:


s = '0123456789'
k = s[::2]
print(k)
l = s[::-1]
print(l)


# In[21]:


s = 'hello world how are you'
print(s[::-1])
print(s[-13:-18:-1])


# In[22]:


x = 'python'
print(dir(x))


# In[23]:


s = "HeLlO WorLd"
k = s.upper()
l = s.lower()
h = s.swapcase()
print(s)
print(k)
print(l)
print(h)


# In[24]:


s = 'PYthon'
doc = s.title.__doc__
print(doc)


# In[26]:


s = "All Dogs are Cat but all Cats are not Dog."
k = s.find('Dog')
print(k)
l = s.replace('Dog','Cat')
print(s)
print(l)


# # LIST

# In[30]:


mylist = [ 5,2,3,56,34,23,46,2] #it can be called array(Homogenous)
mylist1 = [ 'hello',3.14,[1,2,3],12345] #Hetrogenous List
print(*mylist)
print(*mylist1)
k = mylist[3:7]
print(*k)


# In[31]:


l = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(*l[3::3])
print(*l[::-1])
print(*l[::2])
print(*l[-20:-10])
print(*l[-5:-15:-2])


# In[32]:


mylist = [ 1,23,4,123,'hi',45,10,12,66,77,'hello']
print(dir(mylist))


# List Functions 
# 
# Functions that are used to add items into list
# 
# append
# insert
# extend
# 
# Functions that are used delete items from list
# 
# pop
# remove
# 
# Some Common Functions of list
# 
# sort
# revrese
# count
# index
# copy
# clear

# In[34]:


#Functions that are used to add items
#append -> it will add a item at the end of the list use - mylist.append(item)
mylist = [ 1,23,4,23,'hi',45,10,12,66,77,'hello']
print(*mylist)
mylist.append('bye')
print(*mylist)
mylist.append(56)
mylist.append(24)
mylist.append(23)
print(*mylist)


# In[38]:


mylist = [ 1,23,4,23,'hi',45,10,12,66,77,'hello']
print(*mylist)
#1 23 4 23 hi 45 10 12 66 77 hello bye 56 24 23
#insert -> it will take index number and item and add that item to given index
#use = mylist.insert(index,item)
mylist.insert(4,100)
mylist[5] = 23
print(*mylist)
#extend is used to add multiple items


# In[41]:


mylist = [ 1,23,4,23,'hi',45,10,12,66,77,'hello']
mylist.extend('python')
mylist.extend(['hello','world'])
print(mylist)


# In[58]:


mylist = [1, 23,'python', 4, 23, 'hi',23, 45,'hello', 10, 12,23, 66, 77, 'hello', 'p', 'y', 't', 'h', 'o', 'n', 'hello', 'world']
mylist.pop();mylist.pop();mylist.pop()
mylist.pop();mylist.pop();mylist.pop()
mylist.pop();mylist.pop();mylist.pop()
print(mylist)
mylist.pop(2)
print(mylist)
mylist.remove('hi')
mylist.remove('hello')
mylist.remove(23)
print(mylist)
k = mylist.count(23)
mylist.reverse()
print(k)
print(mylist)
mylist1 = mylist.copy()
#mylist1.clear()
mylist1.sort()
print(mylist1)
mylist.sort(reverse=True)
print(mylist)
l = [ 'zello','yellow','hello','challo']
l.sort()
print(l)
l.sort(reverse=True)
print(l)


# In[61]:


l = [ var for var in range(100) ]
print(l)


# # Tuple

# Tuples are immutable data types that can not be changed after it's defination

# In[12]:


mytuple = ('one',2,'three',2,[1,2,3,4],5,3,2,324,)
print(mytuple)
print(dir(mytuple))
print(mytuple[-1::-1])
print("2 is repeted {} times in tuple ".format(mytuple.count(2)))
print("Index of 3 is ",mytuple.index('three'))
print(mytuple[4][3])


# In[13]:


#Example of 2 d list
mylist = [
    ['a[0][0]','a[0][1]','a[0][2]'],
    ['a[1][0]','a[1][1]','a[1][2]'],
    [ 'a[2][0]','a[2][1]','a[2][2]'],
]
    
print(mylist[2])
print(mylist[2][2])


# In[14]:


mylist = [
    [1,2,45,34,234],
    [123,34,6,67,45],
    [23,4,7,78,[23,45,'hello',4]],
]
x = mylist[2][4][2]
print(x)


# # Dictionary

# Dictionaries are collection of key and values.

# In[21]:


mydict = {
    'name' : 'python',
    'scope' : 'World Wide',
    'build_year' : 1994,
    'Frame Works' : ['Django','Flask','Web2py','Pyramid'],
    'Father' : 'Guido Van Rossum',
    'Fields' : ['Scripting','Automation','Cloud','AI','ML','Data Science','Web Desgining','Software Development'],
    }
print(*mydict)
print(dir(mydict))
print(mydict.get('name'))
print(mydict.items())
print(mydict.keys())
print(mydict.values())
print(mydict.update.__doc__)


# In[38]:


mydict = {
    'name' : 'python',
    'scope' : 'World Wide',
    'build_year' : 1994,
    'frame_works' : ['Django','Flask','Web2py','Pyramid'],
    'father' : 'Guido Van Rossum',
    'fields' : ['Scripting','Automation','Cloud','AI','ML','Data Science','Web Desgining','Software Development'],
    }
print("Here Are your keys to select ")
print(*mydict.keys())
mydict['name'] = 'Python Programming Language'
key = input("Enter a key : ").strip().lower()
print("Your key is : {}".format(key))
value = mydict[key]
print(value)
#key = input("Enter a key")
#value = input("Enter a value for your key ")
#mydict[key] = value
mydict[input("Enter New Key : ")] = input("Enter your Value : ")
print(mydict[key],"sucessfully added")
print(mydict)


# # SETS in Python

# In[40]:


s1 = { 1,2,3,4,5 ,1,1,1,1,1,5,5,5,5}
s2 = { 4,5,6,7,8 ,8,8,8,8,8,5,5,5,5,}
print(s1)
print(s2)
print("Type os s1 = ",type(s1))
print(dir(s1))


# In[42]:


s1 = { 1,2,3,4,5 ,1,1,1,1,1,5,5,5,5}
s2 = { 4,5,6,7,8 ,8,8,8,8,8,5,5,5,5,}
print(s1)
print(s2)
#value = s1.intersection(s2)
print("Intersection of s1 and s2 is ",s1.intersection(s2))
#value = s1.union(s2)
print("Unison of s1 and s2 is ",s1.union(s2))
value = s1.difference(s2)
print("Difference of {} with {} is {}.".format(s1,s2,value))



# In[44]:


outer_list = []
inner_list = []

key1 = input("Enter key1 : ")
value1 = input("Enter value1 : ")
inner_list.append(key1)
inner_list.append(value1)
outer_list.append(inner_list)
d = dict(outer_list)
inner_list.clear()
key2 = input("Enter key2 : ")
value2 = input("Enter value2 : ")
inner_list.append(key2)
inner_list.append(value2)
outer_list.append(inner_list)
d.update(outer_list)
print(d)


# In[45]:


d = {
    input("Enter key1 : ") : input("Enter value 1 : "),
    input("Enter key2 : ") : input("Enter value 2 : "),
}
print(d)

