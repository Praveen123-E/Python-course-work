
'''
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    if i<=m:
        for j in range(i+1):
            print("*",end=' ')
    else:
        for j in range(n-i):
            print("*",end=' ')

    print()

    
Enter the size: 9
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    if i<=m:
        print("* "*(i+1),end=' ')
    else:
        print("* "*(n-i),end=' ')

    print()

n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    if i<=m:
        print("  "*(m-i),end=' ')
        print("* "*(i+1),end=' ')
    else:
        print("  "*(i-m),end=' ')
        print("* "*(n-i),end=' ')
    

    print()

Enter the size: 9
         *  
       * *  
     * * *  
   * * * *  
 * * * * *  
   * * * *  
     * * *  
       * *  
         *  

n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    if i<=m:
        print(" "*(m-i),end=' ')
        print("* "*(i+1),end=' ')
    else:
        print(" "*(i-m),end=' ')
        print("* "*(n-i),end=' ')
    print()

Enter the size: 9
     *  
    * *  
   * * *  
  * * * *  
 * * * * *  
  * * * *  
   * * *  
    * *  
     *  

n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    if i<=m:
        print("  "*(m-i)+"* "*(i+1),end=' ')
    else:
        print("  "*(i-m)+"* "*(n-i),end=' ')
    print()
Enter the size: 13
            *  
          * *  
        * * *  
      * * * *  
    * * * * *  
  * * * * * *  
* * * * * * *  
  * * * * * *  
    * * * * *  
      * * * *  
        * * *  
          * *  
            *

            
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
    if i<=m:
        print(" "*(m-i)+"* "*(i+1),end=' ')
    else:
        print(" "*(i-m)+"* "*(n-i),end=' ')
    print()

Enter the size: 7
   *  
  * *  
 * * *  
* * * *  
 * * *  
  * *  
   *  

n=int(input("Enter the size: " ))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
    
Enter the size: 7
* * * * * * * 
*           * 
*           * 
*           * 
*           * 
*           * 
* * * * * * * 
  
n=int(input("Enter the size: " ))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==m or j==m:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()         
Enter the size: 7
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * *


n=int(input("Enter the size: " ))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()         

Enter the size: 7
* * * * * * * 
* *       * * 
*   *   *   * 
*     *     * 
*   *   *   * 
* *       * * 
* * * * * * *

'''
n=int(input("Enter the size: " ))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print() 

