'''

n=int(input("Enter the size:"))

for row in range(n):
    for col in range(n):
        print('*',end=' ')

    print()




n=int(input("Enter the size:"))

for row in range(n):
    for col in range(n):
        print(col%2,end=' ')
    print()

output:
Enter the size:5
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0



n=int(input("Enter the size:"))

for row in range(n):
    for col in range(row +1):
        print('*',end=' ')
    print()
    
Enter the size:5
* 
* * 
* * * 
* * * * 
* * * * *


n=int(input("Enter the size:"))

for i in range(n):
    for j in range(n-i):
        
        print('*',end=' ')
    print()
  
Enter the size:5
* * * * * 
* * * * 
* * * 
* * 
*


n=int(input("Enter the size:"))

for i in range(n):
    for sp in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
Enter the size:5
        * 
      * * 
    * * * 
  * * * * 
* * * * *

n=int(input("Enter the size:"))

for row in range(n):
    for sp in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()
Enter the size:5
* * * * * 
  * * * * 
    * * * 
      * * 
        *



n=int(input("Enter the size:"))

for row in range(n):
    for col in range(n):
        print((row +col)%2,end=' ')
    print()

Enter the size:5
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 


n=int(input("Enter the size:"))
c=1
for row in range(n):
    for col in range(row+1):
        print(str(c),end=' ')
        c+=1
    print()

Enter the size:5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
     

n=int(input("Enter the size:"))
c=1
for row in range(n):
    for col in range(row+1):
        print(str(c).zfill(2),end=' ')
        c+=1
    print()

Enter the size:5
01 
02 03 
04 05 06 
07 08 09 10 
11 12 13 14 15

'''
    
