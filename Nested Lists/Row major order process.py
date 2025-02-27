grades = [
    [34, 67, 23, 45],
    [12, 56, 78, 90],
    [31, 24, 55, 88],
    [99, 13, 46, 73],
    [18, 37, 61, 80],
    [45, 22, 19, 27],
    [67, 54, 29, 11]
]


# calculate each row and store its value in list
def calculate_avg_row(lst_of_lsts):
    row_avg = []
    for lst in lst_of_lsts:
        sum = 0
        for num in lst:
            sum += num
        row_avg.append(sum / len(lst))
    return row_avg


print(calculate_avg_row(grades))


# more shorty way ( comprehension )
def compute_avg_row(lst_of_lsts):
    return [sum(lst) / len(lst) for lst in lst_of_lsts]


print(compute_avg_row(grades))
