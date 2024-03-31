# Nested Functions and Closures in Python 🔄

## Nested/Inner Function 🔍

A function which is defined inside another function is known as a nested or inner function. Nested functions are scoped inside their parent function.

```python
def parent_function():
    print("Hi from PARENT function")

    def child_function():
        print("Hi from CHILD function")

    child_function()

parent_function()
```

Nested functions are not directly accessible outside of the parent function. If we try calling `child_function` outside of `parent_function`, we will get errors.

Python Error: `NameError`: name `child_function` is not defined

## Closure 📦

Closure is a function that remembers values/variables after execution.

Let's write a "multiplier" using closure.

```python
def multiply_by(factor):
    def wrapper(n):
        return n * factor

    return wrapper

multiply_by_2 = multiply_by(2)
print(multiply_by_2(5))  # Output: 10
```

Here, we are calling `multiply_by` function with argument 2 (`factor=2`). The `wrapper` function inherits the argument (`factor`) from the outer function. `multiply_by_2` stores the reference of the `wrapper` function returned by `multiply_by` function.

We’re calling `multiply_by_2` with argument 5 (`n = 5`) and getting result 10 (`n*factor = 5*2=10`). Here's the twist! We’re not passing the value of `factor`, `multiply_by_2` function "remembers" the previous value of `factor` (2).
