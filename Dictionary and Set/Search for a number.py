lst = list(map(int , input().split()))
queries = list(map(int , input().split()))
dct ={}
for idx , value in enumerate(lst):
    dct[value] = idx
for q in queries:
    ans = dct.get(q , -1)
    print(f"Query {q} answer {ans}")

user_data = {'hobbies' : 1 }
user_data['hobbies'].append('Coding')
print(user_data)