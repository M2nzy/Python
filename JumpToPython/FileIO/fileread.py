# fileread.py
f = open("test.txt",'r')
data = f.read() # readline(), readlines()
print(data)
f.close()