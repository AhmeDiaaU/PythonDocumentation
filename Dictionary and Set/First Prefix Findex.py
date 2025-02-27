n = int(input("Enter number of string : "))
db = []
for i in range(n):
    x = input("Enter Data : ")
    db.append(x)
dct = {}
for idx, value in enumerate(db):
    dct[idx] = value
num = int(input("Enter Queries number : "))
for i in range(num):
    output = []
    s = input("Enter a Query : ")
    for key in range(n):
        if s in dct[key]:
            output.append(dct[key])
    if len(output) == 0:
        print("NO items founded")
    else:
        print(output)
