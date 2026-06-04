Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s='   hello   world   '
>>> s
'   hello   world   '
>>> s.strip()
'hello   world'
>>> s.lstrip()
'hello   world   '
>>> s.rstrip()
'   hello   world'
>>> #string testing methods
>>> s='string.py'
>>> s
'string.py'
>>> s.startswith('str')
True
>>> s.startswith('pra')
False
>>> 'praveen'.isalpha()
True
>>> 'vjdhvdsbvhjdvh sdjv'.isalpha()
False
>>> 'praveen@123'.isalpha()
False
>>> "123yehydbc".isalpha()
False
>>> '1232'.isalnum()
True
>>> ' reads 1123'.isalnum()
False
>>> 'praveen123'.isalnum()
True
>>> ' ewe123'.isalnum()
False
>>> 'ghgdh1233'.islower()
True
>>> 'ghgg@#hjhvb8768'.islower()
True
>>> #it checks only characters
>>> 'AHDHC'.isupper()
True
>>> 'DGHVB@#J123'.isupper()
True
>>> 'FVJshchc'.isupper()
False
>>> 'cgschADD'.islower()
False
' '.isspace()
True
'  hello '.isspace()
False
'Py Pra Lan'.istitle()
True
'Py bnb'.istitle()
False
'varible123'.isidentifier()
True
'a@123'.isidentifier()
False
23.2.isdecimal()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    23.2.isdecimal()
AttributeError: 'float' object has no attribute 'isdecimal'
'232.32'.isdecimal()
False
