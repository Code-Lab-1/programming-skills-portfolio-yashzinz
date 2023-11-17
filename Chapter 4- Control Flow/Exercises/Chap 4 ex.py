#Ex 1
alien_color="green"
if alien_color=="green":
    print("You earned 5 points")
alien_color="red"
if alien_color=="green":
    print("You earned 5 points")
#Ex 2
alien_color="green"
if alien_color=="green":
    print("You earned 5 points")
else:
    print("You earned 10 points")
alien_color="red"
if alien_color=="green":
    print("You earned 5 points")
else:
    print("You earned 10 points")
    
#Ex 3
alien_color="green"
if alien_color=="green":
    print("you earned 5 points")
elif alien_color=="yellow":
    print("You earned 10 points")
elif alien_color=="red":
    print("You earned 15 points")
alien_color="yellow"
if alien_color=="green":
    print("you earned 5 points")
elif alien_color=="yellow":
    print("You earned 10 points")
elif alien_color=="red":
    print("You earned 15 points")
alien_color="red"
if alien_color=="green":
    print("you earned 5 points")
elif alien_color=="yellow":
    print("You earned 10 points")
elif alien_color=="red":
    print("You earned 15 points")
#Ex 4
age=34
if age<2:
    print("You are a baby")
elif age==2 or age<4:
    print("You are a toddler")
elif age==4 or age<13:
    print("You are a kid")
elif age==13 or age<20:
    print("You are a teenager")
elif age==20 or age<65:
    print("You are an adult")
else:
    print("You are an elder")
#Ex 5
favorite_fruits=["orange","mango","apple"]
if "orange" in favorite_fruits:
    print("You really like oranges")
if "banana" in favorite_fruits:
    print("You really like bananas")
if "mango" in favorite_fruits:
    print("You really like mangoes")
if "water melon" in favorite_fruits:
    print("You really like water melons")
if "apple" in favorite_fruits:
    print("You really like apples")
#Ex 6 Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
for x in range(1500,2700):
    if x%7==0 and x%5==0:
        print(x)
#Ex 7 A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.
salary=int(input("Enter your salary:"))
years=int(input("Enter the number of years you have worked:"))
bonus=salary*5/100
if years>5:
    print("Thank you for your services, here's your bouns",bonus)
else:
    print("Sorry, unfortunately you will not receive a bonus.")
#EX 8 Take input of age of 3 people by user and determine oldest and youngest among them.
age1=int(input("Enter the age of person 1:"))
age2=int(input("Enter the age of person 2:"))
age3=int(input("Enter the age of person 3:"))
if age1>age2 and age1>age3 and age2<age3:
    print("Person 1 is oldest and Person 2 is youngest")
if age1>age2 and age1>age3 and age3<age2:
    print("Person 1 is oldest and Person 3 is youngest")
elif age2>age1 and age2>age3 and age1<age3:
    print("Person 2 is oldest and Person 1 is youngest")
elif age2>age1 and age2>age3 and age3<age1:
    print("Person 2 is oldest and Person 3 is youngest")
elif age3>age2 and age3>age1 and age1<age2:
    print("Person 3 is oldest and Person 1 is youngest")
elif age3>age2 and age3>age1 and age2<age1:
    print("Person 3 is oldest and Person 2 is youngest")
#EX 9 Class attendance
held=int(input("Number of classes held:"))
attn=int(input("Number of classes attended:"))
percentage=(held/attn)*100
if percentage>75:
    print("You cannot take the exam")
else:
    print("You can take the exam.")
#EX 10 Discount on purchase
quantity=int(input("Enter quantity:"))
cost=quantity*50
discount=cost*5/100
if cost>=1000:
    print("You have received a discount on your purchase:",discount)
    print("Your total bill is:",cost-discount)
else:
    print("Your total bill is",cost)
