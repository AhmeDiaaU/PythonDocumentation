print("abcDEF".upper())  # print all of it to upper case
print("abcDEF".lower())  # print all of it to lower case
print("abc".islower())  # check if all are lowercase (bool)
print("DEF".isupper())  # check if all are lowercase (bool)

print("abcdef".endswith("def"))  # check what does it end with
print("abcdef".startswith("abc"))  # check what does it start with

print("abcdef".find("def"))  # find lowest index it will return -1 if the string is not founded
print("abcdef".rfind("def"))  # checkl from behind in reversed way

print("abcdef".count("def"))  # count how many time does this exist in line

print(" ".isspace())  # gives true
print('\n\tHello   \t '.strip())  # strip remove all spaces
print('hi ahmed ? hi'.replace('hi', 'bye'))  # replace string with another one
print("\ni am 33 ".split())  #split every string after every whitespace in a list
print("hey\nhow\nare\nyou doing".splitlines())  # after every \n it will put string in list
print("i am ahmed diaa".split("a"))  # will split after every a in the string
input().split()  # meanss that take input after every whitespace

#join method
lst = ["a", "bb", "ccc"]

print("".join(" "))  #  join list items with " "
s1 = "abc"
s2 = "123"
print(s1.join(s2)) # 1abc2abc3
# after every number from s2 it will print s1
 