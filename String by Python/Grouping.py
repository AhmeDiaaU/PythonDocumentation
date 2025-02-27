if __name__ ==  '__main__':
    line = input()+ '$'

    res = []
    group_idx = 0
    for idx in range(1,len(line)):
        if line[idx].lower() != line[idx-1].lower():
            res.append(line[group_idx:idx])
            group_idx = idx

    print(','.join(res))