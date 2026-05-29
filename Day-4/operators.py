Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#day-4

#Operators
#1.arithmetic operator
# +,-,*,/,//,**,%
a=10
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a%b
0
a//b
2
a**b
10240000000000
17%3
2
3
3







































#comparison operators
#<,>,<=,>=,==,!=
a
20
b
10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True

#assignnment operators
#=,+=,-=,*=,/=,//=,%=,**=

a
20
b
10
10
10
y=5
y=y+5
y
10
y=y+10
y
20
y+=10
y
30
y-=10
y
20
y*=2
y
40
y/=2
y
20.0
y//=2
y
10.0
y%=3
y
1.0
y=4
y
4
y**=2
y
16
#logical operators
# and,or, not
a
20
b
10
a%20==0 and a%30==0 and a<b
False
a%20==0 or a%30==0 or  a<bFalse
True
a%22==0 or b%20==0 or a<b
False
not a<b
True
not a>b
False

#membership operators
# in, not in
# it used for str,list,tuple ,set,dict
a="python programming"
a
'python programming'
"y" in a
True
"z" in a
False
"z" not in a
True
l=["java","python","mysql","c++","c","html"]
l
['java', 'python', 'mysql', 'c++', 'c', 'html']
"mysql" in l
True
"javascript" in l
False
"javascript" not in l
True
t=("java","c","python")
t
('java', 'c', 'python')
"c++" in t
False
"c" in t
True
"python" not in t
False
d={"name":"egg","nums":20}
d
{'name': 'egg', 'nums': 20}
"egg" in d
False
"name" in d
True
"nums" in d
True
20 in d
False
20 not in d
True
# here membership operator give only key names it not give keys

#identity operators
# is , is not

l=[1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True
n=m
n
[1, 2, 3, 4, 5]
n is m
True
l is m
False
# because we create two lists l,m so their memory loction is different
l is m
False
l is not m
True
l is not n
True
n is m
True
m in n
False
m is n
True
id(l)
2273726135552
id(m)
2273681449152
id (n)
2273681449152
2273681449152
2273681449152
"""
 Bitwise Operators

 &, |,^,~,<<,>>
 0 - 0000
 1 - 0001
 2 - 0010
 3 - 0011
 4 - 0100
 5 - 0101
 6 - 0110
 7 - 0111
 8 - 1000
 9 - 1001
 10 - 1010
 11 - 1011
 12 - 1100
 13 - 1101
 14 - 1110
 15 - 1111
 """
'\n Bitwise Operators\n\n &, |,^,~,<<,>>\n 0 - 0000\n 1 - 0001\n 2 - 0010\n 3 - 0011\n 4 - 0100\n 5 - 0101\n 6 - 0110\n 7 - 0111\n 8 - 1000\n 9 - 1001\n 10 - 1010\n 11 - 1011\n 12 - 1100\n 13 - 1101\n 14 - 1110\n 15 - 1111\n '
8 & 14
8
>>> 8&7
0
>>> 8|7
15
>>> 10^11
1
>>> ~10
-11
>>> ~34
-35
>>> 15>>1
7
>>> 15>>3
1
>>> 16<<1
32
>>> 15<<2
60
>>> # right shift remove element from right
>>> # left shift add 0 at end
>>> 
>>> # output
>>> a=10
>>> b=20.12
>>> c="python"
>>> print(a,b,c)
10 20.12 python
>>> print("a=","b=","c=")
a= b= c=
>>> 
... print("a=",a,"b=",b,"c=",c)
a= 10 b= 20.12 c= python
>>> print("a=",a,"b=",b,"c=",c,sep="\t")
a=	10	b=	20.12	c=	python
>>> print("a=",a,"b=",b,"c=",c,end="@@")
a= 10 b= 20.12 c= python@@
>>> print("a=",a,"b=",b,"c=",c,sep="$",end="@@")
a=$10$b=$20.12$c=$python@@
>>> print(f'a={a} b={b} c={c}')
a=10 b=20.12 c=python
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
a=10 b=20.12 c=python
>>> print('a= {} b={} c={}'.format(a,b,c))
a= 10 b=20.12 c=python
>>> print('a={2} b={0} c={1}'.format(a,b,c))
a=python b=10 c=20.12
