'''
1.import

import logic
print(logic.add(3,4))
print(logic.sub(3,4))
print(logic.mul(3,4))
print(logic.div(3,4))
print(logic.mod(3,4))
print(logic.exp(3,4))

7
-1
12
0.75
3
81

2.allias name

import logic as lg
print(lg.add(3,4))
print(lg.sub(3,4))
print(lg.mul(3,4))
print(lg.div(3,4))
print(lg.mod(3,4))
print(lg.exp(3,4))

7
-1
12
0.75
3
81

3.directly import functions

from logic import add,sub,mul

print(add(3,4))
print(sub(3,4))
print(mul(3,4))

7
-1
12



from logic import *

print(add(3,4))
print(sub(3,4))
print(mul(3,4))
print(div(3,4))
print(mod(3,4))
print(exp(3,4))

7
-1
12
0.75
3
81

'''























