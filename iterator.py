
#-------------------------------ITERATOR---------------------------------------

#iterator       iterable --->>list , tuples, dictionary


tuple1 =("car","bus","train")

myit= iter(tuple1)

print(next(myit))
print(next(myit))
print(next(myit))

#iterator works on tuples,list,dictionary, string

tuple1="apples"
myit= iter(tuple1)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
                        #--->don't excced the length of string or tuples,list.... it will give error stopIteration


#using for loop iterate

tuple1 =("car","bus","train")

for x in tuple1:
    print(x)


#iterator in class

class MyNumber:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a+=1
        return x
    

myclass=MyNumber()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))      #--> it will print number 