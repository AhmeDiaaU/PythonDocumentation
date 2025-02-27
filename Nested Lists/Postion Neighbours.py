# in postion neighbours we use it to get ->
# 1- up , right , down , left , di = {1,0,-1,0} , dj={0,1,0,-1}
# or 8 neighbours

def get_neighbour(i, j):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    return [(i + di[d] , j + dj[d]) for d in range(4)]
    #

print(get_neighbour(0, 0))
print(get_neighbour(3, 6))

# 4 neighbours