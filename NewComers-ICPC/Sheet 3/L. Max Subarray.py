test_case = int(input())
for t in range(test_case):
    No_of_digits = int(input())
    lst = list(map(int, input().split()))
    subarray = []
    if len(lst) == No_of_digits:
        for length in range(1, No_of_digits + 1):
            for i in range(No_of_digits - length + 1):
                subarray.append(lst[i:i + length])
        for i in subarray:
           print(max(i), end=" ")
        print()