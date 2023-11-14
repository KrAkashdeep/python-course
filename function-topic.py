# --->> to define function we use def keywords before writing function name 

# -->> created function 

def trailfunction():
    print("hello world")


# -->> calling the function like this 

trailfunction()


# --->> passing argument to function 

def trailfunction(x):   #-->> in defined / created function value is called parameter
    print(x+" world")

trailfunction("hello")   #-->> function called and value pass from here is called argument


#-->>multiple arguments

def trial(x,y):
    print(x+" "+y)

trial("Hello "," Akash")  #--> the first value is for x and second for y 
                          #--->> if we give or pass one value gives error


#function as argument

list=['car ','bus ','bike ']

def loop(x):
    print(x*3)           #--->>it will print that value three times

loop(list)


def map_func(crazy,list):
    for item in list:
        crazy(item)


map_func(loop,list)