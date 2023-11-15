#-----------------------------------LAMBDA----------------------------------------

#it is also a function 
#but small and anonymous function


#SYNTAX---

# lambda arguments:expression

# any numbeer of argument but only on expression


#normal single expression using function

def f1(x):
    return x+10

print(f1(4))


# by using lambda in single expression

a=lambda x:x+10

print(a(8))




#---------------------------------MAP -------------------------------------------

#runs a function on all item in a collection 

# general way to convert all item in float

colle=[1,4,6,7,3,2]
coll2=[]

for x in colle:
    coll2.append(float(x))

print(coll2)


#use MAP function to convert all item in float

coll2=list(map(float,colle))

print(coll2)


# to double the value using lambda and map function

double=list(map(lambda x:x*2,colle))

print(double)


#------------------------------FILTER--------------------------------------------------


#run a function on all item in a collection but only store true value


age=[14,34,2,44,5,31,12,65,4,7,6,88]


adults=list(filter(lambda x:x>=18,age))

print(adults)