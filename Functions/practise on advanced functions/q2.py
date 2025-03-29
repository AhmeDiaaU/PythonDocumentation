def myreduce(func , iterable , init = None):
    if not iterable:
     if init != None: # لو الinit مش بnone بيرجع قيمتها
        return init
     else :
        raise TypeError("reduce of empty sequence with no initial value")
    
    for item in iterable :
       if init is None:
          init = item
       else:
          init = func(init , item)
    return init

print(myreduce(max , {7 , 20 , 10}))