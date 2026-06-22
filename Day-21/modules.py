'''

import sys
print(sys.argv)
print(sys.path)
print(sys.version)
print("Before exit")
sys.exit()
print("After exit")



import platform

print(platform.system(),platform.release(),platform.processor())


Windows 11 Intel64 Family 6 Model 154 Stepping 3, GenuineIntel



import math

print(math.pi)
print(math.e)
print(math.sqrt(25))
print(math.pow(2,4))

print(math.ceil(12.33)) # it return upper boundary(13)
print(math.ceil(12.000000001))
print(math.ceil(12.999999999))

print(math.floor(12.3)) #it return lower boundary(12)
print(math.floor(12.0000000001))
print(math.floor(12.9999999999))

print(round(20.1))
print(round(20.9))
print(round(20.5))
print(round(20.51))

3.141592653589793
2.718281828459045
5.0
16.0
13
13
13
12
12
12
20
21
20
21




import math

print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(8,28))

print(math.log(10,10))
print(math.sin(10))
print(math.cos(10))
print(math.tan(10))

print(math.degrees(20))
print(math.radians(20))

12.0
120
4
1.0
-0.5440211108893698
-0.8390715290764524
0.6483608274590866
1145.9155902616465
0.3490658503988659




import random

random.seed(4)# to products same output 
print(random.random())#blw 0 to 1
print(random.randint(1,6))
print(random.uniform(1,6))

l=['python','c','c++','java','html']

print(random.choice(l))
print(random.choices(l,k=3))

s='rps'
print(random.choice(s))
print(l)
random.shuffle(l)
print(l)

0.23604808973743452
1
4.606084525438332
java
['python', 'python', 'c++']
p
['python', 'c', 'c++', 'java', 'html']
['html', 'java', 'c++', 'c', 'python']


import collections

s='python progromming language'

print(collections.Counter(s))

d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)

Counter({'g': 4, 'o': 3, 'n': 3, 'p': 2, ' ': 2, 'r': 2, 'm': 2, 'a': 2, 'y': 1, 't': 1, 'h': 1, 'i': 1, 'l': 1, 'u': 1, 'e': 1})
{'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 3, 'n': 3, ' ': 2, 'r': 2, 'g': 4, 'm': 2, 'i': 1, 'l': 1, 'a': 2, 'u': 1, 'e': 1}




import collections

s='python progromming language'

d=collections.defaultdict(int)

print(d)
for i in s:
    
    d[i]+=1
print(d)

defaultdict(<class 'int'>, {})
defaultdict(<class 'int'>, {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 3, 'n': 3, ' ': 2, 'r': 2, 'g': 4, 'm': 2, 'i': 1, 'l': 1, 'a': 2, 'u': 1, 'e': 1})


import collections

l=collections.deque([])

l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.popleft()
l.popleft()
l.popleft()
l.append(50)
l.append(60)
l.popleft()

print(l)
#deque([50, 60])

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()

print(l)


deque([50, 60])
deque([60, 50, 40, 30])



import itertools

print(list(itertools.combinations('abcd',2)))
print(list(itertools.permutations('abcd',2)))

[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]
[('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('b', 'd'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c')]




from itertools import combinations,permutations

com=combinations('abcd',2)
print([''.join(i) for i in com])

per=permutations('abcd',2)
print([''.join(i) for i in per])


['ab', 'ac', 'ad', 'bc', 'bd', 'cd']
['ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca', 'cb', 'cd', 'da', 'db', 'dc']

'''

















































































































