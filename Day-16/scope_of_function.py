'''
#local scope

def display():
    n=10
    print("Inside",n)

display()
#print("outside",n)  error because n in function



#global access/scope
n=10
def display():
    print("Inside",n)

display()
print("Outside",n)


#global keyword

def display():
    global n
    n=10
    print("Inside",n)

display()
print("Outside",n)


n=10
def display():
    global n
    print("Inside",n)

display()
print("Outside",n)


n=10
def display(n):
    #global n
    n+=10
    print("Inside",n)

display(n)
print("Outside",n)


def display():
    global n
    n+=10
    print("Inside",n)
n=10
display()
print("Outside",n)



#Ensclosing scope or nested functions

def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("inner function:",n)

    inner()

    print("Outer Function:",n)

outer()


s="Python"
print(len(s))

len=5
print(len(s))

TypeError: 'int' object is not callable

'''





















