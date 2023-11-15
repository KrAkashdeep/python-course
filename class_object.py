#------------------CLASS--------------------------

# created class

class Human:
    x=5

#to print class value

#create object first

h=Human()      #--->> here " h " is the object

print(h.x)



class Human:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def methods(self):                         #--->>> methods inside class
        print("Hy my name is "+self.name )


h1=Human("akash",21)
h1.methods()


h1.name="raj"
h1.age=26
h1.methods()

#directly change name by using object

#if we delete object we can't change or modify the value using that object


#to delete object

del h1

#now this can't work e can't modify value

h1.name="raj"
h1.age=26
h1.methods()

#class not be empty if you want to create empty just write "pass"

class Human:
    pass