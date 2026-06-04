Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1,2,3,4)
t
(1, 2, 3, 4)
t=(1,1,1,1,1,11)
t
(1, 1, 1, 1, 1, 11)
t=(1,1.2,33,3.44,"praaveen",[])
t
(1, 1.2, 33, 3.44, 'praaveen', [])
#operation of tuple
#1.concatination
t=(1,2,3,4)
h=(5,6,7,8)
t+h
(1, 2, 3, 4, 5, 6, 7, 8)
#repetition
t*2
(1, 2, 3, 4, 1, 2, 3, 4)
t*5
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
#indexing
t=(10,20,30,40,50,60)
t
(10, 20, 30, 40, 50, 60)
t[0]
10
t[5]
60
t[-1]
60
t[-4]
30
#slicing
t
(10, 20, 30, 40, 50, 60)
t[::-1]
(60, 50, 40, 30, 20, 10)
t[0:4]
(10, 20, 30, 40)
t[:5]
(10, 20, 30, 40, 50)
t[3:]
(40, 50, 60)
t[2:6:2]
(30, 50)
#membership

20 in t
True
40 in t
True
50 not in t
False
70 in t
False
80 not in t
True

t
(10, 20, 30, 40, 50, 60)
>>> sorted(t)
[10, 20, 30, 40, 50, 60]
>>> min(t)
10
>>> max(t)
60
>>> t.count()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    t.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> sum(t)
210
>>> t.count(20)
1
>>> t.index(40)
3
>>> #packing and unpacking
>>> t=1,2,3,4,5,6
>>> t
(1, 2, 3, 4, 5, 6)
>>> a=1,2,3
>>> x,y,z=a
>>> x
1
>>> y
2
>>> z
3
>>> t=(1,2,3,[4,5,6],7,8)
>>> t
(1, 2, 3, [4, 5, 6], 7, 8)
>>> t[2]
3
>>> t[3]
[4, 5, 6]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
>>> # here tuple is immutable ,but if any element inside the tuple is mutable we can modify that datatype
>>> t[2]=4
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
