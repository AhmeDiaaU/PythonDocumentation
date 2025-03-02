from f4 import f4


def f3(path, idx):
    try:
        return f4(path, idx)
    except FileNotFoundError:
        print("f3 caughtt a no file")
        return 0
