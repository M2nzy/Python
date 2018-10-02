# problem2.py : file save
import os

data = input("저장할 내용 입력 >>> ")

if not os.path.exists("test.txt"):
    f = open("test.txt",'w')
    f.write(data)

else:
    f = open("test.txt",'a')
    f.write(data)
    
f.close()