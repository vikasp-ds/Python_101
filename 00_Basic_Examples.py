# Ex01. basic for loop

fruits = ['Mango', 'Banana', 'Apple']

for fruit in fruits:
    print(fruit)
	
# Ex02. Looping through string
for x in 'Banana':
    print(x)
	
# The Break statement
# With the break statement we can stop the loop before 
# it has looped through all the items:

fruits = ['Mango', 'Banana', 'Apple']

for fruit in fruits:
    print(fruit)
	if fruit == 'Banana':
	    break
		
# Range function
# The range() function defaults to 0 as a starting value, 
# however it is possible to specify the starting value by 
# adding a parameter: range(2, 6), 
# which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
    print(x)
	
for x in range(2, 30, 3):
    print(x)
	
# Else in For Loop
# The else keyword in a for loop specifies a block of code 
# to be executed when the loop is finished:
for x in range(6):
    print(x)
else:
    print('Finally finished')

# Q. Find the area of the triangle if sides are given	
#If a, b and c are three sides of a triangle. Then,
#s = (a+b+c)/2
#area = √(s(s-a)*(s-b)*(s-c))

# Python Program to find the area of triangle
# Sides
a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)

# Q. Python Program to Convert Kilometers to Miles
kilometers = 5.5

# To take kilometers from the user, uncomment the code below
# kilometers = float(input("Enter value in kilometers"))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))

# Q. Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)


