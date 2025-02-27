from datetime import datetime 

def hello1 (curdate = datetime.now()): # The variable will take the first value and print it it will neveer change
    print(curdate)

for i in range(10) : 
    hello1() # they are all the same 

def hello2 (curdate =None):
    if curdate is None :
        curdate = datetime.now()# assign new value evey time 
    print(curdate)

 #print all of them differently 
for i in range(10):
    hello2()