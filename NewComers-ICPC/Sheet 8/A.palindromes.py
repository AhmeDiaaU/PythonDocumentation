def PalindromesReplace(name):
    end = len(name)
    name = list(name)
    for start in range(len(name)) :
        mirror = end - start -1
        if name[start] == name[mirror] == '?':
            name[start] = 'a'
            name[mirror] = 'a'
        elif name[start] == '?':
            name[start] = name[mirror]
        elif name[mirror] == '?':
            name[mirror] = name[start]
        elif name[start] != name[mirror]:
            return -1
    return name
string = input()
P_string = PalindromesReplace(string)
if P_string == -1:
    print(-1)
else :
    print("".join(PalindromesReplace(P_string)))