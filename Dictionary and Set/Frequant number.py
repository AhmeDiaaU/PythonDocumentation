n = int(input())
x = list(map(int, input("Enter Numbers: ").split()))
if len(x) == n:
    dct = dict.fromkeys(x, 0)
    for num in x :
        dct[num] +=1
    mx = max(dct.values())
    freq = [keys for keys , value in dct.items() if value == mx ]
    print(f"highest frequancy is {mx} , for values : {freq}")
