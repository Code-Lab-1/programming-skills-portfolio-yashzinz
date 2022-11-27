#EX 1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
#EX 2
import sys
print(sys.version)
#EX 3
import datetime
now=datetime.datetime.now()
print(now)
#EX 4
x="My name "
y="is "
z="Yashvi"
a=x+y+z 
print(a)
#EX 5
radius=int(input("Enter radius of a circle"))
area=3.14*radius**2
print("AREA OF THE CIRCLE=", area)
#Ex 6: Calculate the multiplication and sum of two numbers
a=23
b=54
print(a+b)
print(a*b)
#Ex 7 Write a program to create a new string made of an input string’s first, middle, and last character.
name="Yashvi"
print(name[0]+name[3]+name[5])
#Ex 8 Display float number with 2 decimal places using print()
x=3.6453
print("%.2f"%x)
#Ex 9 Write a program to use string.format() method to format the following three variables as per the expected output
a="park"
b="exercised"
c="noon"
print("I",f'{b}',"in the",f'{a}',"and went back by"f'{c}')
#Ex 10  Write a Python program to display the examination schedule. 
examination_schedule="25.06.2023"
print("The examination is scheduled to take place on",examination_schedule)