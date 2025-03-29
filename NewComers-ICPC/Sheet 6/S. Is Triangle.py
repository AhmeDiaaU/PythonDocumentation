import math
def IsTriangle(x , y , z) :
	area = 0 
	if x + y > z and x + z > y and y + z > x :
		s = (x + y + z )// 2 
		area = math.sqrt(s * (s-x)*(s-y)*(s-z))
		print("Valid")
		print(area)
	else :
		print("Invalid")
 
a ,b ,c = map(int, input().split())
IsTriangle(a , b, c)