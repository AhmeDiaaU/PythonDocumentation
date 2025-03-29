def myreduce(func1_overall , func2_overall , iterable ):
    try :
        first , second , *iterable = iterable
        res = func2_overall(first , second)
    except:
        return RuntimeError("The iterable should have at least two elements")
    
    while iterable:
        try:
            first , second , *iterable = iterable
        except:
            return RuntimeError("number must be even")
        res = func1_overall(res , func2_overall(first , second))
    return res

print(myreduce(lambda x , y : x * y , lambda x , y : x + y , [2,5,3,4,5,10])) 
