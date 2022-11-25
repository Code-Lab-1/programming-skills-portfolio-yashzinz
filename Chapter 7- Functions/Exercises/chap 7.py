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
    print("I would like a "+size+" shirt"+"and "+"\""+message+"\""+" printed on it")
make_shirt()