def sort_by_type(lst):
    dct = {}
    for item in lst :
        t = type(item)
        dct.setdefault(t , [])
        dct[t].append(item)

    lsts = [sorted(lst) for lst in dct.values()]
    return[item for lst in lsts for item in lst]


if __name__ == '__main__':
    lst = [1, 2, 3, 'a', 'b', 'c', 1.1, 1.2, 1.3]
    print(sort_by_type(lst))