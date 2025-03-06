
```
def our_sum(a, b):
    """
     Returns the sum of two values (numbers  or strings )!

     This function does:
    -  Arithmetic addition for numbers
    - String concatenation for text

     Parameters:
        a (int, float, str): First value 
        b (int, float, str): Second value (match a's type!)
     Returns:
         int/float if numbers: 2 + 3 → 5
         str if strings: "Hello" + "World" → "HelloWorld"

     Watch Out:
         TypeError if mixing types! (Number + Text = ❌)

     Examples:
         Number Magic:
        >>> our_sum(2, 3)
        5

         Text Wizardry:
        >>> our_sum("Hello", "World")
        'HelloWorld'

         Float Sorcery:
        >>> our_sum(2.5, 3.7)
        6.2
    """
    return a + b
```

**How to View:**  
```python
help(our_sum)  # Will show emojis if terminal supports them! 
``` 
