def print_l(lst_of_lst) :
    for lst in lst_of_lst :
        print(*lst)
## to print list of lists and unpacking

def print3(lst_of_lsts):
    for i in range(len(lst_of_lsts)):
        for j in range(len(lst_of_lsts)):
            print(lst_of_lsts[i][j] , " ")
        print()
## to make it more indexable

def read_lst_of_lists() :
    rows = int(input())
    list_of_lists = [0] * rows
    for i in range(rows) :
        list_of_lists[rows] = list(map(int,input().split()))
    return list_of_lists