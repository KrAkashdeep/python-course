#--------------------DICTIONARY--------------------


#they are unordered, changeable ,do not allow duplicate

# to declare dictionary us curly bracket { }

# we store data in form of keys and values

dictt={
    "name":"akash",
    "age":20,
    "standard":"cse",
    "fruits":["apple","mangoes"]
}
print(dictt)


print(len(dictt))   #--->> print the key value pair :->> here there is 4 pairs

x=dictt["age"]      #---->>> print the value of age
print(x)

x=dictt.get("age")   #---->>> print the value of age using get method
print(x)



# change or update value

dictt["age"]=21
print(dictt)


#use update method to change value


dictt.update({"name":"akashdeep"})
print(dictt)


#add item at end

dictt["colour"]="white"
print(dictt)


# to delete (also works in list , tuples)

#use pop method to delete

dictt.pop("colour")
print(dictt)