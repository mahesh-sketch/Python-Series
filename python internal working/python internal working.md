# Internal Working Of Python 🐍

## Exploring Immutable Objects in Python 🧠

In Python, immutable objects like numbers behave in a specific way when assigned to variables and manipulated. Let's take a closer look:

```python
# Create an integer object with value 5 and store it in memory
x = 5

# Create a reference 'y' pointing to the same memory location as 'x'
y = x

# Print the values of 'x' and 'y'
print("Value of x:", x)  # Output: 5
print("Value of y:", y)  # Output: 5

# Change the value of 'x'
x = 10

# Print the values of 'x' and 'y' after modification
print("Modified value of x:", x)  # Output: 10
print("Value of y:", y)            # Output: 5
```

Explanation:

🔹 When x = 5 is executed, Python creates an integer object with the value 5 and assigns it to the variable x. This object is stored in memory.

🔹 When y = x is executed, Python creates a reference y that points to the same memory location as x.

🔹 After modifying x to 10, a new integer object with value 10 is created and stored in memory. The variable x is then updated to reference this new object. However, y still references the original object with value 5.

## Exploring Mutable Objects in Python 🧠

In Python, mutable objects like lists behave differently compared to immutable objects when assigned to variables and manipulated. Let's explore:

```python
# Create a list object and store it in memory
numbers = [1, 2, 3]

# Create a reference 'copy_numbers' pointing to the same memory location as 'numbers'
copy_numbers = numbers

# Modify the list by appending a new element
numbers.append(4)

# Print the values of 'numbers' and 'copy_numbers'
print("Modified list 'numbers':", numbers)       # Output: [1, 2, 3, 4]
print("Value of 'copy_numbers':", copy_numbers)  # Output: [1, 2, 3, 4]
```

Explanation:

🔹 When numbers = [1, 2, 3] is executed, Python creates a list object [1, 2, 3] and assigns it to the variable numbers. This list object is stored in memory.

🔹 When copy_numbers = numbers is executed, Python creates a reference copy_numbers that points to the same memory location as numbers. Both variables reference the same list object.

🔹 After modifying the numbers list by appending 4, the list object is updated in memory. Since copy_numbers points to the same memory location, it reflects the changes made to the list as well.