'''
l=[var for var in seq]
l=[var for var in seq if condition]
l=[var if condition else var for var in seq]




res1=[i for i in range(1,11)]
print(res1)

res2=[i for i in range(3,31,3)]
print(res2)

res3=[i for i in range(2,51,2)]
print(res3)

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]



a='python programming'
l=[]
for i in a:
    if i in "aeiouAEIOU":
        l.append(i)
print(l)




l=[i for i in a if i in 'aeiouAEIOU']
print(l)

['o', 'o', 'a', 'i']




a=[1,2,3,4,3,5,4,6,55,66,33,4,22,5,6,8,899,90]

l=[]
for i in a:
    if i%2==0:
        l.append(i)

    else:
        l.append(0)

print(l)

l1=[i if i%2==0 else 0 for i in a ]
print(l1)


[0, 2, 0, 4, 0, 0, 4, 6, 0, 66, 0, 4, 22, 0, 6, 8, 0, 90]
[0, 2, 0, 4, 0, 0, 4, 6, 0, 66, 0, 4, 22, 0, 6, 8, 0, 90]



l=[int(input(f"Enter the number {i+1}:")) for i in range(10)]
print(l)

Enter the number 1:2
Enter the number 2:3
Enter the number 3:4
Enter the number 4:5
Enter the number 5:77
Enter the number 6:54
Enter the number 7:22
Enter the number 8:12
Enter the number 9:3
Enter the number 10:4
[2, 3, 4, 5, 77, 54, 22, 12, 3, 4]


l=[]
for i in range(3):
    for j in range(1,4):
        l.append(j)

print(l)

l1=[j for i in range(3) for j in range(1,4)]
print(l1)

[1, 2, 3, 1, 2, 3, 1, 2, 3]
[1, 2, 3, 1, 2, 3, 1, 2, 3]


l=[]

for i in range(3):
    a=[]
    for j in range(1,4):
        a.append(j)
    l.append(a)
    

print(l)



l1=[[j for j in range(1,4)] for i in range(3)]

print(l1)


[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]


s=set()
for i in range(1,11):
    s.add(i)

s1={i for i in range(1,11)}
print(s,s1)


{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


d={}
for i in range(1,11):
    d[i]=i*i

print(d)

res={i:i*i for i in range(1,11)}
print(res)

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

'''
'''
d={}
for i in range(5):
    key=input("Enter the name:")
    v=int(input("Enter the marks"))
    d[key]=v

print(d)


d1={input("Enter the name:") : int(input("Enter the marks")) for i in range(5) }

print(d1)

Enter the name:praveen
Enter the marks99
Enter the name:kumar
Enter the marks67
Enter the name:virat
Enter the marks98
Enter the name:rohit
Enter the marks27
Enter the name:rahul
Enter the marks29
{'praveen': 99, 'kumar': 67, 'virat': 98, 'rohit': 27, 'rahul': 29}

'''











































































