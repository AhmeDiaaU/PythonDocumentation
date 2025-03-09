def check_odd():
    arr_length = int(input())
    arr = list(map(int , input().split()))
    if len(arr) == arr_length :
        arr = sorted(arr)
        sum_result = 0
        for i in range(len(arr)):
            if (i+1) %2 ==1 or arr[i] % 2 ==1 :
                continue
            sum_result += arr[i]
        return sum_result
print(check_odd())