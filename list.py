#--------------------LIST----------------

#It is use to store multiple item in single variable

list=['car','bike',30,3.2,True]
print(list)

#list is in square bracket
#it is ordered ,changeable and allow duplicate

print(list[0])  #-->>print specific element from list

print(list[2:5])  #--->> print in range from list

#changes at particular index

list[2]="bus"
print(list)

# change in ranges

list[1:3]=["akash","jeep","hello"]
print(list)


#Insert at particular index

list.insert(3,"world")
print(list)

#insert or add value at end of list

list.append(4566)
print(list)