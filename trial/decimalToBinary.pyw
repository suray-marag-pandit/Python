n = int (input("Enter the number: "))

a,m,c=0,0,1

while(n>0):
    a = n%2
    m = m+ (a*c)
    c=c*10
    n=int(n/2)


print(m)