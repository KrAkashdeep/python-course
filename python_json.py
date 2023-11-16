#---------------PYTHON JSON -----------------------------------

#json -->>> Javascript object notation

#commonly use to transmit and receive data b/w server and web application in json format

#json file was written in the dictionary format of python

#it have key and value pair and some key have value in dictionary format


# import json

# person='{"name":"akash","language":["english","hindi"] }'


# per_dict=json.loads(person)

# print(per_dict)

# print(per_dict['language'])


# ---------------PRINT DATA FROM OTHER JSON FILE------------------------------


# import json

# with open("data.json")as f:
#     data=json.load(f)

# print(data)                  #--->>it will print data in single line from the file data.json 

# print(json.dumps(data,indent=4,sort_keys=True))



# import json

# person={"name":"akash","language":"hindi"}

# pr_json=json.dumps(person)

# print(pr_json)


"""
dictionary
list
tuples
string
int 
float
boolean
none
"""
# this type of data can be converted to json


#--------------add data in json format--------------------------


import json

person={
  "name": "akashdeep",
  "age": 20,
  "sub": "pyton",
  "class": "CSE",
  "year": "3rd"
}

with open('person.txt','w') as json_file:
    json.dump(person,json_file)