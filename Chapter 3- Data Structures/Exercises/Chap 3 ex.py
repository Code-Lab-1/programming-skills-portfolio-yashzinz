#Ex 1
friends=["Anantha","Sneha","Rithisha","Emaan"]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
#EX 2 
print("I'm Yashvi's friend,", friends[0])
print("I'm Yashvi's friend,", friends[1])
print("I'm Yashvi's friend,", friends[2])
print("I'm Yashvi's friend,", friends[3])
#Ex 3
sports_car=["Toyota GR86","Toyota Supra","Chevy Camaro","Ford Mustang","Chevy Corvette","Porsche 718 Cayman"]
print("I would like to own a",sports_car[0])
print("I would like to own a",sports_car[1])
print("I would like to own a",sports_car[2])
print("I would like to own a",sports_car[3])
print("I would like to own a",sports_car[4])
print("I would like to own a",sports_car[5])
#Ex 4
Guest_list=['Alan Turing','Anantha','Agatha Christie']
print("I would like to cordially invite Mr",Guest_list[0],"for dinner")
print("I would like to cordially invite Ms",Guest_list[1],"for dinner")
print("I would like to cordially invite Ms",Guest_list[2],"for dinner")
# EX 5
print("Unfortunately",Guest_list[2],"can not make it to the dinner")
Guest_list[2]="Rick Jordan"
print("I would like to cordially invite Mr",Guest_list[0],"for dinner")
print("I would like to cordially invite Ms",Guest_list[1],"for dinner")
print("I would like to cordially invite Mr",Guest_list[2],"for dinner")
#Ex 6
print("Due to lack of dinning furniture, I will only be able to invite",Guest_list[0],"and", Guest_list[1])
print("Sorry Mr",Guest_list[2],"unfortunately, due to lack of dinning furniture, I won't be able to invite you for dinner")
Guest_list.pop(2)
print(Guest_list)
print("I would like to cordially invite Mr",Guest_list[0],"for dinner")
print("I would like to cordially invite Ms",Guest_list[1],"for dinner")
del Guest_list[0]
del Guest_list[0]
print(Guest_list)
#Ex 7
places=["Peru","South Korea","Japan","Canada","France"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
#Ex 8 sum of all numbers in a list
num=[12,46,78,10,76]
sum=num[0]+num[1]+num[2]+num[3]+num[4]
print("The sum of all numbers in the list=", sum)
#EX 9 create a list of even numbers and another list of odd numbers from a given list
num=[12,87,23,76,100,116,10,67]
even_numbers=[]
odd_numbers=[]
for x in num:
    if x%2==0:
        even_numbers.append(x)
    else:
        odd_numbers.append(x)
print("The even numbers are:", even_numbers)
print("The odd numbers are:", odd_numbers)
#Ex 10  check if the grocery items are listed in the list
grocery_items=["eggs","milk","chocolate","oil","olives"]
print("bread" in grocery_items)
print("chocolate" in grocery_items)
print("broccali" in grocery_items )