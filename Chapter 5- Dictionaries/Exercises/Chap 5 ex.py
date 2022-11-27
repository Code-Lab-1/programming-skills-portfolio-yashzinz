#Ex 1
personal_info={"first_name":"Anantha", "last_name":"Peddeda", "age":"18", "city":"Hydrabad"}
print(personal_info)

#Ex 2
glossary={"Concatenation":"Addition of any two strings"
,"Boolean":"A data type representing one of two possible values-True or False."
,"Escape sequence":"Representation of non graphic characters."
,"Delimiters":"Symbols that can be used as seperators of values or enclose some values."
,"Keywords":"Reserved words used by python interpreter to recognize the structure of a program"}
words=["Concatenation:","Boolean:","Escape Sequence:","Delimiters:","Keywords:"]
print(words[0]+'\n'+glossary["Concatenation"])
print(words[1]+'\n'+glossary["Boolean"])
print(words[2]+'\n'+glossary["Escape sequence"])
print(words[3]+"\n"+glossary["Delimiters"])
print(words[4]+"\n"+glossary["Keywords"])

#Ex 3
glossary={"Concatenation":"Addition of any two strings",
"Boolean":"A data type representing one of two possible values-True or False.",
"Escape sequence":"Representation of non graphic characters."
,"Delimiters":"Symbols that can be used as seperators of values or enclose some values."
,"Keywords":"Reserved words used by python interpreter to recognize the structure of a program"
,"for loop":"The for loop is used to iterate over a given sequence, such as lists or strings."
,"Functions":"A function is a group of related statements that performs a specific task."
,"String Formatting":"Strings have a format() function, which enables values to be embedded in it, using placeholders."
,"List Slices":"List slices allow you to get a part of the list using two colon-separated indices." 
,"Iteration":"The code in the body of a while loop is executed repeatedly while the condition is True.This is called iteration."
}
for key, values in glossary.items():
    print(key+":"+"\n"+values)

#Ex 4
Rivers={"Ganga":"India", "Amazone":"South America","Thames":"London" }
print("\n".join(f'The {keys} runs through {values}.'
             for keys, values in Rivers.items()))
for river in Rivers.keys():
    print(river)
for country in Rivers.values():
    print(country)

#Ex 5
pet_1={"name":"Ginney","type":"Dog","owner":"Yashvi"}
pet_2={"name":"Maris","type":"Cat","owner":"Jash" }
pet_3={"name":"Goldie","type":"Gold fish","owner":"Khushi"}     
pet_4={"name":"Bitto","type":"Parrot","owner":"Anantha"}
pet_5={"name":"Athena","type":"Canery","owner":"Rithisha"}
pets=[pet_1,pet_2,pet_3,pet_4,pet_5]
print("\n".join(pet["name"]+" is a "+pet["type"]+", owned by "+pet["owner"]
 for pet in pets))

 #EX 6 Changing value in Nested list
records={
    "person1":{"name":"Anantha","salary":"20,000"},
    "person2":{"name":"Rithisha","salary":"28,000"},
    "person3":{"name":"Sneha","salary":"30,000"}
}
records["person3"]["salary"]="23,000"
print(records)

#EX 7 Python program to find the sum of all items in a dictionary
nums={"x":189 ,"y":123, "z":342,"w":145}
sum=0
for values in nums.values():
    sum+=values
print(sum)
#EX 8 Poll for favorite language
candidates={"Ryan":"Python",
"Joshua":"C",
"Roshini":"Java",
"Rihana":"C#",
"Lana":"Python"
}
for keys,values in candidates.items():
    print(keys+"'s favorite programming language is "+values)
coders=["Rithisha","Ryan","Joshua","Sneha","Anantha","Roshini","Rihana","Lana"]
for coder in coders:
    if coder in candidates.keys():
        print("Thank you for taking the poll, " + coder + "!")
    else:
        print(coder+ ", what's your favorite programming language?")


#Ex 9 People info stored in a dictionary
person1={"name":"Yashvi", "Occupation":"Student","Age":"18"}
person2={"name":"Anantha", "Occupation":"Doctor","Age":"26"}
person3={"name":"Sneha", "Occupation":"Developer","Age":"18"}
info=[person1,person2,person3]
for i in info:
    print(i["name"]+" is a "+i["Age"]+" year old "+i["Occupation"])


#EX 10 Create a dictionary by extracting the keys from a given dictionary
Dict = {"name":"Yashvi", "Occupation":"Student","Age":"18"}
list=["name","Occupation"]
new_dict={x:Dict[x] for x in list}
print(new_dict)

