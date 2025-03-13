def f():
    return 1,2,3

a , b, c = f() # ==> each vale will be in a variable
together = f() # ==> this will return value in a tuple
#we can unpack it by ==> 
together  = a , b, c



#_______________________________________________

#No return function 

# we cant print a function thatt doesnt contain return 

def f1():
    print(1)

print(f1()) # it will return N 