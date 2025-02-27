value = input()
asci = ord(value)
if asci >= 65 and asci <= 96:
    asci = asci + 32
    print(chr(asci))
elif asci >= 97:
    asci = asci - 32
    print(chr(asci))