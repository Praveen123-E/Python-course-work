'''
while condition:


i=1
while i<11:
    print(i)
    i+=1



i=2
while i<21:
    print(i)
    i+=2
    


i=10
while i>0:
    print(i)
    i-=1

l=[1,2,3,4,5,6,7,8,9]
i=0
while i<len(l):
    print(l[i])
    i+=1


l=[1,0,0,2,3,4,0,0,0,0,3,4,53,0,0,0,4,2,5,0,0,60,0,0,66,0,0]

while 0 in l:
    l.remove(0)
print(l)
'''

l=[1,0,0,2,3,4,0,0,0,0,3,4,53,0,0,0,4,2,5,0,0,60,0,0,66,0,0]
i=0
while i<len(l):
    if l[i]==0:
        l.pop(i)
    else:
        i+=1
print(l)
