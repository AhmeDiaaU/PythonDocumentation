def nth_fibonacci(n):
    """_summary_

    Args:
        n (_type_): postion of the fibonacci
        to get fibonacci : sum of the last 2 numbers
        start with 0
        [0,1]
        we add last 2 values in the array then we append it to the list
        we add counter to get position of n 

    """
    first_value =0
    second_value = 1 
    lst =[first_value , second_value]
    for i in range(n):
       fibonacii = lst[-1]+lst[-2]
       lst.append(fibonacii)
    return lst[n-1]
for i in range(1,10): 
    print(i , nth_fibonacci(i))
