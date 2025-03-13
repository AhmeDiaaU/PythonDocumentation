# Python Closures and Scope

## Variable Identity in Closures

```python

def outer(x):

    y = 20

    print(id(y))  # Memory address of y in outer scope

    def inner(f):

        print(id(y))  # Same memory address as in outer scope

        return x + y + f

    return inner

  

if __name__ == '__main__':

    f = outer(10)  # x=10 is captured in the closure

    print(f(20))   # 10 + 20 + 20 = 50

    print(outer(100)(5))  # 100 + 20 + 5 = 125

```

```mermaid

flowchart TD

    A["outer(10)"] --> B["x=10, y=20"]

    B --> C["Create inner function"]

    C --> D["Return inner"]

    D --> E["f = inner with x=10, y=20"]

    E --> F["f(20)"]

    F --> G["Return 10+20+20 = 50"]

    H["outer(100)"] --> I["x=100, y=20"]

    I --> J["Create new inner function"]

    J --> K["Return inner"]

    K --> L["Call with (5)"]

    L --> M["Return 100+20+5 = 125"]

    style A fill:#f9f,stroke:#333,stroke-width:2px

    style B fill:#bbf,stroke:#333,stroke-width:2px

    style G fill:#fbb,stroke:#333,stroke-width:2px

    style H fill:#f9f,stroke:#333,stroke-width:2px

    style I fill:#bbf,stroke:#333,stroke-width:2px

    style M fill:#fbb,stroke:#333,stroke-width:2px

```


> **Key Point**: The `id(y)` prints show that the inner function references the exact same `y` variable from the outer scope, not a copy. This demonstrates true closure behavior.

## Basic Closure Diagram

```mermaid

flowchart TD

    A["Outer Function<br>Defines variables"] --> B["Inner Function<br>Accesses those variables"]

    B --> C["Return Inner Function"]

    C --> D["Inner Function<br>Still has access to<br>Outer Function variables"]

    style A fill:#f9f,stroke:#333,stroke-width:2px

    style B fill:#bbf,stroke:#333,stroke-width:2px

    style C fill:#dfd,stroke:#333,stroke-width:2px

    style D fill:#fbb,stroke:#333,stroke-width:2px

```

## Basic Closure Example

```python

def outer_function(x):

    y = 10

    def inner_function():

        return x + y

    return inner_function

  

closure1 = outer_function(5)

closure2 = outer_function(10)

  

print(closure1())  # 15 (5 + 10)

print(closure2())  # 20 (10 + 10)

```
## Late Binding Problem

```python

def fun():

    lst = []

    for i in range(3):  # i: 0, 1, 2

        def f():

            return i  # All functions reference the same i

        lst.append(f)

    # At this point, i = 2

    return lst

  

lst = fun()

for f in lst:

    print(f())  # Prints: 2, 2, 2

```

```mermaid

flowchart TD

    A["for i in range(3)"] --> B["Create f"]

    B --> C["Append f to lst"]

    A --> D["Loop ends with i = 2"]

    D --> E["All functions reference same i"]

    E --> F["All return 2"]

    style A fill:#f9f,stroke:#333,stroke-width:2px

    style D fill:#fbb,stroke:#333,stroke-width:2px

    style E fill:#bbf,stroke:#333,stroke-width:2px

    style F fill:#ffcccc,stroke:#333,stroke-width:2px

```

  

## Solution to Late Binding: Default Parameters

```python

def fun():

    lst = []

    for i in range(3):

        def f(i=i):  # Each function gets its own copy of i

            return i  # Values: 0, 1, 2

        lst.append(f)

    return lst

  

lst = fun()

for f in lst:

    print(f())  # Prints: 0, 1, 2

```

```mermaid

flowchart TD

    A["for i in range(3)"] --> B["Create f(i=i)<br>with default param"]

    B --> C["Append f to lst"]

    D["i = 0"] --> E["f with i=0"]

    F["i = 1"] --> G["f with i=1"]

    H["i = 2"] --> I["f with i=2"]

    style A fill:#f9f,stroke:#333,stroke-width:2px

    style B fill:#bbf,stroke:#333,stroke-width:2px

    style E fill:#ccffcc,stroke:#333,stroke-width:2px

    style G fill:#ccffcc,stroke:#333,stroke-width:2px

    style I fill:#ccffcc,stroke:#333,stroke-width:2px

```

## Using `nonlocal` Keyword
```python

def counter_factory():

    count = 0  # ← Enclosed variable

    def increment():

        nonlocal count  # ← Access to enclosed variable

        count += 1

        return count

    return increment  # ← Return inner function

```

```mermaid

flowchart TD

    A["counter_factory<br>defines count=0"] --> B["increment function<br>accesses count"]

    A --> C["Returns increment"]

    C --> D["increment + count=0"]

    D --> E["Call increment<br>count becomes 1"]

    E --> F["Call increment<br>count becomes 2"]

    style A fill:#f9f,stroke:#333,stroke-width:2px

    style B fill:#bbf,stroke:#333,stroke-width:2px

    style C fill:#dfd,stroke:#333,stroke-width:2px

    style D fill:#fbb,stroke:#333,stroke-width:2px

```

  

## Database Example with Closures

```python

def init():

    class CustomersDatabase:

        def load_database(self):

            nonlocal users_ids  # Access users_ids from outer scope

            users_ids += [3, 4]  # Modify the outer variable

        def add_id(self, id):

            if id not in users_ids:

                print(f"Adding {id}")

                users_ids.append(id)

                print(users_ids)

            else:

                print(f"{id} is already there")

    users_ids = [1, 2]  # Create the enclosed variable

    db = CustomersDatabase()

    db.load_database()  # Modify users_ids → [1,2,3,4]

    return db.add_id  # Return method with access to users_ids

```

```mermaid

flowchart TD

    A["init function"] --> B["users_ids = [1,2]"]

    A --> C["CustomersDatabase"]

    C --> D["load_database<br>adds [3,4]"]

    C --> E["add_id method"]

    A --> F["Return add_id<br>with access to users_ids"]

    subgraph "Memory After init"

        G["users_ids = [1,2,3,4]"]

        H["add_id function"]

    end

    F --> I["go1 calls add_id"]

    I --> J["users_ids = [1,2,3,4,5]"]

    J --> K["go2 calls add_id"]

    K --> L["users_ids = [1,2,3,4,5,6]"]

    style A fill:#f9f,stroke:#333,stroke-width:2px

    style F fill:#fbb,stroke:#333,stroke-width:2px

    style G fill:#bbf,stroke:#333,stroke-width:2px

```

## DRY Principle (Don't Repeat Yourself)

  

```mermaid

flowchart TD

    A["Repeated Code<br>❌"] --> B["Extract to Function<br>✅"]

    style A fill:#ffcccc,stroke:#333,stroke-width:2px

    style B fill:#ccffcc,stroke:#333,stroke-width:2px

```

## Practical Example: Configurable Logger

```python

def create_logger(level):

    def logger(message):

        if level == "DEBUG":

            print(f"[DEBUG] {message}")

        elif level == "INFO":

            print(f"[INFO] {message}")

        elif level == "WARNING":

            print(f"[WARNING] {message}")

        elif level == "ERROR":

            print(f"[ERROR] {message}")

    return logger

  

debug_log = create_logger("DEBUG")

error_log = create_logger("ERROR")

  

debug_log("This is a debug message")  # [DEBUG] This is a debug message

error_log("System failure")           # [ERROR] System failure

```

  

## Closure Applications

  

```mermaid
mindmap
  root((Closures))
    Data Encapsulation
        Private variables
        Information hiding
    Function Factories
        Create specialized functions
        Customize behavior
    State Maintenance
        Remember between calls
        Avoid global variables
    Decorators
        Enhance functions
        Add functionality
    Callbacks
        Event handlers
        Asynchronous code
```

## Best Practices

```mermaid

flowchart TD

    A["Use closures sparingly"] --> B["Document nonlocal variables"]

    B --> C["Be aware of late binding"]

    C --> D["Consider classes for complex state"]

    style A fill:#ccffcc,stroke:#333,stroke-width:2px

    style B fill:#ccffcc,stroke:#333,stroke-width:2px

    style C fill:#ffcccc,stroke:#333,stroke-width:2px

    style D fill:#ccffcc,stroke:#333,stroke-width:2px

```

## Key Takeaways

  

1. **Closures** capture and preserve the enclosing function's scope

2. **nonlocal** allows modifying variables from outer scopes

3. **Default parameters** solve the late binding problem

4. **DRY** principle encourages reusable inner functions

5. **Encapsulation** keeps implementation details private