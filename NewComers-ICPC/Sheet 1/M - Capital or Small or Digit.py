value = input()
asci = ord(value)
if asci >= 48 and asci <= 64:
    print("IS DIGIT")
elif asci >= 65 and asci <= 96:
    print("ALPHA")
    print("IS CAPITAL")
elif asci >= 97:
    print("ALPHA")
    print("IS SMALL")
