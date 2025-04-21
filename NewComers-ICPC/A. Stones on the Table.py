n = int(input())
stones = input()
counter = 0
for color in range(len(stones)):
    if color > 0 and stones[color] == stones[color-1]:
        counter += 1 
print(counter)