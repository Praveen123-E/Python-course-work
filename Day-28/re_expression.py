'''
r'h.t' . is any char ->hot hit hrt h$t
r'^c'  ^ is start
r'$g' ->end of string -> ing programming
r'ab*' ->a ab abbb abbbb
r'ab+'-> ab abb abbbb
r'to?' -> too to tot

r'[a-zA-Z0-9].-> a b cb ABC 099
r'[aeiou]' -> aeioupen
r'[#@&*!]'-> # $ &


#r'xx\.gmail.com'
r'[10]'-> 9876543210
r'[2,8]'->9876 98765
r'{5,}'->123456789

r'(the)'
r'(ae)'

r'0|1'




import re

pattern = r'h.t\b'

text="hot hit hrt h$t hate hoart heart"
res=re.findall(pattern,text)
print(res)

['hot', 'hit', 'hrt', 'h$t']



import re

pattern = r'^h'

text="hot hit hrt h$t hate hoart heart uot hjt"
res=re.findall(pattern,text)
print(res)

['h']



# for ending

import re

pattern = r'j$'

text="hot hit hrt h$t hate hoart heart uot"
res=re.findall(pattern,text)
print(res)



import re

pattern = r'to?\b'

text="too too t toooooo"
res=re.findall(pattern,text)
print(res)

['t']



import re

pattern = r'[a-z]{4,5}'

text="sereedf fghj fghj hsbjc jvkj "
res=re.findall(pattern,text)
print(res)

['seree', 'fghj', 'fghj', 'hsbjc', 'jvkj']

 

import re

pattern = r'(python)'

text="pyth pythn python puthon"
res=re.findall(pattern,text)
print(res)

['python']

'''

