#-----------------------FOR LOOP--------------------------------------

#numbers
n=[1,5,4,3,8,12,23,41]

for x in n:
    print(x)

#string 
a="akashdeep"

for x in a:
    print(x)


# break statement in for loop
#-->> break use to break the condition at given condition 

for x in n:
    print(x)
    
    if x==8:
        break


#contine statement in for loop
#--> skip that given condition and continue 

for x in n:
    if x==8:
        continue

    print(x)


#range

for x in range(20):
    print(x)          #--> by default it print from 0 to 20 


for x in range(10,20):
    print(x)           # --->> to print from other than 0 use like this




# --------------------------WHILE LOOP----------------------------


i=1
while i<6:
    print(i)
    i+=1


#break in while loop
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

#continue in while loop
i=1
while i<6:
    i+=1
    if i==3:
        continue
    print(i)






