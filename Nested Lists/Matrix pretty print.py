def read_matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows
    for row in range(rows):
        lst_of_lsts[row] = list(input().split())
    return rows, len(lst_of_lsts[0]), lst_of_lsts


if __name__ == '__main__':
    row, cols, matrix = read_matrix()
    width_per_col = [max([len(word) for word in col]) for col in zip(*matrix)] # width of each column
    matrix = ['#'.join([word.ljust(width_per_col[idx])for idx , word in enumerate(row)]) for row in matrix]
    print('\n'.join(matrix))


