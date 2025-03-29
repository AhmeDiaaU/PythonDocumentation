# Modeling Real Systems

## Overview
To solve complex systems, we use classes that encapsulate related information into objects.

## Example: Employee Class

### Class Definition
```python
class Employee:
    name = None
    salary = None
    address = None
```

### Creating Instances
```python
ahmed = Employee()  # Creating an instance
ahmed.name = "Ahmed Diaa"
ahmed.salary = 20000
ahmed.address = "assuit"
```

### Creating Multiple Objects
```python
mohamed = Employee()
mohamed.name = "Mohamed"
mohamed.salary = 23123
mohamed.address = "Cairo"
```

## Diagram
```mermaid
graph TD;
    A[Employee Class] --> B[ahmed Instance]
    A --> C[mohamed Instance]
    B --> D[Name: Ahmed Diaa]
    B --> E[Salary: 20000]
    B --> F[Address: assuit]
    C --> G[Name: Mohamed]
    C --> H[Salary: 23123]
    C --> I[Address: Cairo]
```

## Key Points
- **Related Information:** Classes encapsulate related information.
- **Multiple Objects:** We can create multiple instances for each class.
- **Object Data:** Each object has its own data.

### Additional Notes
- Everything in Python is an object.