def Next_alphapitical():
    char = input()
    char = char.lower()
    if char == 'z':
        return 'a'
    return chr(ord(char)+1) # this will make u add 1 to get next char

print(Next_alphapitical())