if __name__ ==  '__main__':
    line = input()+ '$'

    res = []
    group_idx = 0
    for idx in range(1,len(line)):
        if line[idx].lower() != line[idx-1].lower():
           ln = idx - group_idx
           res.append((-ln , line[idx-1]))
           group_idx = idx
    print(res)
    res.sort()
    for idx ,(freq,char) in enumerate(res):
        freq = -freq
        if freq == 1 :
            res[idx] = char
        else :
            res[idx] =f"{freq}{char}"

    print("_".join(res))