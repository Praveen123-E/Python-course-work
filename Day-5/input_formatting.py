Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#input formatting

name=input()
praveen
a=5
a
5
name
'praveen'
name=input("Enter your name: ")
Enter your name: praveen
name
'praveen'
age=input()
21
age
'21'
age=input("Enter your age: ")
Enter your age: 22
age
'22'

age=int(input())
23
age
23

cgpa=float(input())

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    cgpa=float(input())
ValueError: could not convert string to float: ''
9
9
cgpa
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    cgpa
NameError: name 'cgpa' is not defined
cgpa=float(input())
8
cgpa
8.0
#str
name=input()
praveen
name
'praveen'
#list for we use split function to convert str in list
students=input().split()
praveen kumar rahul naveen
students
['praveen', 'kumar', 'rahul', 'naveen']
#tuple
# for tuple we use tuple to convert str in list then we use tuple function
stu=tuple(input().split())
praveen kumar rahul naveen
stu
('praveen', 'kumar', 'rahul', 'naveen')
#SET for set we use set function to convert into set

s=set(input().split())
is not is not and or is 
s
{'or', 'and', 'not', 'is'}

#examples
products=input("enter the products: ").split()
enter the products: laptap mouse charger keyboard
products
['laptap', 'mouse', 'charger', 'keyboard']

topics=tuple(input("Enter the topics: "))
Enter the topics: token statement variable set list
topics
('t', 'o', 'k', 'e', 'n', ' ', 's', 't', 'a', 't', 'e', 'm', 'e', 'n', 't', ' ', 'v', 'a', 'r', 'i', 'a', 'b', 'l', 'e', ' ', 's', 'e', 't', ' ', 'l', 'i', 's', 't')
topics=tuple(input("Enter the topics: ")).split()
Enter the topics: token statement variable set list
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    topics=tuple(input("Enter the topics: ")).split()
AttributeError: 'tuple' object has no attribute 'split'
topics
('t', 'o', 'k', 'e', 'n', ' ', 's', 't', 'a', 't', 'e', 'm', 'e', 'n', 't', ' ', 'v', 'a', 'r', 'i', 'a', 'b', 'l', 'e', ' ', 's', 'e', 't', ' ', 'l', 'i', 's', 't')
topics=tuple(input("Enter the topics: ").split())
Enter the topics: token statement variable set list
topics
('token', 'statement', 'variable', 'set', 'list')
op =set(input("Enter the operators: ").split())
Enter the operators: in not or and in is or not in
op
{'not', 'or', 'and', 'is', 'in'}
marks=input("enter the marks: ").split()
enter the marks: 90 20 35 45 63 
marks
['90', '20', '35', '45', '63']
list(map(int,marks))
[90, 20, 35, 45, 63]
list(map(float,marks))
[90.0, 20.0, 35.0, 45.0, 63.0]
list(map(int,marks))
[90, 20, 35, 45, 63]
#list of integers
# by using map function
marks=list(map(int,input("enter the marks: ").split()))
enter the marks: 20,30,54,09,69
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    marks=list(map(int,input("enter the marks: ").split()))
ValueError: invalid literal for int() with base 10: '20,30,54,09,69'
list(map(int,input("enter the marks: ").split()))
enter the marks: 
[]
marks=list(map(int,input("enter the marks: ").split()))
enter the marks: 20 60 70 50
marks
[20, 60, 70, 50]
prices=tuple(map(int,input("enter the prices:").split()))
enter the prices:2345 432 3456 876
prices
(2345, 432, 3456, 876)
rating=set(map(int,input("enter your rating: ").split()))
enter your rating: 4 5 6 4 5 3 4
rating
{3, 4, 5, 6}
per=list(map(float,input("enter your per:".split())))
['enter', 'your', 'per:']
per=list(map(float,input("enter your per:").split()))
enter your per:34 54.6 45 3 4
per
[34.0, 54.6, 45.0, 3.0, 4.0]
prices=tuple(map(float,input("enter your prices:".split())))
['enter', 'your', 'prices:']
prices=tuple(map(float,input("enter your prices: ").split()))
enter your prices: 343 234 5655 7766 333
prices
(343.0, 234.0, 5655.0, 7766.0, 333.0)
prices=set(map(float,input("enter your prices: ").split()))
enter your prices: 333 444 22 333 565 654
prices
{333.0, 654.0, 565.0, 22.0, 444.0}

#
a,b=10,20
a
10
b
20
a,b=[10,20]
a
10
b
20

username,password=input("enter username and password:").split()
enter username and password:praveen 123456
username
'praveen'
password
'123456'
# side of rectangle
a,b,c,d=list(map(int,input("enter 4 side of rectangle: ").split()))
enter 4 side of rectangle: 3 4 5 6
a
3
b
4
c
5
d
6
price,dicount=list(map(float,input().split()))
2500 10
price
2500.0
discount
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    discount
NameError: name 'discount' is not defined. Did you mean: 'dicount'?
>>> dicount
10.0
>>> #eval method
>>> #eval is use to declare all types
>>> a=eval(input())
232
>>> a
232
>>> a=eval(input())
32.43
>>> a
32.43
>>> s=eval(input())
"python"
>>> s
'python'
>>> type(s
...      )
<class 'str'>
>>> a=eval(input())
[1,2,3,4]
>>> a
[1, 2, 3, 4]
>>> a=eval(input())
(1,2,3,4)
>>> a
(1, 2, 3, 4)
>>> a=eval(input())
[1,2,34,3,2,1}
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1
    [1,2,34,3,2,1}
                 ^
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a=eval(input())
{1,2,3,2,1,3,2,4}
>>> a
{1, 2, 3, 4}
>>> a=eval(input())
True
>>> a
True
>>> type(a)
<class 'bool'>
