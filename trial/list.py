# l = [1,2,3,4]
# print(l)


# fruits = ["apple", "banana", "cherry", "mango","kiwi"]
# fruits.sort()
# print(fruits)
# newlist = [s[0] for s in fruits if 'a' in s]

# print(newlist)

# i = [x for x in range(10)]
# print(i)

# print([x if x != "apple" else "orange" for x in fruits])

# l = [x for x in range(100) if x%2==0 ]
# l = [x if x%2==0 else 'x' for x in range(10)]
# newlist = [expression for item in iterable if condition == True]
# l = [ x  for x in range(100) if x%2==0 ]

# print(l)
# l = [x**2 for x in range(25)]
# print(l)

# array = list(input("Enter the string: "))
# print(array)

# l = [x for x in range(10)]
# number = int(input("Enter the number: "))
# print(l+[number])

# l = [x for x in range(10)]
# # l2 = l.copy()
# l2 = l[:]
# print(l2)



# size = int(input("Enter the number of elements in the list: "))
# l = []

# for i in range(size):
#     value = input("Enter the value: ")
#     l.append(value)

# print("The original list is: ", end="")
# print(", ".join(l))

# try:
#     l = [int(x) for x in l]
# except ValueError:
#     print("Error: The list must contain only numbers.")
#     exit(1)

# if size < 2:
#     print("Error: Need at least two elements to find the second largest.")
# else:
#     if l[0] > l[1]:
#         max1, max2 = l[0], l[1]
#     else:
#         max1, max2 = l[1], l[0]

#     for j in l[2:]:
#         if j > max1:
#             max2 = max1
#             max1 = j
#         elif j > max2:
#             max2 = j

#     print("The second largest number is:", max2)


# l = ["Monday", 1, "Tuesday", 2, "Wednesday", 3, "Thursday", 4, "Friday", 5, "Saturday", 6, "Sunday", 7]
# list1,list2=[],[]
# for i in l :
#     # if type(i)==str:
#     if i%2==0:
#         list1.append(i)
#     else:
#         list2.append(i)

# print(list1)
# print(list2)



# various operations in the list program


# <-------------------------------------------------------------------------------------------------------------------------------->


def display_menu():
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Append another list")
    print("4. Modify an element")
    print("5. Delete an element at position")
    print("6. Delete an element with value")
    print("7. Sort the list (Ascending)")
    print("8. Sort the list (Descending)")
    print("9. Display the list")
    print("10. Exit")


# list1 = [1,2,3,4,5]
# choice = 0

# while True:
#     display_menu()

#     choice = int(input("Enter the choice: "))
#     if choice==1:
#         temp = int(input("Enter the element: "))
#         list1.append(temp)
        
#     elif choice==2:
#         temp = int(input("Enter the element: "))
#         index = int(input("Enter the index: "))
#         list1.insert(index,temp)
#     elif choice==3:
#         temp = input("Enter the list: ").split(",")
#         temp2 = [int(x) for x in temp]
        
#         list1.extend(temp2)
#     elif choice==4:
#         temp = int(input("Enter the element to modify: "))
#         temp2 = int(input("Enter the new element to modify: "))
#         list1[list1.index(temp)]=temp2
#     elif choice==5:
#         temp = eval(input("Enter the position: "))
#         del list1[temp]
#     elif choice ==6:
#          temp = int(input("Enter the position: "))
#          del list1[list1.index(temp)]
#     elif choice ==7:
#          list1.sort()
#     elif choice == 8:
#         list1.sort(reverse=True)
#     elif choice == 9:
#         print(list1)
#     elif choice ==10:
#         exit()
    
    
# l = [10 for x in range(10)]
# l.append(1)
# print(l.count(1))

# mixed_numbers = [-15, -13, -11, -9, -7, -5, -3, 2,4,5,6,8,-1, 1, 3, 5, 7, 9, 11, 13]


# # for i in mixed_numbers:
# #     if i < 0 or i%2!=0:
# #         mixed_numbers.remove(i)
# print(len(mixed_numbers))
# print(mixed_numbers.index(11))


# l = [1,2,3,4,1,5,1]

# number = eval(input("Enter the number: "))
# count=0
# for i in l:
#     if i==number:
#         count+=1    

# print(count)


l =list(eval(input("Enter the elements: ")))
print(l)