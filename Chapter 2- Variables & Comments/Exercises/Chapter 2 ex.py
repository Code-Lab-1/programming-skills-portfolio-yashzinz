#Ex 1
x="I like reading books"
print(x)
x="I like watching anime"
print(x)
#Ex 2
print("\"Sometimes it is the people no one can imagine anything of who do the things no one can imagine.\n\t\t\t\t-Alan Turing\"")
#Ex 3
y="\tYashvi \n Zinzuadia"
print(y)
print(y.lstrip())
print(y.rstrip())
print(y.strip())
#Ex 4
x=6
message="My favorite number is:" ,x
print(message)
#Ex 5
Total_amount=50
Cost_of_each_USB_stick=6
print("Number of usb sticks the girl can buy=",Total_amount//Cost_of_each_USB_stick)
print("Amount left with her=",Total_amount%Cost_of_each_USB_stick)
#EX 6  Write a python program to read a number ,if it is an even number ,print the square of that number and if it is odd number print cube of that number.
x=int(input("Enter a number:"))
if x%2==0:
    print(x**2)
else:
    print(x**3)
#EX 7 Calculate average marks and percentage of your marks
Mathematics=96
English=94
Accountancy=84
Economics=89
Bst=85
Total_marks=Mathematics+English+Accountancy+Economics+Bst
Avg_score=Total_marks/5
print(Avg_score)
percentage=Total_marks/500*100
print(percentage)
#EX 8 calculate sum and product
a=3
a+=9
print(a)
b=a
b*=3
print(b)
#EX 9
x,y=2,6
x,y=y,x+2
print(x,y)
#EX 10 calculate the selling price
cost_price=int(input("Enter the cost price"))
profit=int(input("Enter profit:"))
selling_price=cost_price+profit
print("The selling  price is",selling_price)