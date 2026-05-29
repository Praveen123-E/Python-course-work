Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=10.22
b
10.22
int(b)
10
complex(b)
(10.22+0j)
str(b)
'10.22'
list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True

c=10+4j
c
(10+4j)
int(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(10+4j)'
bool(c)
True
list,tuple,set, dict are not possible
SyntaxError: invalid syntax
s="python"
a="12323"
b="2323.232"
s
'python'
a
'12323'
b
'2323.232'

int(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
float(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
list(s)
['p', 'y', 't', 'h', 'o', 'n']
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
set(s)
{'p', 'y', 'n', 't', 'o', 'h'}
complex,dict are not possible
SyntaxError: invalid syntax
bool(s)
True

a
'12323'

int(a)
12323
float(a)
12323.0
complex(a)
(12323+0j)
list(a)
['1', '2', '3', '2', '3']
tuple(a)
('1', '2', '3', '2', '3')
set(a)
{'1', '2', '3'}
dict(a)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(a)
True

b
'2323.232'

int(b)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '2323.232'
float(b)
2323.232
complex(b)
(2323.232+0j)
list(b)
['2', '3', '2', '3', '.', '2', '3', '2']
tuple(b)
('2', '3', '2', '3', '.', '2', '3', '2')
set(b)
{'2', '.', '3'}
dict(b)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    dict(b)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(b)
True

l=[1,2,3,2,4,5,6,8]
l
[1, 2, 3, 2, 4, 5, 6, 8]
int,float,complex are not possible
SyntaxError: invalid syntax
str(l)
'[1, 2, 3, 2, 4, 5, 6, 8]'
tuple(l)
(1, 2, 3, 2, 4, 5, 6, 8)
>>> set(l)
{1, 2, 3, 4, 5, 6, 8}
>>> dict(l)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(l)
True
>>> 
>>> t=(1,2,3,43,2,3,6)
>>> t
(1, 2, 3, 43, 2, 3, 6)
>>> int,float,complex,dict are not possible
SyntaxError: invalid syntax
>>> str(t)
'(1, 2, 3, 43, 2, 3, 6)'
>>> list(t)
[1, 2, 3, 43, 2, 3, 6]
>>> set(t)
{1, 2, 3, 6, 43}
>>> bool(t)
True
>>> s={1,2,3,2,4,5,4}
>>> s
{1, 2, 3, 4, 5}
>>> int,float,complex,dict are not possible to convert
SyntaxError: invalid syntax
>>> 
>>> str(s)
'{1, 2, 3, 4, 5}'
>>> list(s)
[1, 2, 3, 4, 5]
>>> tuple(s)
(1, 2, 3, 4, 5)
>>> bool(s)
True
>>> 
>>> d={1:2,2:4,3:6}
