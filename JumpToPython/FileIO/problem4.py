# data modify
f = open("test.txt",'r')
data = f.read()
data = data.replace("java","python") # java -> python
f.close()

f = open("test.txt",'w')
f.write(data)
f.close()