#we write comments like this for single line comments
"""
for multiple comments we can use like this 
"""
print("hello world")


#int float complex

x=1   #int 
y=1.0  #float
z= 5j #complex

print(type(x))  #print which type of data x contain
print(type(y))
print(type(z))

#convert int to float
a=float(x)
#convert float to int
b=int(y)
#convert int to complex
c=complex(x)
print(a)
print(b)
print(c)


#math operation 
#add
d=10
e=20

f=d+e
print(f)
#OR 
print(d+e)
#all are same like this
#expo
d=2
e=2

f=d**e  #exponential 
print(f)
#floor division  is dividing one number by another and then rounding the result to the closest integer that is smaller 
d=10
e=20

f=d//e
print(f)