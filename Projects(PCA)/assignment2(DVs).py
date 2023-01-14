#Write a python program to define an integer value and print the values.
sam = 10
print(sam)

#2.Write a python program to find addition of two integer numbers taken as input from the user.
x = input("Enter first integer:")
y = input("Enter second integer:")
#addition of two integer
sum = int(x) + int(y)
print(sum)

#3.Write a python program to check the given year is a leap year or not.
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0) & (year % 100 != 0):
    print("Year is leap year")
else:
    print("Year is not leap year")

#4.Write a python program for swapping the value of two integers.
p = int(input("Enter value for P:"))
q = int(input("Enter value for Q:"))
#for swapping using a thrid variable'r'
r = p
p = q
q = r
print("The value of P after swapping :", p)
print("The value of Q after swapping :", q)

#5.Write a python program for swapping the value of two integers without a third variable.
p = int(input("Enter value for P:"))
q = int(input("Enter value for Q:"))
p, q = q, p
print("The value of P after swapping :", p)
print("The value of Q after swapping :", q)

#6.Write a python program to find the ASCII value of the given character.
ascii = str(input("Enter a character to find ASCII value:"))
print("The ASCII value of '" + ascii + "' is", ord(ascii))

#7.Write a python program to calculate the square root of a number.
import math
num = int(input("Enter a number: "))
print(math.sqrt(num))

#8.Write a python program to generate a random number between 0 and 15.
import random
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(random.choice(list))

#taking a list of 10 numbers
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print all the elements after 5th index
print(list[4 : ])
#print all the elements before 6th index
print(list[:-5])
#printing element between 2nd and 8th index
print(list[1 : 7])

#10.python program to find area of a triangle
a = float(input("Enter the first side:"))
b = float(input('Enter the second side:'))
c = float(input("Enter the third side:"))
#calculating the semi-perimeter
s = (a+b+c)/2
#calculating area
area = (s*(s-a)*(s-b)*(s-c)) ** .5
print("The area of a triangle is %0.2f"%area)

#11.Write a python program to create a list with n number of items
#(where n should be at least 6) with different types
list1 = [1, 2, 1.2, 2.1, "souvik", "adhikary"]
#a.Count the length of the list
print(len(list1))

#b.Access the last element in the list using negative indexing.
print(list1[-1])

#c.Add one item to a list using the append()method.
list1.append("arch")
print(list1)

#d.Add several items using the extend()method.
list2 = ["data", "science"]
list2.extend(list1)
print(list2)

#e.Add a list as an item to the existing list (nested list).
nested_list = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
new_list = nested_list + list1
print(new_list)

#f.Use the index operator to access the items at various location within the list.
#accessing the list1 5th element
print(list1[4])
#accessing the list2 2nd element in reverse way
print(list2[1])
#accessing the nested_list "eee"
print(nested_list[2][2][0])

#g.Add an element to the list at the specified index using insert() method.
#adding string "MAKAUT" in index no. 0 in nested_list
nested_list.insert(0, "MAKAUT")
print(nested_list)

#h.Replace an existing element from the list at a specified location.
#replacing the nested_list 0 index "MAKAUT" to "assignment"
nested_list[0] = "assignment"
print(nested_list)

#i.Add duplicate elements to the list.
res = []
res.extend([3 for i in range(10)])
print ("The filtered list is : " + str(res))

#j.Remove the item at the given index from the list using pop() method.
#removing item from list1 5th element
list1.pop(4)
print(list1)

#k.Sort the elements of the given list in a specific ascending or descending order.
#for ascending order
num_list = [11, 24, 35, 45, 56, 69, 73, 82, 97]
num_list.sort(reverse = False)
print(num_list)
#for descending order
num_list.sort(reverse = True)
print(num_list)

#l.Reverse the elements of the list using reverse() method.
num_list = [11, 24, 35, 45, 56, 69, 73, 82, 97]
#for reversing
num_list.sort(reverse = True)
print(num_list)

#12.Write a python program to print all the prime numbers between 1 to 1000 using loop.
num_start = 1
num_end = 1000
print ("The Prime Numbers in the range are: ")  
for number in range (num_start, num_end + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)

#13.Write a python program to print the Fibonacci series.
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b

#14.Write a python code to print the following:
print("     *")
print("   *****")
print("  *******")
print(" *********")
print("***********")
print(" *********")
print("  *******")
print("   *****")
print("     *")

#sorry for not implementing loop method