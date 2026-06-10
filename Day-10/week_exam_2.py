'''
salary=int(input())
bonus=0
if salary>=70000:
    bonus =salary *0.2
elif salary>=50000:
    bonus =salary *0.15
elif salary>=30000:
    bonus =salary *0.1
else:
    bonus =salary *0.05

print("Bonus: ",bonus)

'''
tup=tuple(input("tuple: ").split())
pro=input("Product: ")
pri=int(input("price: "))
s=set(map(int,input("set values: ").split()))

print("Tuple : ",tup)
d={}
d[pro]=pri
print("dictionary:",d)
print("set:",s)
