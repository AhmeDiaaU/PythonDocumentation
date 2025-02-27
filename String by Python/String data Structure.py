s1 = "ahmed"
s2 = "diaa"
s3 = s1 +2 *s2
lst = list(s1)
print(lst)
for idx , char in enumerate(s1):   # looping in a loop and printing its index
    print(idx,char)
print("most" < "MOST") # comparing in ascii

# unpacking a string
a ,b,c,d = "Most"
print(a,b)

#### functions with string
s1 ="moST"
print(len(s1),min(s1),max(s1))
print(sorted(s1))
print(tuple(reversed(s1)))
# string is immutable
print(s1[0],s1[-1]) # -1 means the first from right
print(s1[2:])# from 2 to last
print(s1[::]) # from 0 to last and step by 1
print(s1[::-1]) # print it in reverse

# list comprehension
lst = ["Ahmed" , "Diaa" , "eldeen","Kamel","1234"]
first_letter = [word[0] for word in lst]
first_letter_l = [word[0].lower() for word in lst] # for lowecasses
print(first_letter)
print(first_letter_l)
# to find digits
digits = [int(char) for char in lst if char.isdigit()]
print(digits)


# immutability
my_str = "Ahmed"
my_str = my_str[:2] + my_str[:2].upper() +my_str[3:]
my_str2 = my_str
print(my_str2 is my_str) # check if the point to the same memory
print(id(my_str)) # id of the memory
my_str+='saad' # string is immutable the memory address will change
print(id(my_str2))# id of memory
print(my_str is my_str2)
print(my_str)
    