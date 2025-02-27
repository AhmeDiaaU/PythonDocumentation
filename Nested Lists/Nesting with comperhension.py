# Flatten a list without comperhension :
lst_of_lsts = [[1, 2], [3], [4, 5, 6], [7, 8], [9, 10]]
lst1 = []
for lst in lst_of_lsts:
    for num in lst:
        lst1.append(num)
print(lst1)

# for easiear way maje it in comperhension way :

lst2 = [item for lst in lst_of_lsts for item in lst]
#append item by accessing item in lst which is inside lst_of_lsts
print(lst2)


# same list


# Add int to all
# by normal way
def add_value(lst_of_lists, value):
    new_list_of_lsts = []
    for lst in lst_of_lists:
        new_list = []
        for item in lst:
            new_list.append(item + value)
        new_list_of_lsts.append(new_list)
    return new_list_of_lsts


lst_of_lsts = [[1, 2], [3, 4], [4, 5], [6, 7], [8, 9]]

value = 10
print(add_value(lst_of_lsts, value))


# By comprehensive way
def compute_value(lst_of_lsts, value):
    return [[item + value for item in lst] for lst in lst_of_lsts]


print(compute_value(lst_of_lsts, 11))
# get list and transform it to new list
# so its so simple


# generating pairs  ->
l1 = [1, 2]
l2 = [10, 20, 30]
lst_pairs = []
for pair1 in l1:
    for pair2 in l2:
        lst_pairs.append((pair1, pair2))
print(lst_pairs)

# by comperhesive way - >
lst_pairs2 = [(item1, item2) for item1 in l1 for item2 in l2]
print(lst_pairs2)

# get two items as tuble insert them into lst by getting them while making two loops l1 and l2

# creating simple Grids , empty matrix
rows, col = 3, 4
ls = [[0] * rows] * col
print(ls)

########################################

ls[0][0] = 2
print(ls)
# just make the same copy of the same object

# proper way is
lst4 = [[0] * rows for i in range(col)]
lst4[0][0] = 2
print(lst4)
# print only two values in index 0 which is the first value in row and index 0 which is the first value in coulmn

# get 0 , 1 , 2  in lst
lst5 = [[x for x in range(rows)] for y in range(col)]
print(lst5)
# inner loop generate 0 1 2 and the outter loop for coulmn generate it 4 times
