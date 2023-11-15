
#---------------------LIST COMPREHENSION--------------------------------

#offer smaller line of code to create new list using existing list

# General way to use or create new list

fruit=["apple","kiwi","mangoes","banana"]
newfruit=[]

for x in fruit:
    if "a" in x:

     newfruit.append(x)  #--->> it will add all item from fruit list who have "a" present in newfruit list

print(newfruit)


#use LIST COMPREHENSION for adding item

newfruit=[x for x in fruit if "i" in x]   #-->>  it will add all item from fruit list who have "i" present in it using list comprehension
print(newfruit)


# to remove from list

newfruit=[x for x in fruit if x!="kiwi"]  # to remove certain item from list here "kiwi" is remove from list and add in newfruit list
print(newfruit) 


newfruit=[x.upper() for x in fruit] #--->>> print in upper case and add item in newfruit list
print(newfruit) 


#to replace item with other

newfruit=[x if x!="kiwi" else "orange"for x in fruit ]
print(newfruit) 
