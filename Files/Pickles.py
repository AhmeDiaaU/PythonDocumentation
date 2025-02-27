##pickle module 

import pickle 

data = (2021 , '4444' ,((7,'wow')) , [4,5])
lst = [1 , 251221,30000]

with open ("data.pickle" , "wb") as pickle_file :
    pickle.dump(data , pickle_file)
    pickle.dump(lst , pickle_file) # dump function take data and file and start writing data into the file in binary

"""
in other way to write in a more complex way :

with open("data.binary", "wb") as writer: # open file as writter 
    binary_format = bytearray(lst)  # must be in range(0, 256)
    writer.write(binary_format) # write after transofrming data into byte array
    str_encoded = bytearray('abc', 'utf-8') # we can change it into utf -8 which is more flexable and have wide range
    writer.write(str_encoded)


with open("data.binary", "rb") as reader:
    lst2 = list(reader.read()) # make what is imported from file to list item 
    print(lst2)     # [120, 255, 100, 97, 98, 99]
    # a integer code is 97
"""
with open("data.pickle" , "rb") as pickle_file : 
    data = pickle.load(pickle_file)
    lst = pickle.load(pickle_file)
    print(data)
    print(lst)