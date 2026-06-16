#int float complex str list tuple set dict

#not effect to outer variable: int float complex str tuple bool
#all immutable datatypes are not effect to outer scope
#effect to outer scope:list set dict
'''
def update(n):
    n+=10
    print("Inside:",n)


n=10
update(n)
print("Outside:",n)

Inside: 20
Outside: 10



def update(n):
    n+=10
    print("Inside:",n)


n=10.4
update(n)
print("Outside:",n)


Inside: 20.4
Outside: 10.4



def update(n):
    n+=10
    print("Inside:",n)


n=(3+4j)
update(n)
print("Outside:",n)

Inside: (13+4j)
Outside: (3+4j)



def update(n):
    n+='  lang'
    print("Inside:",n)


n="Python"
update(n)
print("Outside:",n)

Inside: Python  lang
Outside: Python


def update(n):
    n.append(6)
    print("Inside:",n)


n=[1,2,3,4]
update(n)
print("Outside:",n)

Inside: [1, 2, 3, 4, 6]
Outside: [1, 2, 3, 4, 6]


def update(n):
    n+=(2,3)
    print("Inside:",n)


n=(1,2,3,4)
update(n)
print("Outside:",n)

Inside: (1, 2, 3, 4, 2, 3)
Outside: (1, 2, 3, 4)



def update(n):
    n.add(8)
    print("Inside:",n)


n={1,2,3,4}
update(n)
print("Outside:",n)

Inside: {1, 2, 3, 4, 8}
Outside: {1, 2, 3, 4, 8}

'''


def update(n):
    n.add({'o':4})
    print("Inside:",n)


n={'n':"p",'a':'b'}
update(n)
print("Outside:",n)























