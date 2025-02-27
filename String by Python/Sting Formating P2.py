# Precision
value = 72.12345678901234
print(value)

print('{:20}'.format(value)) # print it all
print('{:11f}'.format(value)) # print 11 units
print('{:11.3f}'.format(value)) # print 11 units 3 of them precision
print('{:3.5f}'.format(value)) # print 5 precision elements


val =2.6
print('{:11f}'.format(value)) # f defult is 6 numbers it will print 6 numbers and the resst is spaces
print('{:11.0}'.format(value)) # 2.6 will be rounded


# f string way :
name , age = "ahmed " , 21
print(f"{name} is {age} old") # simpliying the formating
print(f'{val :11.3f}') # simpilfying the value to 3 decimal points in one line


# we can use it with classes

class employee :
    def __init__(self , name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Employee {self.name} is {self.age} years old "

most = employee("ahmed", 21)
print(f"{most}") # to print the function inside
print(f"{most!r}") # to force to print them in a -("" + "")- way


