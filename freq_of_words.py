a="sheena loves eating mango apple and mango , her sister loves eating mango"
li=a.split()


d={}
for i in li:
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1
print(d)










