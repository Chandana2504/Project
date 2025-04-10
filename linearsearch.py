q=list()
user=int(input("enter the elements "))
for i in range(user):
    q.append(int(input("vals")))
print(q)
search=int(input("search element"))
for i in range(len(q)):
    if q[i]==search:
        print(search, "found at index",i+1)