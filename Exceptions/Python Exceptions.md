
### **What is an Exception?**
An **exception** is an unexpected event that occurs during program execution. For example:
```python
divide_by_zero = 7 / 0  # Raises ZeroDivisionError
```
This code causes an exception because dividing by zero is not allowed.

---

## **Python Logical Errors (Exceptions)**
Errors that occur at runtime (after passing the syntax test) are called **exceptions** or **logical errors**. They occur in situations like:
- Trying to open a file that doesn’t exist (`FileNotFoundError`).
- Dividing a number by zero (`ZeroDivisionError`).
- Importing a module that doesn’t exist (`ImportError`).

When these errors occur, Python creates an **exception object**. If not handled, it prints a **traceback** with details about the error.

#### Example:
```python
divide_numbers = 7 / 0
print(divide_numbers)
```
**Output:**
```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ZeroDivisionError: division by zero
```

---

## **Python Built-in Exceptions**
Python has many built-in exceptions that are raised when specific errors occur. You can view all built-in exceptions using:
```python
print(dir(locals()['__builtins__']))
```

#### Common Built-in Exceptions:
| **Exception**            | **Cause of Error**                                                                 |
|--------------------------|-----------------------------------------------------------------------------------|
| `AssertionError`          | Raised when an `assert` statement fails.                                          |
| `AttributeError`          | Raised when attribute assignment or reference fails.                              |
| `EOFError`                | Raised when `input()` hits end-of-file condition.                                 |
| `FileNotFoundError`       | Raised when a file or directory is not found.                                     |
| `ImportError`             | Raised when the imported module is not found.                                     |
| `IndexError`              | Raised when the index of a sequence is out of range.                              |
| `KeyError`                | Raised when a key is not found in a dictionary.                                   |
| `KeyboardInterrupt`       | Raised when the user hits the interrupt key (`Ctrl+C` or `Delete`).               |
| `MemoryError`             | Raised when an operation runs out of memory.                                      |
| `NameError`               | Raised when a variable is not found in local or global scope.                     |
| `TypeError`               | Raised when a function or operation is applied to an object of incorrect type.    |
| `ValueError`              | Raised when a function gets an argument of correct type but improper value.       |
| `ZeroDivisionError`       | Raised when the second operand of division or modulo operation is zero.           |

---

## **Python Errors vs Exceptions**
- **Errors**:
  - Represent conditions like syntax errors, logical errors, or system-related issues.
  - Usually beyond the programmer's control.
  - Examples: `SyntaxError`, `IndentationError`.

- **Exceptions**:
  - Can be caught and handled by the program.
  - Examples: `ZeroDivisionError`, `FileNotFoundError`.

---

## **Handling Exceptions**
Python provides `try`, `except`, and `finally` statements to handle exceptions. For example:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution complete.")
```

---

## **User-Defined Exceptions**
You can define custom exceptions in Python by creating a new class that inherits from Python's `Exception` class. For example:
```python
class CustomError(Exception):
    pass

raise CustomError("This is a custom error!")
```

---

## **Key Takeaways**
1. **Exceptions** are runtime errors that can be handled using `try`, `except`, and `finally`.
2. Python has many **built-in exceptions** for common errors.
3. **Errors** are usually beyond the programmer's control, while **exceptions** can be managed.
4. You can create **custom exceptions** for specific use cases.
