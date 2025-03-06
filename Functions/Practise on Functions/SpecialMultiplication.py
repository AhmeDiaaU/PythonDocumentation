def SpecialMulti(word):
    """_summary_

    Args:
        word : String 
        get each char by an iteration 
        for idx , char in enumerate(word):
             result += (char*idx) 
             multiply it by its index
    
        return result 
    """
    result = ""
    for idx , char in enumerate(word):
        result += (char * (idx+1))
    return result
word = input()
print(SpecialMulti(word))
