
## 1 **Dictionary Basics**
- **Key Concepts**:
  - Dictionaries store key-value pairs.
  - Keys must be unique.
  - Values can be of any type.
  
- **Code Example**:
  ```python
  det = {'Ahmed': 20, 'Ziad': 25.2, 'C#bj': [5.23]}
  print(det.get('Ahmed'))  # Returns 20
  print(det.get(7.15, 'IP 7 doesn\'t exist'))  # Sets value to 7 if key doesn't exist
  ```

---

### 2. **Dictionary Operations**
- **Key Concepts**:
  - `clear()`: Removes all keys.
  - `items()`: Returns key-value pairs.
  - `keys()`: Returns all keys.
  - `values()`: Returns all values.
  
- **Code Example**:
  ```python
  clct = {'X': 1, 'b': 20, 'q': 80}
  clct['a'] = 30  # Inserted at the end
  for key, value in clct.items():
      print(f'{key}: {value}')
  ```

---

### 3. **Time Complexity**
- **Key Concepts**:
  - Insertion, deletion, and lookup operations are generally O(1).
  - Iterating over all elements is O(n).
  
- **Formula**:
  \[
  \frac{q}{Nv_3}
  \]
  
---

### 4. **Insertion Order Preservation**
- **Key Concepts**:
  - In Python 3.7+, dictionaries preserve insertion order.
  
- **Code Example**:
  ```python
  det = {20: 10, 1/4: 20, 30: 15, (0, 2): 50}
  det[30] = 10  # Updates the value
  print(det)  # Order is preserved
  ```

---

### 5. **List vs Dictionary**
- **Key Concepts**:
  - **List**: Ordered sequence, can be indexed or sliced.
  - **Dictionary**: Unordered collection of key-value pairs, insertion order is preserved.
  
- **Code Example**:
  ```python
  lst = [5, 3, 3]
  det = {"Ziad": 95.9, 9: lst, "Hey": emp}
  lst.pop()  # Only affects the list, not the dictionary
  ```

---

### 6. **Shallow Copy**
- **Key Concepts**:
  - `copy()` creates a shallow copy of the dictionary.
  - Changes to nested objects affect both the original and the copy.
  
- **Code Example**:
  ```python
  clb = det.copy()
  print(clb['Hey'] is det['Hey'])  # Returns True
  ```

---

### 7. **Set Basics**
- **Key Concepts**:
  - Sets are unordered collections of unique elements.
  - Insertion order is not preserved.
  
- **Code Example**:
  ```python
  unique_keys = dict.fromkeys([1, 2, 30, 'b', 20])
  print(unique_keys)  # {1: None, 2: None, 30: None, 'b': None, 20: None}
  ```

---

### 8. **Set Operations**
- **Key Concepts**:
  - **Union**: Combines elements from two sets.
  - **Intersection**: Finds common elements.
  - **Difference**: Finds elements in one set but not the other.
  
- **Code Example**:
  ```python
  str1 = {1, 5, 7, 8}
  str2 = {1, 5, 3, 10}
  print(str1 | str2)  # Union: {1, 3, 5, 7, 8, 10}
  print(str1 & str2)  # Intersection: {1, 5}
  ```

---

### 9. **FrozenSet**
- **Key Concepts**:
  - Immutable version of a set.
  - Can be used as a dictionary key.
  
- **Code Example**:
  ```python
  frozen = frozenset([1, 2, 3, 4, 5])
  print(frozen)  # frozenset({1, 2, 3, 4, 5})
  ```

---

### 10. **Set Comprehension**
- **Key Concepts**:
  - Similar to list comprehension but for sets.
  
- **Code Example**:
  ```python
  line = "Ahmed Dina Eldeen Kamel"
  unique_vowels = {i for i in line if i in 'AEIOUaeiou'}
  print(unique_vowels)  # {'a', 'e', 'i'}
  ```

---

### 11. **Filtering Duplicates**
- **Key Concepts**:
  - Use sets to filter out duplicate lists.
  
- **Code Example**:
  ```python
  def filter_duplicates(list_of_lists):
      seen = set()
      result = []
      for lst in list_of_lists:
          t = tuple(lst)
          if t not in seen:
              seen.add(t)
              result.append(lst)
      return result
  ```

---

### 12. **Sorting by Data Type**
- **Key Concepts**:
  - Sort a list by data type (int, float, string, etc.).
  
- **Code Example**:
  ```python
  def sort_by_datatype(lst):
      dt = {}
      for item in lst:
          t = type(item)
          if t not in dt:
              dt[t] = []
          dt[t].append(item)
      return [item for lst in dt.values() for item in lst]
  ```

---

### 13. **String Mapping**
- **Key Concepts**:
  - Map characters from one string to another.
  
- **Code Example**:
  ```python
  from_str = "abc"
  to_str = "123"
  mapping = {from_str[i]: to_str[i] for i in range(len(from_str))}
  string = input("Enter String")
  res = ""
  for char in string:
      res += mapping.get(char, char)
  print(res)
  ```

---

### 14. **Set Methods**
- **Key Concepts**:
  - `add()`: Adds an element.
  - `remove()`: Removes an element (raises error if not found).
  - `discard()`: Removes an element (no error if not found).
  - `pop()`: Removes a random element.
  
- **Code Example**:
  ```python
  s = {1, 2, 3}
  s.add(4)
  s.discard(2)
  print(s)  # {1, 3, 4}
  ```

---

### 15. **Subset and Superset**
- **Key Concepts**:
  - `<=`: Checks if one set is a subset of another.
  - `>=`: Checks if one set is a superset of another.
  
- **Code Example**:
  ```python
  str1 = {1, 5}
  str2 = {1, 5, 7, 8}
  print(str1 <= str2)  # True
  print(str2 >= str1)  # True
  ```

---

### 16. **Set Updates**
- **Key Concepts**:
  - `|=`: Updates a set with the union of another set.
  - `&=`: Updates a set with the intersection of another set.
  
- **Code Example**:
  ```python
  str1 = {1, 5}
  str2 = {5, 7, 8}
  str1 |= str2  # str1 is now {1, 5, 7, 8}
  ```

---

### 17. **FrozenSet as Dictionary Key**
- **Key Concepts**:
  - Frozen sets can be used as dictionary keys because they are immutable.
  
- **Code Example**:
  ```python
  frozen = frozenset([1, 2, 3])
  d = {frozen: 'value'}
  print(d[frozen])  # 'value'
  ```

---

### 18. **Set Iteration**
- **Key Concepts**:
  - Iterate over a set using a loop.
  
- **Code Example**:
  ```python
  s = {1, 2, 3, 4, 5}
  for item in sorted(s):
      print(item, end=" ")  # 1 2 3 4 5
  ```

---

### 19. **Set Comprehension with Conditions**
- **Key Concepts**:
  - Use conditions to filter elements in set comprehension.
  
- **Code Example**:
  ```python
  line = "Ahmed Dina Eldeen Kamel"
  unique_vowels = {i for i in line if i in 'AEIOUaeiou'}
  print(unique_vowels)  # {'a', 'e', 'i'}
  ```

---

### 20. **Set Union with Multiple Sets**
- **Key Concepts**:
  - Union of multiple sets can be done using the `|` operator.
  
- **Code Example**:
  ```python
  str1 = {1, 5, 7, 8}
  str2 = {1, 5, 3, 10}
  str3 = {5, 6, 13}
  union_set = str1 | str2 | str3
  print(union_set)  # {1, 3, 5, 6, 7, 8, 10, 13}
  ```

________________________________________________________________
