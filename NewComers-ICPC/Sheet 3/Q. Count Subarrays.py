test_case = int(input())
for t in range(test_case):
    No_of_digits = int(input())
    lst = list(map(int, input().split()))
    subarray = []
    count = 0
    x = 0
    n = 0
    if len(lst) == No_of_digits:
        for length in range(1, No_of_digits + 1):
            for i in range(No_of_digits - length + 1):
                x = i + length
                subarray.append(lst[i:x])
        for j in subarray:
            if j == sorted(j):
                count+=1
        print(count)
