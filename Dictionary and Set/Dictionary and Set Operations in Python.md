#  Dictionary Methods
> [!abstract] Dictionary at a Glance Dictionaries store data as **key-value pairs** and are one of Python's most powerful built-in data structures.
> 
> ```python
> # Dictionary visualization
> {
>   🔑 'key1': 📦 'value1',
>   🔑 'key2': 📦 'value2'
> }
> ```

## Essential Dictionary Methods

```python
# Creating our playground dictionary
user_data = {'name': 'Alice', 'age': 30, 'skills': ['Python', 'Data Science']}

# 🕵️ .keys(): Retrieve all keys
print(user_data.keys())  # dict_keys(['name', 'age', 'skills'])

# 🔍 .values(): Get all values
print(user_data.values())  # dict_values(['Alice', 30, ['Python', 'Data Science']])

# 🔗 .items(): Get key-value pairs
print(user_data.items())  # dict_items([('name', 'Alice'), ('age', 30), ('skills', [...])])
```

> [!tip]+ Dynamic Views 🔄 The `.keys()`, `.values()`, and `.items()` methods return _view objects_ that dynamically reflect dictionary changes!
> 
> ```python
> data = {'a': 1}
> keys = data.keys()  # dict_keys(['a'])
> data['b'] = 2
> print(keys)  # dict_keys(['a', 'b']) - automatically updated!
> ```

##  Advanced Dictionary Methods

> [!example]+ 🧩 `.get()`: Safe Value Retrieval
> 
> ```python
> # Default value if key doesn't exist
> username = user_data.get('username', 'Guest')  # Returns 'Guest'
> 
> # Visual comparison:
> # ✅ Safe: user_data.get('missing_key', 'default')  → 'default'
> # ❌ Risky: user_data['missing_key']  → KeyError exception!
> ```

> [!example]+ 🔄 `.update()`: Merging Dictionaries
> 
> ```python
> # Combine dictionaries with ease
> contact_info = {'email': 'alice@example.com'}
> user_data.update(contact_info)
> # user_data now includes email
> ```
> 
> ```mermaid
> graph LR
>     A["user_data<br>{name: 'Alice', age: 30}"] --> C
>     B["contact_info<br>{email: 'alice@example.com'}"] --> C
>     C["RESULT<br>{name: 'Alice', age: 30, email: 'alice@example.com'}"]
>     style A fill:#ffcccc
>     style B fill:#ccffcc
>     style C fill:#ccccff
> ```

> [!example]+ 🗑️ `.pop()`: Remove and Return
> 
> ```python
> # Remove a specific key and get its value
> age = user_data.pop('age')  # Removes 'age' key and returns 30
> ```
> 
> ```mermaid
> flowchart LR
>     A["Before: {'name': 'Alice', 'age': 30}"] --> B["pop('age')"]
>     B --> C["After: {'name': 'Alice'}"]
>     B --> D["Return: 30"]
>     style A fill:#f9d5e5
>     style B fill:#eeac99
>     style C fill:#e06377
>     style D fill:#c83349
> ```

> [!example]+ 🔒 `.setdefault()`: Clever Default Insertion
> 
> ```python
> # Insert key with default if not exists
> hobbies = user_data.setdefault('hobbies', [])
> # If 'hobbies' didn't exist, it's created with an empty list
> user_data['hobbies'].append('Coding')
> ```
> 
> ```mermaid
> graph TD
>     A["Dict: {'name': 'Alice'}"] --> B{Key 'hobbies' exists?}
>     B -->|Yes| C["Return existing value"]
>     B -->|No| D["Create key with default value"]
>     D --> E["Dict: {'name': 'Alice', 'hobbies': []}"]
>     style A fill:#cfe2f3
>     style B fill:#fff2cc
>     style C fill:#d9ead3
>     style D fill:#f4cccc
>     style E fill:#d0e0e3
> ```

##  Dictionary Comprehensions: One-Liners of Magic

> [!note]+ Dictionary Comprehension Syntax
> 
> ```
> { key_expression: value_expression for item in iterable [if condition] }
> ```
> 
> ![Dictionary Comprehension](https://digital-garden.netlify.app/images/dict-comp.png)

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

> [!success]+ Visual Transformation
> 
> ```mermaid
> graph LR
>     A["range(6)"] --> B["Dictionary Comprehension<br>{x: x**2 for x in range(6)}"]
>     B --> C["{0:0, 1:1, 2:4, 3:9, 4:16, 5:25}"]
>     style A fill:#d4f1f9
>     style B fill:#75e6da
>     style C fill:#189ab4
> ```

##  Method Comparison Table

> [!important]+ Quick Reference Guide
> 
> |Method|Purpose|Returns|Example|
> |:-:|:-:|:-:|:--
> |`.keys()`|All keys|View object|`{'a':1, 'b':2}.keys()` → `dict_keys(['a', 'b'])`|
> |`.values()`|All values|View object|`{'a':1, 'b':2}.values()` → `dict_values([1, 2])`
> |`.items()`|Key-value pairs|View object|`{'a':1, 'b':2}.items()` → `dict_items([('a',1), ('b',2)])`
> |`.get()`|Safe retrieval|Value or default|`{'a':1}.get('b', 0)` → `0`
> |`.pop()`|Remove & return|Removed value|`{'a':1}.pop('a')` → `1`
> |`.update()`|Merge dictionaries|`None`|Modifies in-place
> |`.setdefault()`|Set if missing|Value of key|`d.setdefault('k', [])`
> |`.clear()`|Empty dict|`None`|`d.clear()` → `{}`
> |`.copy()`|Shallow copy|New dict|`d.copy()` → New dict with same contents
##  Advanced Tricks

> [!success]+ Dictionary Inversion
> 
> ```python
> # Inverting a dictionary
> original = {'a': 1, 'b': 2, 'c': 3}
> inverted = {value: key for key, value in original.items()}
> # Result: {1: 'a', 2: 'b', 3: 'c'}
> ```
> 
> ```mermaid
> flowchart LR
>     A["{'a': 1, 'b': 2, 'c': 3}"] --> B["Dictionary Comprehension"]
>     B --> C["{1: 'a', 2: 'b', 3: 'c'}"]
>     style A fill:#ffcc99
>     style B fill:#ff9966
>     style C fill:#ff6633
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
> 
> ```mermaid
> graph TD
>     A["dict1 = {'a': 1, 'b': 2}"] --> D
>     B["dict2 = {'c': 3, 'd': 4}"] --> D
>     D["dict1 | dict2"] --> E["{'a': 1, 'b': 2, 'c': 3, 'd': 4}"]
>     style A fill:#c8e6c9
>     style B fill:#a5d6a7
>     style D fill:#81c784
>     style E fill:#66bb6a
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
> 
> ```mermaid
> graph TD
>     A["user_profile"] --> B["'personal'"]
>     A --> C["'professional'"]
>     B --> D["'name': 'Alice'"]
>     B --> E["'age': 30"]
>     C --> F["'title': 'Developer'"]
>     C --> G["'skills': ['Python', 'SQL']"]
>     style A fill:#bbdefb
>     style B fill:#90caf9
>     style C fill:#90caf9
>     style D fill:#64b5f6
>     style E fill:#64b5f6
>     style F fill:#64b5f6
>     style G fill:#64b5f6
> ```

##  Dictionary Method Flow Chart

```mermaid
flowchart TD
    A[Dictionary] --> B{Operation Type}
    
    B -->|Access| C{Access Type}
    C -->|Single Key| C1{Key Exists?}
    C1 -->|Yes| C1A[Direct: dict[key]]
    C1 -->|Maybe Not| C1B[Safe: dict.get(key)]
    
    C -->|Multiple Keys| C2{What to Access?}
    C2 -->|All Keys| C2A[dict.keys()]
    C2 -->|All Values| C2B[dict.values()]
    C2 -->|Key-Value Pairs| C2C[dict.items()]
    
    B -->|Modify| D{Modification Type}
    D -->|Add/Update| D1{Single Entry?}
    D1 -->|Yes| D1A[dict[key] = value]
    D1 -->|Multiple| D1B[dict.update(other_dict)]
    
    D -->|Remove| D2{Remove Type}
    D2 -->|Known Key| D2A[dict.pop(key)]
    D2 -->|All Entries| D2B[dict.clear()]
    
    D -->|Special| D3{Special Operation}
    D3 -->|Default If Missing| D3A[dict.setdefault(key, default)]
    D3 -->|Create Copy| D3B[dict.copy()]
    
    style A fill:#f9d5e5,stroke:#333,stroke-width:2px
    style B fill:#eeac99,stroke:#333,stroke-width:2px
    style C fill:#e06377,stroke:#333,stroke-width:2px
    style D fill:#c83349,stroke:#333,stroke-width:2px
    style C1 fill:#5b9aa0,stroke:#333,stroke-width:2px
    style C2 fill:#5b9aa0,stroke:#333,stroke-width:2px
    style D1 fill:#622569,stroke:#333,stroke-width:2px
    style D2 fill:#622569,stroke:#333,stroke-width:2px
    style D3 fill:#622569,stroke:#333,stroke-width:2px
```

##  Dictionary Use Cases

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

##  Performance Considerations

> [!warning]+ Time Complexity
> 
> |Operation|Average Case|Worst Case|
> |---|---|---|
> |Access|O(1)|O(n)|
> |Insert|O(1)|O(n)|
> |Delete|O(1)|O(n)|
> |Search|O(1)|O(n)|

> [!quote]+ Zen of Dictionaries "Dictionary-based solutions are often more elegant and efficient than their list-based counterparts when working with mapped data."