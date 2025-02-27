def Get_Keys_from_value(dct,val):
    return[k for k , v in dct.items() if val == v]# return key if the value is founded in the dct 


def From_Decimal_To_BaseX(num:int, base:int,dct:dict):
    result = []
    while num > 0 :
        reminder = num%base
        if reminder >= 10 :
           key = ''.join(Get_Keys_from_value(dct,reminder))
           result.append(key)
        else:
            result.append(reminder)
        num //= base
    return result[::-1]


def From_BaseX_To_Decimal(num, base,dct:dict):
    converted_number = 0
    for idx , char in enumerate(num[::-1]):
        if char.isdigit():
            value = int(char)
        else :
            value = dct[char.upper()]
        converted_number += value * (base**idx)
    return converted_number

t = int(input())
num , base = input().split()
base = int(base)
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dct = {chars[idx]:numbers[idx] for idx in range(len(chars))}

if t == 1 :
    print(From_BaseX_To_Decimal(num, base,dct))
elif t == 2 :
    number = From_Decimal_To_BaseX(int(num) , int(base) ,dct)
    s = ''.join(str(x) for x in number)
    print(s)

        