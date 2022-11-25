#Class ex 1
i=["apple","Banana","Car","Dolphin"]
for x in i:
    print("The following lines will print each letter of",x)
    for y in x:
        print(y)
#Class ex 2-sum of all the values in a list
num=[1,4,7,2,3,8]
sum=0
for i in num:
    sum=sum+i
    print("The sum is", sum)
#Class ex 3
books=["Harry Potter","Percy Jackson","The shadow Hunters"]
for i in range(len(books)):
    print("I like",books[i])
#Class ex 4
digits = [0, 1, 5,45,67,34,28,53,57,98,65,22,56,67,43,23,84,59]
for i in digits:
    print(i)
else:
    print("No items left.")
