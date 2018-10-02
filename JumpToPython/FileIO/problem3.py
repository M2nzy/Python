# problem3.py : reverse save

# data get and reverse
f = open("abc.txt",'r')
DataList = f.readlines()
DataList.reverse()
f.close()

# data save
f = open("abc.txt",'w')
f.writelines(DataList)
f.close()