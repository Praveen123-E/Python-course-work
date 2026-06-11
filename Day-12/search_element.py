l=[2,3,4,5,8,7,10,24]
search=int(input("Enter number"))
for i in range(len(l)):
    

    if l[i]==search:
        print(f'{search} is found index-{i}')
        break
else:
    print(f'{search} is not found')
