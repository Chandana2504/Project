import array as arr
a=arr.array('i',[])
length_of_array=int(input("enter length"))
for i in range(length_of_array):
    x=int(input("enter value"))
    a.append(x)

print(a)
val=int(input("which value"))
t=0
for e in a:
    if e==val:
        print(t)
        break
    t+=1
print(a[2])

