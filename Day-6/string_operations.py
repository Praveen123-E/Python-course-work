Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s="Python programming"
len(s)
18
sorted(s)
[' ', 'P', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'r', 'r', 't', 'y']
s.sort()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.sort()
AttributeError: 'str' object has no attribute 'sort'
min(s)
' '
max(s)
'y'
ord("a")
97
ord("A")
65
ord("")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    ord("")
TypeError: ord() expected a character, but string of length 0 found
ord(" ")
32
chr(120)
'x'
chr(65)
'A'
chr(134)
'\x86'
chr(37)
'%'
#case conversions
s='python Programming'
s
'python Programming'
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'PYTHON pROGRAMMING'
s.casefold()
'python programming'
len(s)
18
s.center(28,"-")
'-----python Programming-----'
s.ljust(5,"-")
'python Programming'
s.ljust(28,'-')
'python Programming----------'
s.rjust(28,'-')
'----------python Programming'
'123'.zfill(5)
'00123'
'123'.zfill(10)
'0000000123'

'123'.zfill(3)
'123'
s
'python Programming'
s.find("o")
4
s.find("g")
10
s.rfind("o")
9
s.lfind("p")
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.lfind("p")
AttributeError: 'str' object has no attribute 'lfind'. Did you mean: 'find'?
s.index("o")
4
s.rindex("o")
9
s
'python Programming'
s.replace("python","java")
'java Programming'
s.maketrans("python","123456")
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans("python","123456"))
'123456 Pr5grammi6g'
s='java,python,javascript,c,c++'
s
'java,python,javascript,c,c++'
s.split(",")
['java', 'python', 'javascript', 'c', 'c++']
s.split(",",2)
['java', 'python', 'javascript,c,c++']
s.rsplit(",",2)
['java,python,javascript', 'c', 'c++']
g="sdfdf\nhffb;\nvsdsvdv\nfrfee'
SyntaxError: unterminated string literal (detected at line 1)
>>> g="sdfdf\nhffb;\nvsdsvdv\nfrfee"
>>> s.splitlines()
['java,python,javascript,c,c++']
>>> g.splitlines()
['sdfdf', 'hffb;', 'vsdsvdv', 'frfee']
>>> l=['java,python,javascript', 'c', 'c++']
>>> ''.join(l)
'java,python,javascriptcc++'
>>> ' '.join(l)
'java,python,javascript c c++'
>>> '@'.join(l)
'java,python,javascript@c@c++'
>>> l=['java', 'python', 'javascript', 'c', 'c++']
>>> ''.join(l)
'javapythonjavascriptcc++'
>>> ' '.join(l)
'java python javascript c c++'
>>> '@',join(l)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    '@',join(l)
NameError: name 'join' is not defined
>>> '@',join(l)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    '@',join(l)
NameError: name 'join' is not defined
>>> "@".join(l)
'java@python@javascript@c@c++'
>>> s
'java,python,javascript,c,c++'
>>> s.partition(',')
('java', ',', 'python,javascript,c,c++')
>>> s.rpartition(',')
('java,python,javascript,c', ',', 'c++')
>>> 
>>> t='Hello praveen'
>>> t.encode()
b'Hello praveen'
>>> .decode()
SyntaxError: invalid syntax
>>> t='hello 😀'
>>> t.encode()
b'hello \xf0\x9f\x98\x80'
>>> b'hello \xf0\x9f\x98\x80'.decode()
'hello 😀'
