def digits(n):
    if n == 0 :
        return
    digits(n // 10) # divide n till its = 0 then start to rint each part of it by 
    print(n%10 , end=" ") #this
r = int(input())
while r > 0:
  digit = int(input())
  if digit == 0 :
     print(0 , end = " ")
  else :
     digits(digit)
  r -=1
  print()