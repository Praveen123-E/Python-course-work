Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set is collection of unique elements
# and unorder and mutable and it is heteroginous
s={23,54,6765,76,87,55,66,342}
s
{66, 76, 6765, 23, 54, 55, 342, 87}
s=set()
s
set()
s={1,1,1,1,1}
s
{1}
s={2,3,2,2,34,555,33,66,87}
s
{33, 2, 3, 34, 66, 87, 555}
s=set()
s
set()
s.add(1)
s.add(203.43)
s.add('praveen')
s.add([23,3,2])
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.add([23,3,2])
TypeError: unhashable type: 'list'
s.add((1,2,32,))
s.add({2,3,4})
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.add({2,3,4})
TypeError: unhashable type: 'set'
s.add({'name':'praveen'})
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.add({'name':'praveen'})
TypeError: unhashable type: 'dict'
s
{'praveen', 1, 203.43, (1, 2, 32)}
s.add(231)
s
{1, 'praveen', 231, 203.43, (1, 2, 32)}
#operation on set
#only membership operation is there
2 in s
False
1 in s
True
21 not in s
True
# in set there no concatination,repetition ,indexing,slicing
{1,2}+{2,3}
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    {1,2}+{2,3}
TypeError: unsupported operand type(s) for +: 'set' and 'set'
{1,2}*2
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    {1,2}*2
TypeError: unsupported operand type(s) for *: 'set' and 'int'
s
{1, 'praveen', 231, 203.43, (1, 2, 32)}
s[2]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
s[::-1]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s[::-1]
TypeError: 'set' object is not subscriptable
1 in s
True

operation in set
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    operation in set
NameError: name 'operation' is not defined. Did you mean: 'StopIteration'?
#operation in set
#1.union
a={1,2,3,2,4,5}
b={7,8,9}
a.union(b)
{1, 2, 3, 4, 5, 7, 8, 9}
a|b
{1, 2, 3, 4, 5, 7, 8, 9}
a.intersection(b)
set()
a.add(7)
a.intersection(b)
{7}
a&b
{7}
a-b
{1, 2, 3, 4, 5}
a^b
{1, 2, 3, 4, 5, 8, 9}
a
{1, 2, 3, 4, 5, 7}
#{1}{2}{3}{4}{1,2}{3,4}
a>={1}
True
a<={1,2,3,4,5,6,7,8}
True
a>={1,2}
True
a
{1, 2, 3, 4, 5, 7}
b
{8, 9, 7}
a.isdisjoint(b)
False
a.isdisjoint({90,80})
True
a.add(20)
a
{1, 2, 3, 4, 5, 20, 7}
a.update({11,12,13})
a
{1, 2, 3, 4, 5, 7, 11, 12, 13, 20}
a.pop()
1
a.pop()
2
a.remove(4)
a
{3, 5, 7, 11, 12, 13, 20}
a.remove(11)
a
{3, 5, 7, 12, 13, 20}
a.discard(6)
a
{3, 5, 7, 12, 13, 20}
a.discard(3)
>>> a
{5, 7, 12, 13, 20}
>>> a.clear()
>>> a
set()
>>> a
set()
>>> a={1,2,3,4,5,6}
>>> b={2,3,7,8}
>>> a.intersection(b)
{2, 3}
>>> a.intersection_update(b)
>>> a
{2, 3}
>>> b
{8, 2, 3, 7}
>>> c=b
>>> c
{8, 2, 3, 7}
>>> b
{8, 2, 3, 7}
>>> c.add(11)
>>> b
{2, 3, 7, 8, 11}
>>> c
{2, 3, 7, 8, 11}
>>> d=c.copy()
>>> d
{2, 3, 7, 8, 11}
>>> c
{2, 3, 7, 8, 11}
>>> d.add(30)
>>> d
{2, 3, 7, 8, 11, 30}
>>> c
{2, 3, 7, 8, 11}
>>> len(c)
5
>>> min(c)
2
>>> max(c)
11
>>> sorted(c)
[2, 3, 7, 8, 11]
>>> sum(c)
31
