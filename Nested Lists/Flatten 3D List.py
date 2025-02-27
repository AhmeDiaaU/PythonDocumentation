def list_relations (depth = 3 , rows = 4 , cols = 5):
    idx = 0 
    """
    Generates a 3D list with the given depth, rows and columns.
    """
    for d in range(depth):
        for r in range(rows):
            for c in range(cols):
                print(f"({d}, {r}, {c})==> {idx}")
                idx += 1
if __name__ == "__main__":
    depth , rows , cols ,type, *remain = map(int, input("Enter depth, rows and columns: ").split())
    db = rows *cols 
    rb = cols 
    cb = 1 
    if type == 1 :
        d , r , c = remain
        idx = d *db +r *rb +c*cb
        print(idx)
    else : 
        idx = remain[0]
        d = idx//db
        r = (idx %db) //rb
        c = idx % db % rb
        print (d , r , c)
