I'll enhance these notes with Obsidian styling and colors:

# Python Variable Scope and Namespaces

## <span style="color: #ff5733;">Conflicts Between Local and Global Variables</span>

> [!important]+ 🔄 Variable Shadowing When a local variable has the same name as a global variable, the local variable takes precedence within its scope.

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

## <span style="color: #33a8ff;">Namespaces</span>

> [!info]+ 📦 Namespace Definition A **namespace** is a container that holds variable names and their corresponding objects.

Python has four types of namespaces:

1. <span style="color: #d633ff;">**Built-in Namespace**</span>:
    
    - Contains built-in functions and variables like `len`, `max`, `TypeError`, etc.
    - Available throughout the program.
2. <span style="color: #33ff57;">**Global Namespace**</span>:
    
    - Contains names defined at the main program level.
    - Accessible from anywhere in the program.
3. <span style="color: #ff5733;">**Local Namespace**</span>:
    
    - Contains names defined within a function.
    - Exists only while the function is executing.
4. <span style="color: #33a8ff;">**Enclosing Namespace**</span>:
    
    - Relevant for nested functions (non-local scope).

## <span style="color: #33ff57;">Variable Search Order in Python</span>

> [!note]+ 🔍 LEGB Rule When a variable is used in a function, Python searches for it in the following order:

```mermaid
graph TD
    L[1. Local Namespace] --> E[2. Enclosing Namespace]
    E --> G[3. Global Namespace]
    G --> B[4. Built-in Namespace]
    B --> N[5. NameError]
    
    style L fill:#ff5733,color:white
    style E fill:#33a8ff,color:white
    style G fill:#33ff57,color:black
    style B fill:#d633ff,color:white
    style N fill:#ff3333,color:white
```

## <span style="color: #d633ff;">Viewing Namespaces</span>

> [!tip]+ 🔎 Namespace Inspection You can inspect the contents of namespaces using these functions:

```python
print(dir(__builtins__))  # Shows built-in names
print(globals())          # Shows global names
print(locals())           # Shows local names
```

## <span style="color: #ff9f33;">Best Practices for Global Variables</span>

> [!warning]+ ⚠️ Global Variable Usage
> 
> - **Avoid Overusing Global Variables**:
> - Using global variables is generally not efficient and can lead to bugs.
> - They can make code harder to debug and maintain.

> [!success]+ ✅ Proper Use Cases
> 
> - **When to Use Global Variables**:
> - Use global variables for **constants** that do not change.
> - Example:
>     
>     ```python
>     PI = 3.14  # Global constantMAX_CONNECTIONS = 100DATABASE_URL = "postgresql://user:pass@localhost/db"
>     ```
>     

## Key Takeaways

> [!important]+ 🗝️ Summary
> 
> 1. <span style="color: #ff5733;">**Local variables**</span> take precedence over global variables within their scope.
> 2. Python searches for variables in the order: <span style="color: #ff5733;">**Local**</span> → <span style="color: #33a8ff;">**Enclosing**</span> → <span style="color: #33ff57;">**Global**</span> → <span style="color: #d633ff;">**Built-in**</span>.
> 3. Use <span style="color: #33ff57;">**global variables**</span> sparingly and only for constants or shared data.
> 4. Use `globals()`, `locals()`, and `dir(__builtins__)` to inspect namespaces.

