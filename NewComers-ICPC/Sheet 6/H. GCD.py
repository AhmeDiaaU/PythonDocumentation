def GCD(A, B):
    if B == 0:
        return A
    return GCD(B, A % B)


def LCM(A, B):
    return (A * B) // GCD(A, B)


Firstnumber, secondnumber = map(int, input().split())
print(GCD(max(Firstnumber, secondnumber), min(Firstnumber, secondnumber)), end=" ")
print(LCM(Firstnumber, secondnumber))
