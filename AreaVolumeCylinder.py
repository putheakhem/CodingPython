'''
Write a program that reads in the radius and
length of a cylinder and computes the area and volume using the following formulas:
area = radius * radius * π
volume = area * length
'''

a, b = input("Enter the radius and length of a cylinder").split(",")
radiusCylinder = evl(a)
lengthCylinder = eval(b)
area = radiusCylinder * radiusCylinder * 3.14159
volume = area * lengthCylinder

print("The area is ", area)
print("The volume is ", volume)
