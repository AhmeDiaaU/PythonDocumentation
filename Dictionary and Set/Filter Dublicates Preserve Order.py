def Filter_Dublicates_Preserve_Order (lsts) :
    dct = {}
    tubls = [tuple(lst) for lst in lsts]
    dct = dict.fromkeys(tubls)
    print(dct)
    return [list(tup) for tup in dct]
if __name__ == '__main__':
    lst = [[7,1] , [2,4] , [5,1] , [5,1] , [7,4]]
    print(Filter_Dublicates_Preserve_Order(lst))