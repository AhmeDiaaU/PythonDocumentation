def count_distinct_numbers(arr):
    return len(set(arr))


n = int(input())
if n == 0 :
    print(0)
else:
    arr = list(map(int, input().split()))
    print(count_distinct_numbers(arr))
