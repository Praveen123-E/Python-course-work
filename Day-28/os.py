'''
import os
#os.mkdir("sample")
#os.makedirs("sample/demo")
#os.rmdir("Sample")

path=os.path.join("sample/demo","demo.txt")

with open(path,'w+') as file:
    file.write("Hello World")
    file.seek(0)
    print(file.read())

#Hello World

'''

import os
import shutil
#5os.chrdir("demo")

print(os.path.abspath('main.py'))

print(os.path.exists('main.py'))

print(os.path.getsize('main.py'))
