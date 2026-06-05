Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary is collect of key value pair
#it is ordered
d={}
d=dict()
d
{}
type(d)
<class 'dict'>
d={'k1':2,'k2':3}
d
{'k1': 2, 'k2': 3}
d=dict()
d
{}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
#in dict values be any datatype but key must be immutable
#keys must be unique and immutable
#values to be any thing
d
{1: 'int', 12.3: 'float'}
d[2+3j]='complex'
d[praveen]='str'
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d[praveen]='str'
NameError: name 'praveen' is not defined
d['praveen']='str'
d[[1,2,3]]='list'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: unhashable type: 'list'
d=[(1,2,3)]='tuple'
SyntaxError: cannot assign to literal
d
{1: 'int', 12.3: 'float', (2+3j): 'complex', 'praveen': 'str'}
d[(1,2,3)]='tuple'
d
{1: 'int', 12.3: 'float', (2+3j): 'complex', 'praveen': 'str', (1, 2, 3): 'tuple'}
d[{1,2}]='set'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d[{1,2}]='set'
TypeError: unhashable type: 'set'
d[{1:2,2:3}]='dict'
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d[{1:2,2:3}]='dict'
TypeError: unhashable type: 'dict'
d[False]='bool'
d
{1: 'int', 12.3: 'float', (2+3j): 'complex', 'praveen': 'str', (1, 2, 3): 'tuple', False: 'bool'}
d={}
d
{}
d[1]=1
d[23]=23.3
d[3]='praveen'
d[4]=[1,2,3]
d[5]=(1,2,3)
d[6]={1,2,3}
d[7]={1:2,2:3}
d[8]=True
d
{1: 1, 23: 23.3, 3: 'praveen', 4: [1, 2, 3], 5: (1, 2, 3), 6: {1, 2, 3}, 7: {1: 2, 2: 3}, 8: True}
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[2]
4
d[1]
2
d[5]
10
d[6]
12
d[0]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d[0]
KeyError: 0
d[2]
4
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d={'praveen':98,'kumar':95,'ajay':90,'ramu':60}
d
{'praveen': 98, 'kumar': 95, 'ajay': 90, 'ramu': 60}
d[praveen]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d[praveen]
NameError: name 'praveen' is not defined
d["ramu"]
60
d.get('praveen')
98
d.get('kk')
d
{'praveen': 98, 'kumar': 95, 'ajay': 90, 'ramu': 60}
d.get('ramu','user not fount')
60
#membership operation
'ramu' in d
True
'pra' not in d
True
'kk' in d
False
#methods
d.keys()
dict_keys(['praveen', 'kumar', 'ajay', 'ramu'])
>>> d.values()
dict_values([98, 95, 90, 60])
>>> d.items()
dict_items([('praveen', 98), ('kumar', 95), ('ajay', 90), ('ramu', 60)])
>>> sorted(d)
['ajay', 'kumar', 'praveen', 'ramu']
>>> max(d)
'ramu'
>>> min(d)
'ajay'
>>> len(d)
4
>>> #methods
>>> #update
>>> d['ramu']=100
>>> d
{'praveen': 98, 'kumar': 95, 'ajay': 90, 'ramu': 100}
>>> d['kumar']=80
>>> d
{'praveen': 98, 'kumar': 80, 'ajay': 90, 'ramu': 100}
>>> #adding two elements we use update()
>>> d.update({'rahul':68,'naveen':79})
>>> d
{'praveen': 98, 'kumar': 80, 'ajay': 90, 'ramu': 100, 'rahul': 68, 'naveen': 79}
>>> d.popitem()
('naveen', 79)
>>> d.pop('rahul')
68
>>> d
{'praveen': 98, 'kumar': 80, 'ajay': 90, 'ramu': 100}
>>> #delete
>>> del d['ajay']
>>> d
{'praveen': 98, 'kumar': 80, 'ramu': 100}
>>> d['pj']=90
>>> d
{'praveen': 98, 'kumar': 80, 'ramu': 100, 'pj': 90}
>>> d.setdefault('praveen',0)
98
>>> d
{'praveen': 98, 'kumar': 80, 'ramu': 100, 'pj': 90}
>>> d.setdefault("dj",0)
0
>>> d
{'praveen': 98, 'kumar': 80, 'ramu': 100, 'pj': 90, 'dj': 0}
