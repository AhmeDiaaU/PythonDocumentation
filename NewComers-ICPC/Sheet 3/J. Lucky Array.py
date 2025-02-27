no_element = int(input())
lst = list(map(int, input().split()))
counter = 0
mini = 625321373265468454510512
if len(lst) != no_element:
    exit(1)
else:
    for i in lst:
        if mini > i:
            mini = i
    for count in lst:
        if count == mini:
            counter += 1
    if counter % 2 == 0:
        print("Unlucky")
    else:
        print("Lucky")
