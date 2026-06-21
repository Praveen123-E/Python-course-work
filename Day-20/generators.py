'''

def display():
    l=['1...50','51...100','101...150','151...200']
    yield l[0]
    yield l[1]
    yield l[2]
    yield l[3]
scroll =display()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))

1...50
51...100
101...150
151...200


def display():
    for i in range(1,11):
        yield i

n=display()
for i in range(10):
    print(next(n))

1
2
3
4
5
6
7
8
9
10


def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i

n=factors(30)
try:
    while True:
        print(next(n))
except StopIteration:
    print("End of the program")
    
1
2
3
5
6
10
15
30
End of the program

------------------------------------------------

def factors(n):
    return [i for i in range(1,n+1) if n%i==0]

def generators(res):
    for i in res:
        yield i

res=factors(60)
facts=generators(res)
for i in range(len(res)):
    print(next(facts))

1
2
3
4
5
6
10
12
15
20
30
60



def primes():
    res=[]
    for  num in range(2,101):
        for i in range(2,num//2+1):
            if num%i==0:
                break
        else:
            res.append(num)
    return res

def generators(res):
    for i in res:
        yield i

res=primes()
g=generators(res)

for i in range(len(res)):
    print(next(g))

2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97



'''











































































































