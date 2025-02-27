# 2D and 1D flatten relationship :
# find equations :
def From2DTo1D(cols, i, j):
    idx = i * cols + j
    return idx


def From1Dto2D(cols, idx):
    i = idx // cols
    j = idx % cols
    return i, j


def list_relation(rows=3, cols=4):
    idx = 0
    for r in range(rows):
        for c in range(cols):
            print(f"({r} , {c}) ==> {idx}")

            assert (r, c) == From1Dto2D(cols, idx)
            assert idx == From2DTo1D(cols, r, c)

            idx += 1


list_relation(3, 5)
