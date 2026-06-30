'''
### Read mode ###

file=open("sample.txt",'r')

print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)#seek is toward start position
print(file.readlines())

file.close()



Names

-------
praveen
kumar
Srikanth
ajay
Names

['Names\n', '\n', '-------\n', 'praveen\n', 'kumar\n', 'Srikanth\n', 'ajay']



try:
    file=open("samplesss.txt",'r')
except FileNotFoundError:
    print("File is not found")
    
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)#seek is toward start position
    print(file.readlines())
    file.close()

File is not found



with open("sample.txt",'r') as file: # by using with need not to be close the file


    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)#seek is toward start position
    print(file.readlines())


Names

-------
praveen
kumar
Srikanth
ajay
Names

['Names\n', '\n', '-------\n', 'praveen\n', 'kumar\n', 'Srikanth\n', 'ajay']



## append mode   # is adding at end

with open('sample.txt','a') as file:
    file.write('\npraneeth\nshiva\nsrikanth')

# added in sample file



with open('sampless.txt','a') as file:
    file.write('\npraneeth\nshiva\nsrikanth')

#file is not exist append mode create new file



#write Mode
#it first remove all data from file and write new data

with open('sampless.txt','w') as file:
    file.write('\npraneeth\nshiva\nsrikanth')


'''
with open('demo.txt','w+') as file:
    file.write('\npraneeth\nshiva\nsrikanth')
    file.seek(0)
    print(file.read())



#w+ is write and read
#r+ is read and write
# a+ is append and read

































































