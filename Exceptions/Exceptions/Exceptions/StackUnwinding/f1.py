from f2 import f2


def f1(path, idx):
    try:
        return f2(path, idx)
    except IndexError:
        print("f3 caught a out of bound index")
        return -2
