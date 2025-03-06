## **Conflicts Between Local and Global Variables**
When a local variable has the same name as a global variable, the local variable takes precedence within its scope.

### **Example Code**:
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

---

## **Namespaces**
A **namespace** is a container that holds variable names and their corresponding objects. Python has four types of namespaces:

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

---

### **Variable Search Order in Python**
When a variable is used in a function, Python searches for it in the following order:
1. **Local Namespace**: Is the variable defined locally?
2. **Enclosing Namespace**: Is the variable defined in an enclosing function?
3. **Global Namespace**: Is the variable defined globally?
4. **Built-in Namespace**: Is the variable a built-in function or object?
5. If none of the above, Python raises a `NameError`.

---

### **Viewing Namespaces**
You can inspect the contents of namespaces using:
```python
print(dir(__builtins__))  # Shows built-in names
print(globals())          # Shows global names
print(locals())           # Shows local names
```

---

## **Best Practices for Global Variables**
- **Avoid Overusing Global Variables**:
  - Using global variables is generally not efficient and can lead to bugs.
  - They can make code harder to debug and maintain.

- **When to Use Global Variables**:
  - Use global variables for **constants** that do not change (e.g., `pi = 3.14`).
  - Example:
    ```python
    PI = 3.14  # Global constant
    ```

---

### **Key Takeaways**:
1. **Local variables** take precedence over global variables within their scope.
2. Python searches for variables in the order: **Local → Enclosing → Global → Built-in**.
3. Use **global variables sparingly** and only for constants or shared data.
4. Use `globals()`, `locals()`, and `dir(__builtins__)` to inspect namespaces.
