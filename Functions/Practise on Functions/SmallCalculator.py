def print_menu():
    while True :
        print("Menu : ")
        print("Enter 1 to sum numbers from to N")
        print("Enter 2 to evaluate simple 2 numbers expression e.g(2+3)")
        print("Enter 3 to End the program")

def sum_1_to_n (n):
    sum = 0 
    for i in range(n):
        sum+=i
    return sum
def divide (num1 , num2 , operation):
    