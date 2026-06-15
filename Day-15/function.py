'''
def function_name(arg):
    #stmts
    return

function_name(parameter)


def wish(name):
    print(f' Welcome to the Python course {name} ')

wish('praveen')
wish('kumar')
wish('ajay')



def iseven(num):
    if num%2==0:
        return f'{num} is even number '
    else:
        return f' {num} is odd number '

    
num=int(input("Enter the number: "))
print(iseven(num))



def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

num=int(input("Enter the number: "))
print(factorial(num))



def factors(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
num=int(input("enter the number: "))
factors(num)



def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return f' {num} is not prime number'
    return f' {num} is prime number'
num=int(input("enter the number: "))
print(isprime(num))



def prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1

    if count==2:
        print(f' {num} is prime number ')
    else:
        print(f' {num} is not prime number')

num=int(input("Enter the number: "))
prime(num)


type of arguments

1.postional
2.keyword
3.default
4.variable

#1.postional argument

def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display("praveen","praveen@gmail.com","p@123")
display("praveen@gmail.com","p@123","praveen")
display("p@123","praveen","praveen@gmail.com")

2.keyword argument

def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display(name="praveen",email="praveen@gmail.com",pwd="p@123")
display(email="praveen@gmail.com",pwd="p@123",name="praveen")
display(pwd="p@123",name="praveen",email="praveen@gmail.com")


3.default argument

def display(name,email,pwd=''):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display("praveen","praveen@gmail.com","p@123")
display("praveen","praveen@gmail.com")


4.variable argument

def display(*names):
    print("Name:",names)

display('praveen','kumar','naresh','akhil')
display('praveen','dinesh','akhil')
display("nagendra")

postional variable argument
'''

def display(**names):
    print("Name:",names)

display(k1='praveen',k2='kumar',k3='naresh')
display(k1='praveen',k2='dinesh',k3='akhil')
display(k1="nagendra")



