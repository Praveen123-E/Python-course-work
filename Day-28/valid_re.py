'''

import re

pattern = r'^[a-zA-Z]{2,15}([a-zA-Z]{2,15})+$'

text=input("Enter the text: ")

res=re.fullmatch(pattern,text)

print("Valid format" if res else "Invalid Format")


Enter the text: praveen
Valid format



import re

pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

text=input("Enter the text: ")

res=re.fullmatch(pattern,text)

print("Valid format" if res else "Invalid Format")


#Enter the text: praveen@gmail.com
#Valid format

Enter the text: praveen123.com
Invalid Format



import re

pattern = r'^(?:\+91|0)?[6-9]\d{9}$'


text=input("Enter the text: ")

res=re.fullmatch(pattern,text)

print("Valid format" if res else "Invalid Format")


#Enter the text: +919876765432
#Valid format

Enter the text: 3433225566
Invalid Format

Enter the text: 9898975643
Valid format



import re

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%&*?])(A-Za-z\d@$!%*?&]){8,}$'


text=input("Enter the text: ")

res=re.fullmatch(pattern,text)

print("Valid format" if res else "Invalid Format")



'''


import re

pattern = r'[a-zA-Z0-9_]{5,15}$'


text=input("Enter the text: ")

res=re.fullmatch(pattern,text)

print("Valid format" if res else "Invalid Format")


Enter the text: praveen2
Valid format

'''


