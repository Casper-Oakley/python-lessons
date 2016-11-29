#This is what a dictionary looks like

dict = {"Key1": 48, "Key2": 4092, "MyFavKey": 12}

#This prints 48
print(str(dict["Key1"]))

#This iterates through every ""KEY""
#So prints Key2 Key1 MyFavKey
for x in dict:
    print(str(x))

#you can use .values() to get a list of values
for x in dict.values():
    print(str(x))

#You can use .get(key) to get the value of a given key

print(str(dict.get("Key1")))

