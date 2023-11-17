#Ex 1
def display_message():
    print("I'm learning about functions and how to call them.")
display_message()

#Ex 2
def favorite_book(title):
    print(title + " is one of my favorites.")
favorite_book("Harry Potter")

#Ex 3
def make_shirt(size,message):
    print("I would like a "+ size+" size"+ " and "+"\""+message+"\""+" printed on it" )
make_shirt("large","Change is inevitable")
make_shirt(size="large",message="Change is inevitable")

#Ex 4
def make_shirt(size="large",message="I love python"):
    print("I would like a "+size+" shirt"+" and "+"\""+message+"\""+" printed on it")
make_shirt()
make_shirt(size="medium",message="I love coding")

#Ex 5
def describe_city(city,country="India"):
    print(city+" is in "+country)
describe_city("Ahemdabad")
describe_city("Pune")
describe_city("Sharjah","UAE")

#Ex 6 Create a function with variable length of arguments
def function(*arguments):
    for i in arguments:
        print(i)
function(20,30,12)
function(21,34)
function("My name is Yashvi")

#EX 7 Write a Python function to find the Max of three numbers
def max_of_num(x,y,z):
    if x>y and x>z:
        print("The greatest number from the list:",x)
    elif y>x and y>z:
        print("The greatest number from the list:",y)
    if z>x and z>y:
        print("The greatest number from the list:",z)
max_of_num(3,2,-5)

#EX 8  Write a Python function to sum all the numbers in a list.
def sum(num):
    total=0
    for x in num:
        total+=x
    return total
print(sum([1,3,5,7,9,11]))

#Ex 9  Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
def string(x):
    dict={"UPPER CASE":0,"LOWER CASE":0}
    for i in x:
        if i.isupper():
            dict["UPPER CASE"]+=1
        elif i.islower():
            dict["LOWER CASE"]+=1
        else:
            pass
    print("The no. of upper case letters=",dict["UPPER CASE"])
    print("The number of lower case letters=",dict["LOWER CASE"])
string("Harry Potter and The Goblet of Fire")

#EX 10 Python program to print the even numbers from a given list.
def even_numbers(x):
    even_num=[]
    for i in x:
        if i%2==0:
            even_num.append(i)
    return even_num
print(even_numbers([1,2,4,3,6,7,9]))        

        