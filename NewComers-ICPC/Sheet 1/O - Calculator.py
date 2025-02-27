equ = str(input())
for i in range(0, len(equ)):
    if equ[i] == '+' or equ[i] == '-' or equ[i] == '*' or equ[i] == '/':
        indexoperator = i
        oper = equ[i]
n1 = equ[0:indexoperator]
n2 = equ[indexoperator + 1:]
# print(indexoperator ," " , oper)
# print(n1)
# print(n2)
n1 = int(n1)
n2 = int(n2)
if oper == '+':
    result = n1 + n2
    print(result)
elif oper == '-':
    result = n1 - n2
    print(result)
elif oper == '*':
    result = n1 * n2
    print(result)
elif oper == '/':
    if n2 == 0:
        print("U cant divide by 0 ")
        False

    result = n1 // n2
    print(result)
else:
    print(f"{oper} is invalid operator")