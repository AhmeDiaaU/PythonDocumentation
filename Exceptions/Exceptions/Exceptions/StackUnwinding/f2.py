from f3 import f3
def f2(path , idx):
    try :
        return f3(idx , path)
    except ValueError :
        print("f2 caught a wrong value")
        return -1 

