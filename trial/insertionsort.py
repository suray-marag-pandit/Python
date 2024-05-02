l = [4,3,2,5,1,8]

for i in range(1,len(l)):
    for j in range(i,0,-1):
        if l[j]<l[j-1]:
           l[j],l[j-1]=l[j-1],l[j]

print(l)
    