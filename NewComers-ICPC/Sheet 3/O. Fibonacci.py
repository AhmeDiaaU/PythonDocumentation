def fibonacci (n):
    lst=[]
    num1 = 0
    num2 = 1
    result = 0
    for i in range(n):
        lst.append(num1)
        result = num1+num2
        num1 = num2
        num2 = result
    return lst[n-1]
n = int(input())
print(fibonacci(n))
