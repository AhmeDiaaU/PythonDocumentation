def print_conc(str1, str2):
    for c1, c2 in zip(str1, str2):
        print(c1, c2, end=" ")
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        if len(str1) > len(str2):
            print(str1[len(str2):], end=" ")
        print()


if __name__ == "__main__":
    str1, str2 = input().split()
    print(print_conc(str1, str2))
