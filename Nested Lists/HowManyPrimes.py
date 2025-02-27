def Read_Matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows
    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input().split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts


def IsPrime(num):
    if num <= 1:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1


# if prime return 0 if not return 1

if __name__ == '__main__':
    rows, cols, matrix = Read_Matrix()
    is_prime_matrix = [[IsPrime(value) for value in row] for row in matrix]  #
    # for every row it iterates over it if value is prime it replace it with 1 else replace it with 0

    q = int(input())  # number of queries
    while q > 0:
        total_prime = 0
        sr, sc, nr, nc = map(int,input().split())  # Start row  , start coulmn , next row , next column
        for r in range(sr, sr + nr):
            total_prime += sum(is_prime_matrix[r][sc:sc + nc])
        print(total_prime)
        q -= 1
