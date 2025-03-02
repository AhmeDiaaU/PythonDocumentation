# try to open a file that doesnt exist
path = "data.txt"

file =  open(path , 'r')
for line in file :
    print(line , end = " ")
file.close()
#file doesnt exist it will throw Exception 
#"[Errno 2] No such file or directory: 'data.txt'"


# we handel it by ==> 
"""try: 
    file = open(path , 'r')
    for line in file :
        print(line , end="")
except :
    print(f"There is no file called {path}")"""
# this will return message make the error more clear 
# and doesnt stop the program

#try divide by zero 
"""def division():
    num = int(input())
    divisable_number = int(input())
    return num // divisable_number
print(division())"""

# will throw exception that integer division by zero 
