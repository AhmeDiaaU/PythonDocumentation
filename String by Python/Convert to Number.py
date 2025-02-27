def our_int(x):
    digits = [char for char in x if char.isdigit()]
    x = "".join(digits)
    x = int(x)
    return x


x = input()
print(our_int(x))
print(our_int(x)*3)