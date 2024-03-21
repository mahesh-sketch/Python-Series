# Python Basic 🐍

## Explaining Python's Inner Workings 🧠

Python is an interpreted language, meaning it executes code line by line rather than compiling it into machine code beforehand like compiled languages such as C or C++. When you run a Python script, the Python interpreter reads the source code, tokenizes it, parses it into an Abstract Syntax Tree (AST), compiles it into bytecode, and then executes the bytecode using the PVM.

## What is \_\_pycache\_\_? 📦

When you import functions or modules from another file in Python, the interpreter compiles the source code into bytecode. This bytecode is then stored in a directory called **pycache** to speed up subsequent imports. The **pycache** directory contains compiled Python files (.pyc) which are used to execute the code more efficiently.

## Why Python Runs Bytecode and How PVM Executes It? ⚙️

Python runs bytecode for performance reasons. When you execute a Python script, the source code is first compiled into bytecode by the Python compiler. This bytecode is then executed by the Python Virtual Machine (PVM). The PVM is responsible for interpreting and executing the bytecode instructions. By using bytecode and the PVM, Python achieves platform independence and enables cross-platform execution of Python programs.
