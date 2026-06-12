'''
l=[[1,2,3],[4,5,6],[7,8,9]]

sum1=0
for i in l:
    for j in i:
        sum1+=j
        
print(sum1)

'''

d={'1234':{'pin':'4567','balance':2300},
   '2345':{'pin':'9876','balance':5300},
   '3456':{'pin':'5678','balance':6300},
   '4567':{'pin':'9876','balance':7300}}
'''
for i in d:
    print("Account Number:",i)
    print("Pin Number:",d[i]['pin'])

'''
for k,v in d.items():
    print("Account Number:",k)
    print("Pin Number:",v['pin'])
    
        
