Calculator Emulator
A calculator application that integrates x86-64 assembly language for core arithmetic operations with a Python interface. This project demonstrates cross-language integration by combining the efficiency of low-level assembly code with the user-friendly features of Python.
Project Overview
This calculator emulator showcases the integration of assembly language and Python to create a functional application. The core arithmetic operations (addition, subtraction, multiplication, and division) are implemented in x86-64 assembly language for efficiency, while Python provides a user-friendly command-line interface. This project demonstrates practical applications of computer organization and architecture concepts through cross-language development.
Technical Implementation
Architecture
The calculator consists of two key components:

Assembly language implementation of basic arithmetic operations (add, subtract, multiply, divide)
Python wrapper that provides a user interface and connects to the assembly code via ctypes

This design separates the computation layer (assembly) from the interface layer (Python), demonstrating a modular architecture approach.
Assembly Implementation
The core calculator functions are implemented in x86-64 assembly language. The assembly code:

Takes advantage of CPU registers for efficient computation
Follows Windows x64 calling convention (arguments in RCX, RDX registers)
Returns results in the RAX register
Implements four basic operations: addition, subtraction, multiplication, and division

Python Interface
The Python component:

Uses ctypes to load and interact with the compiled assembly code
Defines proper function signatures to ensure correct data type handling
Provides a simple command-line interface for user interaction
Handles input validation and error cases (such as division by zero)

calculator.asm

The assembly file exports four functions that implement the basic arithmetic operations using x86-64 assembly. Each function follows the Windows x64 calling convention, taking parameters in RCX and RDX registers and returning results in RAX.

calculator.py

The Python script loads the compiled assembly functions as a shared library and provides type information for the function parameters and return values. It then implements a simple command-line interface for the calculator.
Setup and Usage
Prerequisites

Windows operating system
Python 3.x
NASM (Netwide Assembler)
GCC (GNU Compiler Collection)

Build Instructions

Assemble the calculator.asm file to create an object file:
nasm -f win64 calculator.asm -o calculator.obj

Compile the object file into a shared library (DLL):
gcc -shared -o libcalc.dll calculator.obj

Run the Python script:
python calculator.py


Usage Example
Enter first number: 18
Enter second number: 88
Choose operation (+ - * /): *
Result: 1584
Technical Challenges and Solutions

Windows x64 Calling Convention

The project required understanding and implementing the Windows x64 calling convention for assembly language, where:

The first argument is passed in RCX
The second argument is passed in RDX
The return value is expected in RAX




Foreign Function Interface

Using ctypes to bridge Python and assembly required careful definition of argument and return types to ensure proper data conversion between languages.


Division Implementation

Division in x86-64 assembly requires the use of the CQO instruction to extend the sign bit of RAX into RDX for proper handling of signed division with the IDIV instruction.



Learning Outcomes
This project demonstrates:

Practical application of assembly language programming
Integration of low-level code with high-level languages
Foreign function interface usage in Python
Cross-language development techniques
Building and using shared libraries

Future Enhancements
Potential improvements to this project could include:

Adding more complex mathematical operations (square root, power, etc.)
Implementing floating-point arithmetic
Creating a graphical user interface
Adding memory functions similar to a standard calculator
Implementing error handling for arithmetic exceptions

License
This project is available under the MIT License. See the LICENSE file for more details.
Acknowledgments

Developed as part of the Computer Organization and Architecture (ECE2002) course
Inspired by low-level programming concepts and cross-language development techniques
