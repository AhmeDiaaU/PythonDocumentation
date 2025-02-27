import math
def power(num , base):
    result = 1 
    for _ in range(base) :
        result*=num
    return result
def DistanceBetweenPoints(x,y,x2,y2):
    xp = power(x2 - x , 2)
    yp = power(y2 - y , 2)

    distance = math.sqrt(xp + yp)
    return distance
x , y , x2, y2 = map(int,input().split())
print(DistanceBetweenPoints(x , y , x2 , y2))