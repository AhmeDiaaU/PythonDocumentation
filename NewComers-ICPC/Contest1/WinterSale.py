discount, listed_price = map(float, input().split())
original_price = listed_price / (1 - discount / 100)
print(f"{original_price:.2f}")

