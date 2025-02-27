lines = []
M = 0
S = 0
with open ("data.txt" , 'r') as file :
    lines = file.readlines()
for line in lines : 
    S +=abs(int(line))
    if int(line) > M :
        M = int(line)
print(S * M)