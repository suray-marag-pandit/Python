import math

length = int(input("Enter the length of the triangle: "))
breath = int(input("Enter the breath of the triangle: "))

h = math.sqrt(math.pow(length,2)+ math.pow(breath,2))
perimeter = length + breath + h
area = (1/2)*breath* length

print("perimeter of the triangle is ",perimeter)
print("area of the triangle is ",area)