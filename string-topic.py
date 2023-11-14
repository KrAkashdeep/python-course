#stirng

x="oranges"
print(x)


#multi line strings

x=""" oranges are
orange in 
colour
"""
print(x)


#string are basically array

x="hello, world"
print(x[8]) #we can access single character like this


print(len(x)) # print thee length of string  



#to check either word present in the string or not
x="hello my name is akasheep"

print("name" in x) 
print("hi" in x)

print(x[6:18]) # to print some parts of string
print(x[:6])  # print from 0th to 6th position
print(x[6:])  # print from 6th to the last position 
print(x[-8:-2]) #print from last


x="hello world"
print(x.upper())  #print in upper 

x="hello world     "
print(x.strip())  # to remove white space

print(x.replace("h","a"))   # to replace a character

x="hello, world"

print(x.split(","))   # to split a word


#concatination of string
a="hello"
b="world"
print(a+" "+b)


#study "STRING METHOD" FROM GOOGLE FOR MORE DETAILS 
# STUDY "ESCAPE CHARACTERS" FOR MORE INFORMATION ABOUT THIS ALL