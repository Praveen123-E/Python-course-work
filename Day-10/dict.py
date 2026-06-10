data={
    'subbu':{'status':True,'python':98,'mysql':67,'flask':89},
    'praveen':{'status':True,'python':90,'mysql':93,'flask':99},
    'kumar':{'status':False,'python':None,'mysql':None,'flask':34},
    'ajay':{'status':True,'python':55,'mysql':68,'flask':77},
    'ranjith':{'status':True,'python':55,'mysql':99,'flask':89}
    }
name=input("Enter the name: ")
if name in data:
    if data[name]['status']:
        total=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg = total/3
        if avg>90:
            print(f'Congrations {name},You got first class!!!')
        elif avg>70:
            print(f'Good {name},Keep it up for the next time!!')
        elif avg>35:
            print(f'Better {name},work hard next time!')
        else:
            print(f'{name}, you have failed in tje exam.Bring your parents.')
    else:
        print(f"{name} didn't write the exam. Bring your parents")

else:
    print(f'{name} is not found')
    
