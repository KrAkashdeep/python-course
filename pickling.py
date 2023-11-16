#------------------------PICKLING------------------------------

#it is module 
#use for serialize and deserialize data
#convert data
#use to read or write data in byte format 

import pickle

mydict={'1':'a','2':'b','3':'c'}
pickle_file=open("picklefile.txt","wb")
pickle.dump(mydict,pickle_file)


pickle_file=open("picklefile.txt","rb")
new_dict=pickle.load(pickle_file)
print(new_dict)