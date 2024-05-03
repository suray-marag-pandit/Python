# class myname:
#     x=10

# m = myname()

# print(m.x)

# class node:
#     def __init__(self,data,next):
#         self.data = data
#         self.next = next
#     def __str__(self):
#         return f"{self.data} and {self.next}"
        
# head = node(10,None)

# # print(head.data,head.next)
# # print(head)

# head2 = node(20,None)
# head.next=head2

# print(head.next.data)


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname,self.lastname)

# x = Person("suray","marag")
# x.printname()


# class child(Person):
#   pass

# child("s","m").printname()

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)
# print(myiter)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# import platform

# print(platform.system())
# print(dir(platform))


import datetime

x = datetime.datetime.now()
print(x)