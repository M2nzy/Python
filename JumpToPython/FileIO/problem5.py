# average
f = open("sample.txt",'r')
lines = f.readlines()
result = 0
for i in lines:
    i = i.strip()
    result += int(i)
f.close()

with open("result.txt",'w') as f:
    f.write(f'sum = {result}, average = {result / len(lines)}')