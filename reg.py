import re

lst=list()
handle=open('python.txt')
for line in handle:
    line =line.rstrip()
    stuff=re.findall('[0-9]+',line)
    for i in range(len(stuff)):
        num=int(stuff[i])
        lst.append(num)

sum=0
for i in range(len(lst)):
    sum=sum+lst[i]

print(sum)
