#Time module:
# get local time  , time / date comp 
# compute time diff between two points 

import time 
if __name__ == '__main__' :
    print(time.gmtime(0)) # print the Epoch
    print(time.localtime()) # print the time at this moment point 
    print(time.localtime().tm_hour) # print hours only 
    """we can change it as we import hours or m or s as indexes [0,1,2,3,,,,,n]"""
    print(time.time()) # number of seconds from 1970 untill now 


    """ Sleep and time difference :
    1- we can check time with this function as : 
    """
    start_time = time.time()
    for _ in range(5):
        time.sleep(1) # hang for second 
    end_time = time.time()
    time_diff = end_time - start_time
    print(time_diff)

    """From date to a formatted string : """

    tm = time.localtime()
    
