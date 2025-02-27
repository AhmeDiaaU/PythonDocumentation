from_str = 'abcdefghijklmnopqrstuvwxyz0123456789'
to_str = 'YZIMNESTODUAPWXHQFBRJKCGVL!@#$%^&*()'

dct = {from_str[idx]: to_str[idx] for idx in range(len(from_str))}
string = input("Enter string: ")
res = " "
for char in string :
    if char in dct :
        x = dct[char]
    res+=x
print(res)