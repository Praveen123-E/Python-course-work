'''
#match
import re
pattern='[abc]'

text='codegnan'

res=re.match(pattern,text)#check wheater the string is start with or not

print(res.group() if res else "No Match Found")

#c


# search
import re
pattern='[a-z]'

text='Python version 3.11'

res=re.search(pattern,text) #checks entire string

print(res.group() if res else "No Match Found")

#y
#No Match Found


#findall
import re
pattern='[a-z]'

text='Python version 3.11'

res=re.findall(pattern,text) #return in list format
print(res)

['y', 't', 'h', 'o', 'n', 'v', 'e', 'r', 's', 'i', 'o', 'n']


#finditer
import re
pattern='[a-z]'

text='Python version 3.11'

res=re.finditer(pattern,text) #return index  of charcter
#it is lazy so we use for loop
for i in res:
    print(i.group(),i.start())

y 1
t 2
h 3
o 4
n 5
v 7
e 8
r 9
s 10
i 11
o 12
n 13



#fullmatch match complete string

import re
pattern='[a-z]{9}'

text='abcdefghi'

res=re.fullmatch(pattern,text)

print(res.group() if res else "No Match Found")

abcdefghi



#split

import re
pattern=r'[,a+yn]'

text='java,python,c++'

res=re.split(pattern,text)

print(res)

['j', 'v', '', 'p', 'tho', '', 'c', '', '']




#sub it is replace function

import re
pattern=r'[0-9]{2}'

text='python: 34 mysql:78 java : 55 html 45'

res=re.sub(pattern,'**',text)

print(res)

python: ** mysql:** java : ** html **

'''































