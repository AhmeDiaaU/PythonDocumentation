def check_num(num):
    invalid_digits = {'2', '3', '4', '5', '7'}
    for char in num :
        if char in invalid_digits:
            return None
    rotated = ""
    for char in num:
        if char == '6':
            rotated+= '9'
        elif char == '9' :
            rotated+='6'
        else :
            rotated+=char
    return rotated[::-1]
num = input()
if check_num(num) is not None and check_num(num) == num:
    print("YES")
else :
    print("NO")
