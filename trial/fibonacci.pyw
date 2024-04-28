term = int(input("Enter the term: "))

x,y=0,1
print(x,y,end=' ')

while(term>2):
    z=x+y
    print(z,end=' ')
    x=y
    y=z
    term-=1