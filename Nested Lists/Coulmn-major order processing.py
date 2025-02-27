grades = [
    [34, 67, 23, 45],
    [12, 56, 78, 90],
    [31, 24, 55, 88],
    [99, 13, 46, 73],
    [18, 37, 61, 80],
    [45, 22, 19, 27],
    [67, 54, 29, 11]
]


# iterate over column and calculate sum of them then calculate avg
def coulmns_col_avg(lst_of_lsts):
    col_avg = []
    for r in range(len(lst_of_lsts[0])):
        sum = 0
        for c in range(len(lst_of_lsts)):
            sum += lst_of_lsts[c][r]
        col_avg.append(sum / len(lst_of_lsts))
    return col_avg


print(coulmns_col_avg(grades))

# effecient way is to un pack !

grade = [1, 2, 3, 4], [5, 6], [7, 8, 9, 10]
for a, b, c in zip(*grade):
    print(a, b, c)


# simple example of unpacking matrix in coulmn way

def compute_col_avg(lst_of_lsts):
    # col_avg = []
    #for tub in zip(*lst_of_lsts):
    #    col_avg.append(sum(tub) / len(tub))
    #return col_avg
    return [sum(tub) / len(tub) for tub in zip(*lst_of_lsts)]


print(compute_col_avg(grades))
# more efficient way to iterate in column in matrixes
