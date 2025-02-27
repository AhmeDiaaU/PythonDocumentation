string = input("Enter a string: ")
string = string.lower()
dct = dict.fromkeys(string,0)
for key in dct :
    for i in string:
        if key == i :
            dct[key]+=1
print(dct)