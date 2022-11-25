#Ex 4
sandwich_orders=["Nutella sandwich","Cheese sandwich","Veggie sandwich","Mushed potato sandwich","Ham sandwich"]
finished_sandwiches=[]
for i in sandwich_orders:
    print("I'm making your",i)
finished_sandwiches=sandwich_orders
for x in finished_sandwiches:
    print("Your",x,"is ready")
#EX 5
sandwich_orders=["pastrami sandwich","Nutella sandwich","pastrami sandwich","Cheese sandwich","Veggie sandwich","Mushed potato sandwich","Ham sandwich","pastrami sandwich"]
finished_sandwiches=[]
print("Unfortunately, we've run out of pastrami sandwich.")
while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")
for i in sandwich_orders:
    print("I'm making your", i)
finished_sandwiches=sandwich_orders
for x in finished_sandwiches:
    print("Your",x,"is ready.")
