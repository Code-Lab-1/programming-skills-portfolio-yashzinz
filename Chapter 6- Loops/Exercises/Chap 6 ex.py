#EX 1
while True:
    pizza_toppings=input("what would you like on your pizza?")
    if pizza_toppings=="quit":
        print("Your order is complete")
        break
    else:
        print("Will add",pizza_toppings,"to your pizza")
#EX 2
while True:
    age=int(input("Enter your age:"))
    if age<3:
        print("Your ticket is free of cost")
    elif age>=3 & age<=12:
        print("Your ticket is $10")
    elif age>12:
        print("Your ticket is $15")
    break
#Ex 3
i=12
while i>11:
    print(i)
#Ex 4
sandwich_orders=["Nutella sandwich","Cheese sandwich","Veggie sandwich","Mushed potato sandwich","Ham sandwich"]
finsihed_sandwiches=[]
for i in sandwich_orders:
    print("I made your",sandwich_orders)
    finished_sandwiches.append[sandwich_orders]