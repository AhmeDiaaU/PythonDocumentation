def read_rooms():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows
    for row in range(rows):
        lst_of_lsts[row] = list(map(int , input().split()))
    return lst_of_lsts

rooms = read_rooms()
counter = 0
for room in rooms :
    if (room[0] + 2 ) <= room[1]:
        counter +=1
print(counter)  
