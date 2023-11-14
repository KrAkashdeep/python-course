a=1
b=3
c=4
#condiitons

a==b
a>b
a<b
a<=b
a>=b

#if elif and else statement        -->> elif is the else if of other language

if a>b:
    print("a is greater")

elif a==b:
    print("both are equal")

else :
    print("b is greater")

if a>b and c>a:                     # -->using and in if
    print("a is greater")

if a>b or c>b:                       # -->using or in if
    print("a or c is greater than b")


