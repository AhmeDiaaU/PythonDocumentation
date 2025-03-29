# Python Variable Scope and Namespaces

## Conflicts Between Local and Global Variables

**Variable Shadowing**: When a local variable has the same name as a global variable, the local variable takes precedence within its scope.

### Example Code:

```python
b = 20  # Global variable
c = 6   # Global variable

def f1():
    b = c + 1  # Local variable 'b' is created
    print(b)   # Prints 7 (local variable)
    return b

print(b)  # Prints 20 (global variable)
b = f1()  # Calls the function and assigns its return value to 'b'
print(b)  # Prints 7 (global variable is now updated)
```

## Namespaces

**Namespace Definition**: A namespace is a container that holds variable names and their corresponding objects.

Python has four types of namespaces:

1. **Built-in Namespace**:
    - Contains built-in functions and variables like `len`, `max`, `TypeError`, etc.
    - Available throughout the program.
2. **Global Namespace**:
    - Contains names defined at the main program level.
    - Accessible from anywhere in the program.
3. **Local Namespace**:
    - Contains names defined within a function.
    - Exists only while the function is executing.
4. **Enclosing Namespace**:
    - Relevant for nested functions (non-local scope).

## Variable Search Order in Python

**LEGB Rule**: When a variable is used in a function, Python searches for it in the following order:
1. Local Namespace
2. Enclosing Namespace
3. Global Namespace
4. Built-in Namespace

## Viewing Namespaces

**Namespace Inspection**: You can inspect the contents of namespaces using these functions:

```python
print(dir(__builtins__))  # Shows built-in names
print(globals())          # Shows global names
print(locals())           # Shows local names
```

## Best Practices for Global Variables

**Global Variable Usage**:
- Avoid Overusing Global Variables:
  - Using global variables is generally not efficient and can lead to bugs.
  - They can make code harder to debug and maintain.

**Proper Use Cases**:
- When to Use Global Variables:
  - Use global variables for constants that do not change.
  - Example:
    ```python
    PI = 3.14  # Global constant
    MAX_CONNECTIONS = 100
    DATABASE_URL = "postgresql://user:pass@localhost/db"
    ```

## Key Takeaways

1. Local variables take precedence over global variables within their scope.
2. Python searches for variables in the order: Local → Enclosing → Global → Built-in.
3. Use global variables sparingly and only for constants or shared data.
4. Use `globals()`, `locals()`, and `dir(__builtins__)` to inspect namespaces.
