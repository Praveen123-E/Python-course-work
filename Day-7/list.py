Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list is collection of characters enclosed with square barkects
l=[]
l
[]
l=list()
l
[]
type(l)
<class 'list'>
l=[10,20,30,40,50]
l
[10, 20, 30, 40, 50]
m=[60,70,80]
#operation on list
#1.concatination
l+m
[10, 20, 30, 40, 50, 60, 70, 80]
#2.repeatition

l*3
[10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
#3.indexing
l[0]
10
l[3]
40
l[-1]
50
l[-3]
30
l[-2]
40
#4.slicing
l[0:4)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
l[0:4]
[10, 20, 30, 40]
l[::-1]
[50, 40, 30, 20, 10]
l[2:5]
[30, 40, 50]
l[-1:-4]
[]
l[-1:-4:-1]
[50, 40, 30]
l[-4:-2]
[20, 30]
l[2:]
[30, 40, 50]
l[:3]
[10, 20, 30]
#5.membership
20 in l
True
30 in l
True
45 in l
False
80 not in l
True
id(l)
2249553291648
l[1]
20
l[1]=60
l
[10, 60, 30, 40, 50]
l[2]=100
l
[10, 60, 100, 40, 50]
#append
l.append(70,60)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    l.append(70,60)
TypeError: list.append() takes exactly one argument (2 given)
l.append(70)
l
[10, 60, 100, 40, 50, 70]
l.insert(1,20)
l
[10, 20, 60, 100, 40, 50, 70]
l.insert(3,80)
l
[10, 20, 60, 80, 100, 40, 50, 70]
#adding multiple elements at end
l.extend(90,50,60)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    l.extend(90,50,60)
TypeError: list.extend() takes exactly one argument (3 given)
l.extend[50,60,70]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    l.extend[50,60,70]
TypeError: 'builtin_function_or_method' object is not subscriptable
l.extend(20,30,40)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    l.extend(20,30,40)
TypeError: list.extend() takes exactly one argument (3 given)
l.remove(40)
l
[10, 20, 60, 80, 100, 50, 70]
l.extend([30,40,50])
l
[10, 20, 60, 80, 100, 50, 70, 30, 40, 50]
#pop
#pop is used to remove last element
l.pop()
50
l.pop()
40
l
[10, 20, 60, 80, 100, 50, 70, 30]
l.pop(-2)
70
l
[10, 20, 60, 80, 100, 50, 30]
l.remove(100)
l
[10, 20, 60, 80, 50, 30]
del l[2]
l
[10, 20, 80, 50, 30]
del l[-3]
l
[10, 20, 50, 30]
l.clear()
l
[]
l=[10, 20, 60, 80, 100, 50, 70, 30, 40, 50]
l
[10, 20, 60, 80, 100, 50, 70, 30, 40, 50]
sorted(l)
[10, 20, 30, 40, 50, 50, 60, 70, 80, 100]
l.sort()
l
[10, 20, 30, 40, 50, 50, 60, 70, 80, 100]
>>> min(l)
10
>>> max(l)
100
>>> l.reverse()
>>> l
[100, 80, 70, 60, 50, 50, 40, 30, 20, 10]
>>> l=[10, 20, 60, 80, 100, 50, 70, 30, 40, 50]
>>> sorted(l,reverse=True)
[100, 80, 70, 60, 50, 50, 40, 30, 20, 10]
>>> l.index(70)
6
>>> l.index(50)
5
>>> l'index(33)
SyntaxError: unterminated string literal (detected at line 1)
>>> l.index(33)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    l.index(33)
ValueError: 33 is not in list
>>> l.count(50)
2
>>> l.count(20)
1
>>> l
[10, 20, 60, 80, 100, 50, 70, 30, 40, 50]
>>> m=l
>>> m.append(400)
>>> l
[10, 20, 60, 80, 100, 50, 70, 30, 40, 50, 400]
>>> m
[10, 20, 60, 80, 100, 50, 70, 30, 40, 50, 400]
>>> #this is deep copy
>>> # it effect on both lists
>>> n=l.copy()
>>> n
[10, 20, 60, 80, 100, 50, 70, 30, 40, 50, 400]
>>> l
[10, 20, 60, 80, 100, 50, 70, 30, 40, 50, 400]
>>> n.append(200)
>>> n
[10, 20, 60, 80, 100, 50, 70, 30, 40, 50, 400, 200]
>>> l
[10, 20, 60, 80, 100, 50, 70, 30, 40, 50, 400]
>>> #here this copy method is called shall copy ,it means there is no effect of changing elements of list
