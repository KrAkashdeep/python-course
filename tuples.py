#---------------------TUPLES-----------------------


# allows to store multiple types of item in single variable

# it is in round bracket

#it is ordered , unchangable, aloow duplicate 

tuple=('bike','car',3,3.5,True,'bike')
print(tuple)

#if we have one item in tuples then it will print but 
# the type of that tuples will show the types of that data type of the available in that

tuple=("akash")
print(type(tuple))  #-->> it will show type as string

#access the tuples elements at particular index

tuple=('bike','car',3,3.5,True,'bike')
print(tuple[1])

#access the tuples elements in range format

print(tuple[1:4])

#we cant add or change in tuple directly

# To  change first convert the tuples in list and change or add items

z=('bike','car',3,3.5,True,'bike')

y=list(z)
y[1]="akash"

x=tuple(y)
print(x)


