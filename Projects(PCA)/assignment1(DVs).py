#Write a python program to define an integer value and print the values
sam = 10
print(sam)

#Write a python program to calculate the square root of a number
import math
#printing square root of 9
print(math.sqrt(9))

#Write a python program to generate a random number between 0 and 15
import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(random.choice(list))

#taking a list of 10 numbers
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print all the elements after 5th index
print(list[4 : ])
#print all the elements before 6th index
print(list[:-5])
#printing element between 2nd and 8th index
print(list[1 : 7])

#python program to find area of a triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

#calculating the semi-perimeter
s = (a+b+c)/2

#calculating the area
area = (s*(s-a)*(s-b)*(s-c)) ** .5

#printing the area of a triangle
print("The area of a triangle is %0.2f" %area)