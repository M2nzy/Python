# adddata.py
f = open("test.txt",'a')
for i in range(11,21):
    data = "%d 번째 줄\n" % i
    f.write(data)   
f.close()