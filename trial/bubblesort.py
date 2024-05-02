l = [4,3,2,5,1,8]

for i in range(len(l)):
    for j in range(0,len(l)-i-1):
        if(l[j]>l[j+1]):
            temp = l[j]
            l[j] = l[j+1]
            l[j+1]=temp

print(l)
