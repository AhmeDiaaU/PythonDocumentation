# Python Dictionaries: A Comprehensive Guide

> [!abstract] Dictionary at a Glance Dictionaries store data as **key-value pairs** and are one of Python's most powerful built-in data structures. Keys must be immutable (strings, numbers, tuples) while values can be any Python object.
> 
> ```python
> # Dictionary visualization
> {
>   'key1': 'value1',
>   'key2': 'value2'
> }
> ```

## Creating Dictionaries

```python
# Empty dictionary
empty_dict = {}
empty_dict = dict()

# Dictionary with initial values
user_data = {'name': 'Alice', 'age': 30, 'skills': ['Python', 'Data Science']}

# Using dict() constructor
config = dict(theme='dark', language='en', notifications=True)

# From list of tuples
items = [('apple', 0.99), ('banana', 0.59), ('orange', 1.29)]
prices = dict(items)
```

## Essential Dictionary Methods

```python
# Creating our playground dictionary
user_data = {'name': 'Alice', 'age': 30, 'skills': ['Python', 'Data Science']}

# .keys(): Retrieve all keys
print(user_data.keys())  # dict_keys(['name', 'age', 'skills'])

# .values(): Get all values
print(user_data.values())  # dict_values(['Alice', 30, ['Python', 'Data Science']])

# .items(): Get key-value pairs
print(user_data.items())  # dict_items([('name', 'Alice'), ('age', 30), ('skills', [...])])

# Basic access - will raise KeyError if key doesn't exist
print(user_data['name'])  # 'Alice'
```

> [!tip]+ Dynamic Views The `.keys()`, `.values()`, and `.items()` methods return _view objects_ that dynamically reflect dictionary changes!
> 
> ```python
> data = {'a': 1}
> keys = data.keys()  # dict_keys(['a'])
> data['b'] = 2
> print(keys)  # dict_keys(['a', 'b']) - automatically updated!
> ```

## Advanced Dictionary Methods

> [!example]+ `.get()`: Safe Value Retrieval
> 
> ```python
> # Default value if key doesn't exist
> username = user_data.get('username', 'Guest')  # Returns 'Guest'
> 
> # Visual comparison:
> # Safe: user_data.get('missing_key', 'default')  → 'default'
> # Risky: user_data['missing_key']  → KeyError exception!
> ```

> [!example]+ `.update()`: Merging Dictionaries
> 
> ```python
> # Combine dictionaries with ease
> contact_info = {'email': 'alice@example.com'}
> user_data.update(contact_info)
> # user_data now includes email
> ```

> [!example]+ `.pop()`: Remove and Return
> 
> ```python
> # Remove a specific key and get its value
> age = user_data.pop('age')  # Removes 'age' key and returns 30
> ```

> [!example]+ `.setdefault()`: Default Insertion
> 
> ```python
> # Insert key with default if not exists
> hobbies = user_data.setdefault('hobbies', [])
> # If 'hobbies' didn't exist, it's created with an empty list
> user_data['hobbies'].append('Coding')
> ```

## Dictionary Comprehensions

> [!note]+ Dictionary Comprehension Syntax
> 
> ```
> { key_expression: value_expression for item in iterable [if condition] }
> ```

```python
# Create a dictionary of squares
squares = {x: x**2 for x in range(6)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Conditional dictionary comprehension
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# Result: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Transform values with comprehension
prices = {'apple': 1.20, 'banana': 0.50, 'orange': 0.80}
sale_prices = {fruit: price * 0.8 for fruit, price in prices.items()}
# Result: {'apple': 0.96, 'banana': 0.40, 'orange': 0.64}
```

## Method Comparison Table

> [!important]+ Quick Reference Guide
> 
> |Method|Purpose|Returns|Example|
> |:-:|:-:|:-:|:--|
> |`.keys()`|All keys|View object|`{'a':1, 'b':2}.keys()` → `dict_keys(['a', 'b'])`|
> |`.values()`|All values|View object|`{'a':1, 'b':2}.values()` → `dict_values([1, 2])`|
> |`.items()`|Key-value pairs|View object|`{'a':1, 'b':2}.items()` → `dict_items([('a',1), ('b',2)])`|
> |`.get()`|Safe retrieval|Value or default|`{'a':1}.get('b', 0)` → `0`|
> |`.pop()`|Remove & return|Removed value|`{'a':1}.pop('a')` → `1`|
> |`.update()`|Merge dictionaries|`None`|Modifies in-place|
> |`.setdefault()`|Set if missing|Value of key|`d.setdefault('k', [])`|
> |`.clear()`|Empty dict|`None`|`d.clear()` → `{}`|
> |`.copy()`|Shallow copy|New dict|`d.copy()` → New dict with same contents|

## Advanced Techniques

> [!success]+ Dictionary Inversion
> 
> ```python
> # Inverting a dictionary
> original = {'a': 1, 'b': 2, 'c': 3}
> inverted = {value: key for key, value in original.items()}
> # Result: {1: 'a', 2: 'b', 3: 'c'}
> ```

> [!success]+ Merging Dictionaries
> 
> ```python
> # Python 3.9+ merge operator
> dict1 = {'a': 1, 'b': 2}
> dict2 = {'c': 3, 'd': 4}
> merged = dict1 | dict2  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
> 
> # Update with |= operator
> dict1 |= dict2  # dict1 is now {'a': 1, 'b': 2, 'c': 3, 'd': 4}
> ```

> [!tip]+ Nested Dictionaries
> 
> ```python
> user_profile = {
>     'personal': {'name': 'Alice', 'age': 30},
>     'professional': {'title': 'Developer', 'skills': ['Python', 'SQL']}
> }
> 
> # Accessing nested values
> user_profile['personal']['name']  # 'Alice'
> ```

## Dictionary Use Cases

> [!example]+ Frequency Counter
> 
> ```python
> # Count character frequency in a string
> text = "hello world"
> char_count = {}
> 
> for char in text:
>     char_count[char] = char_count.get(char, 0) + 1
> 
> print(char_count)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
> ```

> [!example]+ Group By
> 
> ```python
> # Group students by grade
> students = [
>     {'name': 'Alice', 'grade': 'A'},
>     {'name': 'Bob', 'grade': 'B'},
>     {'name': 'Charlie', 'grade': 'A'}
> ]
> 
> by_grade = {}
> for student in students:
>     grade = student['grade']
>     if grade not in by_grade:
>         by_grade[grade] = []
>     by_grade[grade].append(student['name'])
> 
> print(by_grade)  # {'A': ['Alice', 'Charlie'], 'B': ['Bob']}
> ```

> [!example]+ Caching Results
> 
> ```python
> # Using a dictionary as a cache
> def fibonacci(n, cache={}):
>     if n in cache:
>         return cache[n]
>     if n <= 1:
>         return n
>     cache[n] = fibonacci(n-1) + fibonacci(n-2)
>     return cache[n]
>     
> print(fibonacci(30))  # Fast calculation using caching
> ```

## Performance Considerations

> [!warning]+ Time Complexity
> 
> |Operation|Average Case|Worst Case|
> |---|---|---|
> |Access|O(1)|O(n)|
> |Insert|O(1)|O(n)|
> |Delete|O(1)|O(n)|
> |Search|O(1)|O(n)|

> [!note]+ Memory Usage Dictionaries in Python are implemented using hash tables, which typically consume more memory than lists but provide much faster lookups, insertions, and deletions when working with large datasets.

## Best Practices

1. **Use descriptive keys**: Make dictionary keys meaningful and self-documenting.
2. **Prefer `.get()` for safe access**: Avoid KeyError exceptions with default values.
3. **Consider `collections.defaultdict`**: When working with complex default values.
4. **Use dictionary comprehensions** for transformations rather than loops when appropriate.
5. **Check key existence** with `in` operator rather than try/except blocks for readability.

```python
# Better:
if 'key' in my_dict:
    do_something(my_dict['key'])
    
# Rather than:
try:
    do_something(my_dict['key'])
except KeyError:
    pass
