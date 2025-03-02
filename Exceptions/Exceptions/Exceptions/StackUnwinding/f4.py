def f4(path , idx):
    file = open(path , 'r')
    idx = int(idx)
    lst = file.read().splitlines()
    res = lst[idx]
    return res