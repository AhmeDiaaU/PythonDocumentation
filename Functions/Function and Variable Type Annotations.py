# complex typing
from typing import Union, Optional

def div1(x: float, y: float) -> Union[float, None]:
    if y == 0:
        return None
    return x / y

def div2(x: float, y: float) -> Optional[float]:  # same as above which means float is optional and can return none also
    if y == 0:
        return None
    return x / y

# more complex typing : 
def f1() -> list[int]:
    return [1, 2, 3]

def f2() -> list[int | str | None]: # can return list of intgers , string or None
    return ['most', 26, None, 1]

t1: list[float | str | bool] = [10, True, 'hey'] # create a variable of these types
t2: list[list[int]] = [[1, 2], [3, 4]]
t3: list[list[int | str]] = [[1, 2], ['hey', 4]]
t4: tuple[int, int, str] = (10, 20, 'hey')
t5: tuple[int, ...] = (1, 2, 3, 4)
t6: tuple = (1, 2.5, 'he')
t7: dict[str, int] = {'most': 10, 'hey': 20}
print(t1)
"""

The content you've provided discusses the use of type hints in Python and their implications. Here's a summary and explanation of the key points:

1. **Python Interpreter and Type Hints**:
   - The Python interpreter does not enforce type hints. This means that even if you specify that a function should take an `int`, it will still accept `float` or `string` without raising an error.
   - Example: If you define a function to add two integers, it will still work if you pass floats or strings that can be concatenated.

2. **Benefits of Type Hints**:
   - **Encourages Thoughtful Design**: Using type hints can make you think more carefully about your code's input and output, improving overall design and logic.
   - **Clear Communication**: Type hints make it easier to understand what types of arguments a function expects and what it returns, which is particularly useful for APIs and larger codebases.
   - **Static Type Checking**: Tools like `mypy` can be used to statically check your code for type consistency, catching potential errors before runtime.

3. **Debate Around Type Hints**:
   - **Pythonic or Not?**: There is ongoing debate about whether using type hints is "pythonic." Python traditionally relies on duck typing, where the type of an object is less important than the methods and properties it has.
   - **Alternative Approaches**: Instead of type hints, some developers prefer using duck typing combined with `try-except` blocks to handle type-related issues dynamically.

4. **Practical Considerations**:
   - **Added Value**: Consider whether type hints add value to your project. If they improve readability, maintainability, or error detection, they can be a valuable tool.
   - **Use Wisely**: If you decide to use type hints, do so judiciously to avoid cluttering your code or making it unnecessarily complex.

5. **Future Reading**:
   - Exploring more about type hints, static type checking, and best practices can help you make informed decisions about their use in your projects.

Here's an example to illustrate some of these points:

```python
def add(a: int, b: int) -> int:
    return a + b

# The function works even with floats or strings
print(add(1.5, 2.5))  # Output: 4.0
print(add("hello", "world"))  # Output: helloworld

# Using mypy for static type checking
# Install mypy: pip install mypy
# Run mypy: mypy your_script.py
# mypy will flag the above calls as type errors
```

In this example, the `add` function is annotated to take two integers and return an integer. However, Python's dynamic nature allows it to work with floats and strings. Using a tool like `mypy` can help catch these inconsistencies statically.
"""