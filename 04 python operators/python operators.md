# Exploring Operators in Python 🧮

Operators are fundamental constructs in Python for performing operations on variables and values. Let's dive into various operators and explore them:

### Arithmetic Operators

Arithmetic operators are used for mathematical operations such as addition, subtraction, multiplication, division, etc.

```python
x = 10
y = 3

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y

print("Addition:", addition)         # Output: 13
print("Subtraction:", subtraction)   # Output: 7
print("Multiplication:", multiplication) # Output: 30
print("Division:", division)         # Output: 3.3333333333333335
```

### Relational Operators

Relational operators are used to compare values. They return True or False based on the comparison.

```python
x = 10
y = 5

greater_than = x > y
less_than = x < y
equal_to = x == y
not_equal_to = x != y

print("Greater than:", greater_than)      # Output: True
print("Less than:", less_than)            # Output: False
print("Equal to:", equal_to)              # Output: False
print("Not equal to:", not_equal_to)      # Output: True
```

### Logical Operators

Logical operators are used to combine conditional statements. They return True or False based on the conditions.

```python

x = 10
y = 5

logical_and = (x > 5) and (y < 10)
logical_or = (x > 5) or (y > 10)
logical_not = not(x > 5)

print("Logical AND:", logical_and)    # Output: True
print("Logical OR:", logical_or)      # Output: True
print("Logical NOT:", logical_not)    # Output: False
```

### Conditional Operator (Ternary Operator)

The conditional operator is used for conditional expressions. It returns one of two values depending on whether a given condition is true or false.

```python

x = 10
y = 5

result = "x is greater" if x > y else "y is greater"
print("Result:", result)   # Output: x is greater
```
