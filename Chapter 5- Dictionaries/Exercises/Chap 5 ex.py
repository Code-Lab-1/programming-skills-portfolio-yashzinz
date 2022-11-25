#Ex 1
personal_info={"first_name":"Anantha", "last_name":"Peddeda", "age":"18", "city":"Hydrabad"}
print(personal_info)
#Ex 2
glossary={"Concatenation":"Addition of any two strings","Boolean":"A data type representing one of two possible values-True or False.","Escape sequence":"Representation of non graphic characters.","Delimiters":"Symbols that can be used as seperators of values or enclose some values.","Keywords":"Reserved words used by python interpreter to recognize the structure of a program"}
words=["Concatenation:","Boolean:","Escape Sequence:","Delimiters:","Keywords:"]
print(words[0]+'\n'+glossary["Concatenation"])
print(words[1]+'\n'+glossary["Boolean"])
print(words[2]+'\n'+glossary["Escape sequence"])
print(words[3]+"\n"+glossary["Delimiters"])
print(words[4]+"\n"+glossary["Keywords"])
#Ex 3
glossary={"Concatenation":"Addition of any two strings","Boolean":"A data type representing one of two possible values-True or False.","Escape sequence":"Representation of non graphic characters.","Delimiters":"Symbols that can be used as seperators of values or enclose some values.","Keywords":"Reserved words used by python interpreter to recognize the structure of a program",}
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