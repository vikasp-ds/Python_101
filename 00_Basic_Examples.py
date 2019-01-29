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
