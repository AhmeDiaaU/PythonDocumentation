import shelve   
data = (2021 , '4444' ,((7,'wow')) , [4,5])
lst = [1 , 251221,30000]

# file is opened for reading and writing 
with shelve.open('data.shelve' ) as shelf :
    shelf['data'] = data 
    shelf['lst'] = lst
    # its like dictionary 
    # key must be string 

# reading : 
 
with shelve.open("data.shelve" , "r") as shlf :
    for key in shlf.keys(): # make object iterate over all keys 
        print(key , shlf[key]) # return all data from shelf as in dictionary by using keys 


#updating shelve 

with shelve.open('data.shelve') as shelf :
    shelf['data_customer'] = data
    shelf ['numbers'] = lst
