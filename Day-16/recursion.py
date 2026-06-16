#recursion
'''
def function():
    if basecondition:
        return
    function()



def func(num):
    if num==0:
        return
  
    func(num-1)
    print(num,end=" ")

func(5)

1 2 3 4 5 



def func(num):
    if num==0:
        return
    print(num,end=" ")
    func(num-1)

func(5)
5 4 3 2 1


def sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)

print(sumofdigits(5))

15


def productofdigits(n):
    if n==0:
        return 1
    return n*productofdigits(n-1)

print(productofdigits(5))

120



def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(6))

720



#power calucation

def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
print(power(2,4)) #16
print(power(3,3)) #27


# reverse string

def reverse(s,ind):
    if ind==0:
        return s[0]
    return s[ind]+reverse(s,ind-1)
s="Python Programming"
print(reverse(s,len(s)-1))

gnimmargorP nohtyP

'''

def rev(s):
    if len(s)==0:
        return s
    return rev(s[1:]+s[0])
s="Praveen"
print(rev(s))
    













