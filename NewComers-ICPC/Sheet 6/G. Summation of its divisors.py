import math
import time

def SumDivisors(N):
    Start = time.time()
    Result = 0
    for Divisor in range(1 , int(math.sqrt(N)+1)):
        if (N % Divisor == 0 ):
            Result +=Divisor
            Result += N//Divisor
            if ( Divisor == N // Divisor ):
                Result -= Divisor
    return Result
N = int(input())
# it ended in time -> 
Start = time.time()
print(SumDivisors(N))
end = time.time()
print(end - Start)