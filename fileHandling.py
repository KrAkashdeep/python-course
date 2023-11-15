#-------------- FILE HANDLING-------------------------

#to access a file use open function like this open()

#there are four types of modes (primary modes) 


# 1. read(r)  2. write(w)  3. create(x)  4. append(a)



#to open the file in "READ" mode


f=open("trial.txt","r")

#1st one is file location or file name to open  
# 2nd is the mode in which file have to be open  


print(f.read())   #-->> to read that file and print all data from files

print(f.read(20))  # --->> it will print data till 20 character 


# to print in line 


print(f.readline()) # to print 1st line 

print(f.readline()) # to print 2nd line 

print(f.readline(5)) # to print 3rd line  till 5th character



# to print all line using for loop

for x in f:
    print(x)

# after use file close the file 

f.close() 


#-----------ADD LINE IN FILE -----------------------------


y=open("trial.txt","a")        #--->>> open file in append mode to write in exsisting file

y.write("a new line is added from outside ")    #--> add text in the file 

y.close()


# close the file in append mode and open in read mode for check and print

y=open("trial.txt","r")
print(y.read())
y.close()


#----------------WRITE MODE------------------------------

#all data present in file are replace by new line that are given



f=open("trial.txt","w")
f.write("new line from write mode")
f.close()

#close file in write mode and open in read mode to check the output

f=open("trial.txt","r")
print(f.read())
f.close()




#--------------------CREATE NEW FILE ---------------------------------


f=open("new.txt","x")  # --->> it will create new file using create a new file (x is use for create)


# we can use write mode to create new file


f=open("newfile.txt","w")



#----------------------delete file---------------------------- 


import os

os.remove("new.txt")



#delete file using if else


import os

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")

else: print("file is not present")

