Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
a=10.3
type(a)
<class 'float'>
s=9+6j
type(s)
<class 'complex'>
p='python'
type(p)
<class 'str'>
p="java"
type(p)
<class 'str'>
l=[1,2,3,4]
l.append(5)
l.append(6)
l
[1, 2, 3, 4, 5, 6]
type(l)
<class 'list'>
tuple
<class 'tuple'>
c=(1,2,3,4,33,3,3,5)
c
(1, 2, 3, 4, 33, 3, 3, 5)
type(c)
<class 'tuple'>
c=("p",1,2.3,2+8j0
   
SyntaxError: invalid imaginary literal
c=("p",1,2.3,2+8j)
   
c
   
('p', 1, 2.3, (2+8j))
type(c)
   
<class 'tuple'>
id(c)
   
1814498388032
c.append(44)
   
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    c.append(44)
AttributeError: 'tuple' object has no attribute 'append'
c
   
('p', 1, 2.3, (2+8j))
boolen
   
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    boolen
NameError: name 'boolen' is not defined. Did you mean: 'bool'?
e=True
   
e=False
   
type(e)
   
<class 'bool'>
a=none
   
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a=none
NameError: name 'none' is not defined. Did you mean: 'None'?
a=None
   
type(a)
   
<class 'NoneType'>
<class 'NoneType'>
   
SyntaxError: invalid syntax



list=[1,2,3,"pravee"]
   
list
   
[1, 2, 3, 'pravee']
list.remove(3)
   
list
   
[1, 2, 'pravee']
list.remove("pravee")
   
list
   
[1, 2]
list.append("praveen")
   
list.append(2,3,4)
   
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    list.append(2,3,4)
TypeError: list.append() takes exactly one argument (3 given)
>>> list.append(22)
...    
>>> l
...    
[1, 2, 3, 4, 5, 6]
>>> set
...    
<class 'set'>
>>> s={1,2,3,3,3,4,2,2,1,1}
...    
>>> s
...    
{1, 2, 3, 4}
>>> type(s)
...    
<class 'set'>
>>> dict
...    
<class 'dict'>
>>> d={"name";"praveen,'age':22,"course":'PFS'}
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> d={"name";"praveen,'age':22,"course":"PFS"}
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> d={"name";"praveen",'age':22,"course":'PFS'}
...    
SyntaxError: invalid syntax
>>> d={"name";"praveen,"age":22,"course":"PFS"}
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> d={"name":"praveen,'age':22,"course":'PFS'}
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> d={"name":"praveen,'age':22,'course':'PFS'}SyntaxError: unterminated string literal (detected at line 1)
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> d={"name":"praveen",'age':22,'course':'PFS'}
...    
>>> type(d)
...    
<class 'dict'>
