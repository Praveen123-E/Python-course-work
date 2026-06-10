#str list tuple set dict range()
'''
for var in seq:
    print(var)


s='python programming'
for ch in s:
    print(ch)



l=['sugar','salt','oil']
for i in l:
    print(i)
    

t=('praveen','kumar','intro','tokens')
for i in t:
    print(i)


s={'laptop','keyboard'}
for i in s:
    print(i)

d={'name':'praveen','batch':55,'course':'PFS','skills':['python','mysql','java']}
for i in d:
    print(i,d[i])

#range(start:stop+1,step)=>default values(0,n,1)

for i in range(1,11):
    print(i)
    
for i in range(2,51,2):
    print(i)


for i in range(5,101,5):
    print(i)

for i in range(20,0,-1):
    print(i)


# 3 table:
for i in range(1,11):
    a=3*i
    print(f'3 * {i} =',a)

l=[1,2,3,4]
for i in range(len(l)):
    print(l[i])

s='looping'

for i in enumerate(s):
    print(i)

for i in enumerate(s):
    print(i[0],i[1])

t=(1,22,4,3,5,6)
for i in enumerate(t):
    print(i[0],i[1])


k={5,6,7,4,3,2,1,9}
for i in enumerate(k):
    print(i[0],i[1])




#break:it exit for loop
#continue:it skip the current iteration
#pass:when where we don't to write block code just write pass to execute the code

for i in range(10):
    pass


for i in range(10):
    if i==5:
        break
    print(i)



for i in range(10):
    if i == 5:
        continue
    print(i)



s='looping statements'
for i in s:
    if i in 'aeiouAEIOU':
        print(i)


l=[23,44,33,22,12,45,65,77,88,74,67,88]
a=[]
for i in l:
    if i%2==0:
        a.append(i)
print(a)



d={'laptops':0,'chargers':2,'keyboard':10,'phone':15,'tab':0,'mouse':5}
for k,v in d.items():
    if v!=0:
        print(k,v)


t=(9,7,6,55,4,3)
for i in range(len(t)):
    print(i*t[i])
'''


name={'praveen','kumar','subbu','naresh'}
a=[]
for i in name:
    a.append(i.upper())
print(a)
    
