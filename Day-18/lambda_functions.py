'''
syntax:
var = lambda agr:exp



add = lambda a,b:a+b
print(add(12,13))
print(add(22,43))

25
65




wish = lambda name: f'welcome to the python course {name}'

print(wish('praveen'))
print(wish('kumar'))


welcome to the python course praveen
welcome to the python course kumar



gst=lambda price: price*0.18

print(gst(1000))
print(gst(800))
print(gst(3000))

180.0
144.0
540.0



greatest =lambda a,b: a if a>b else b
print(greatest(20,43))

print(greatest(500,467))

43
500



iseven=lambda a:f'{a}-even number' if a%2==0 else f'{a}-odd number'

print(iseven(20))
print(iseven(67))

20-even number
67-odd number


bill=lambda charge: charge if charge>99 else charge+30
print(bill(150))
print(bill(45))
print(bill(98))

150
75
128



#nested if else:

login=True
instock=True

status=lambda login,instock :("You can buy product" if instock else "Product is out of stock") if login else "Login to buy product"

print(status(login,instock))


You can buy product

# loops

l=[1,2,3,4,5,6,7]

res=list(map(lambda i:i**3,l))

print(res)

[1, 8, 27, 64, 125, 216, 343]



names=['praveen','kumar','ajay','rahul','virat']

t=list(map(lambda i:i.title(),names))
print(t)

['Praveen', 'Kumar', 'Ajay', 'Rahul', 'Virat']




l=[1,2,3,4,5,6,7,8,9,10]

res=list(filter(lambda i:i%2==0,l))
print(res)

[2, 4, 6, 8, 10]


l=[1,2,3,4,5,6,7,8,9,10]

res=list(filter(lambda i:i>5,l))
print(res)

[6, 7, 8, 9, 10]

 

l=[1,2,3,4,5,6,7,8,9,10]

res=list(filter(lambda i:i%3==0,l))
print(res)

[3, 6, 9]



from functools import reduce

l=[1,2,3,4,5,6,7,8,9,10,11,12]

s=reduce(lambda sum,i:sum+i,l)

t=reduce(lambda pro,i:pro*i,l)

m=reduce(lambda max,i:max if max>i else i,l)
mi=reduce(lambda min,i:min if min<i else i,l)
print(s,t,m,mi)

78 479001600 12 1


#sorting

d={'praveen':80,'kumar':94,'virat':40,'rahul':67}
print(dict(sorted(d.items())))

print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))



{'kumar': 94, 'praveen': 80, 'rahul': 67, 'virat': 40}
{'virat': 40, 'rahul': 67, 'praveen': 80, 'kumar': 94}
{'virat': 40, 'rahul': 67, 'praveen': 80, 'kumar': 94}
{'kumar': 94, 'praveen': 80, 'rahul': 67, 'virat': 40}



'''
 






