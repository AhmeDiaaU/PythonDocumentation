def my_filter(fun , iterable : list) -> list:
    return [item for item in iterable if fun(item)]
def is_even(n):
    return n%2 == 0
res = my_filter(is_even , [1,2,3,4,5,6,7,8,9,10,13])
print(res)