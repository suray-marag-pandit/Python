# for i in range (5):
#     for j in range(5):
#         print(5,end=" ")
#     print()

num = 65
for i in range(5):
    for j in range(i+1):
        print(chr(num),end=" ")
    print()
    num+=1
print('-'*60)