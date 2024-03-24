## Immutable and Mutable Objects 🧠

In Python, objects are categorized as either mutable or immutable based on whether their state can be changed after creation.

### Immutable Objects 🚫

Immutable objects cannot be modified after creation. Any operation that seems to modify an immutable object actually creates a new object with the modified value. Examples of immutable objects in Python include:

### Examples:

#### Numbers:

```python
x = 5
y = x + 3
print(y)  # Output: 8
```

#### Strings:

```python
s = 'hello'
s += ' world'
print(s)  # Output: hello world

```

#### Tuples:

```python
t = (1, 2, 3)
t += (4,)
print(t)  # Output: (1, 2, 3, 4)
```

#### Boolean and NoneType:

```python
flag = True
flag = not flag
print(flag)  # Output: False

result = None
print(result) # Output: None
```

### Mutable Objects ✅

Mutable objects can be modified after creation. Changes to a mutable object affect its state directly. Examples of mutable objects in Python include:

### Examples:

#### Lists:

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]
```

#### Dictionaries:

```python
person = {'name': 'Alice', 'age': 30}
person['age'] = 31
print(person)  # Output: {'name': 'Alice', 'age': 31}
```

#### Sets:

```python
my_set = {'a', 'b', 'c'}
my_set.add('d')
print(my_set)  # Output: {'a', 'b', 'c', 'd'}
```

#### Bytearray:

```python
ba = bytearray(b'spam')
ba[0] = 98  # Modifying bytearray in place
print(ba)   # Output: bytearray(b'bpan')
```

### Memory Reference of Objects 🔍

In Python, when you create an object, it is stored in memory, and a reference to that memory location is returned. Immutable objects, once created, cannot be altered. Instead, when you perform an operation that seems to change the value, a new object is created with the modified value, and the reference is updated.

Mutable objects, on the other hand, can be modified directly because the reference points to the same memory location. Therefore, changes made to a mutable object affect its state immediately without the need to create a new object.
