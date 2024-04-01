# Object-Oriented Programming (OOP) in Python 🐍

Object-Oriented Programming (OOP) is a programming paradigm that revolves around the concept of objects. Objects are instances of classes, which encapsulate data and behavior. OOP promotes modularity, reusability, and extensibility in code.

## Key Concepts of OOP:

### 1. Classes and Objects

- **Definition:** A class is a blueprint for creating objects. It defines the attributes and methods that an object will have.
- **Real-life Example:** Consider a class `Car` with attributes like `brand`, `model`, and `color`, and methods like `start_engine()` and `drive()`. Each individual car (object) created from this class would have its own specific brand, model, and color, and can perform actions like starting the engine and driving.
- **Syntax Example:**

```python
  class Car:
      def __init__(self, brand, model, color):
          self.brand = brand
          self.model = model
          self.color = color

      def start_engine(self):
          print("Engine started.")

      def drive(self):
          print("Car is moving.")
```

### 2. Objects

- **Definition:** The object is an entity that has a state and behavior associated with it. It may be any real-world object like a mouse, keyboard, chair, table, pen, etc. Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.

An object consists of:

- **State:** It is represented by the attributes of an object. It also reflects the properties of an object.
- **Behavior:** It is represented by the methods of an object. It also reflects the response of an object to other objects.
- **Identity:** It gives a unique name to an object and enables one object to interact with other objects.

### 3. Encapsulation

- **Definition:** Encapsulation is the bundling of data and methods that operate on the data into a single unit (class). It hides the internal state of an object and only exposes the necessary functionalities.

- **Real-life Example:** Think of a television remote control. It encapsulates the functionalities (like changing channels, adjusting volume) and the state (current channel, battery status) within a single device.

- **Syntax Example:**

```python
class TVRemote:
   def __init__(self):
       self.current_channel = 1
       self.battery_status = 100

   def change_channel(self, channel):
       self.current_channel = channel

   def adjust_volume(self, volume):
       # Implementation
       pass
```

### 4. Inheritance

- **Definition:** Inheritance allows a class (subclass) to inherit properties and behavior from another class (superclass). It promotes code reuse and establishes a hierarchical relationship between classes.

- **Real-life Example:** Consider a class Animal with properties and methods common to all animals. Subclasses like Dog and Cat can inherit from the Animal class and add their own specific properties and methods.

- **Syntax Example:**

```python

class Animal:
def make_sound(self):
pass

class Dog(Animal):
def make_sound(self):
print("Woof!")

class Cat(Animal):
def make_sound(self):
print("Meow!")
```

### 5. Polymorphism

- **Definition:** Polymorphism simply means having many forms. Polymorphism allows objects to be treated as instances of their superclass.

- **Real-life Example:** In a zoo management system, a feed() method can be defined in a superclass Animal. Each subclass (Lion, Elephant, Monkey) can implement its own version of the feed() method based on its specific dietary requirements.

- **Syntax Example:**

```python
class Animal:
def feed(self):
pass

class Lion(Animal):
def feed(self):
print("Feeding meat.")

class Elephant(Animal):
def feed(self):
print("Feeding grass.")

class Monkey(Animal):
def feed(self):
print("Feeding bananas.")
```

### 6. Abstraction

- **Definition:** Abstraction refers to the concept of hiding complex implementation details and showing only the essential features of an object. It simplifies the interaction with objects by providing a clear interface.

- **Real-life Example:** When driving a car, you interact with its interface (steering wheel, pedals) without needing to understand the inner workings of the engine or transmission system.

- **Syntax Example:**

```python
class Car:
def **init**(self, brand, model, color):
self.brand = brand
self.model = model
self.color = color

    def start_engine(self):
        print("Engine started.")

    def drive(self):
        print("Car is moving.")
```
