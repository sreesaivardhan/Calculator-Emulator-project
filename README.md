#  Calculator Emulator

A calculator application that integrates **x86-64 assembly language** for core arithmetic operations with a **Python interface**. This project demonstrates cross-language integration by combining the efficiency of low-level assembly with the usability of Python.

---

##  Project Overview

This calculator emulator showcases the integration of **assembly language** and **Python** to create a functional application:

-  Core arithmetic operations (addition, subtraction, multiplication, division) are implemented in **x86-64 assembly language**.
-  A simple **command-line interface** is provided using **Python**.
-  Demonstrates practical concepts in **computer organization and architecture** and **cross-language development**.

---

##  Technical Implementation

###  Architecture

The calculator consists of two main components:

1. **Assembly language** code for core arithmetic operations  
2. **Python** wrapper using `ctypes` for interaction and user interface

This modular design separates the **computation layer** from the **interface layer**.

---

###  Assembly (x86-64)

- Uses CPU registers for efficient computation  
- Follows **Windows x64 calling convention**:  
  - `RCX` and `RDX` for arguments  
  - `RAX` for return value  
- Implements:
  - `add`: Addition  
  - `sub`: Subtraction  
  - `mul`: Multiplication  
  - `div`: Division (with `CQO` and `IDIV`)

---

### Python Interface

- Uses `ctypes` to call assembly functions from Python  
- Defines correct types for function arguments and return values  
- Provides input handling, error checking (e.g., division by zero), and output display via command line

---

## File Structure

calculator-emulator/
├── calculator.asm # Assembly file with arithmetic functions
├── calculator.py # Python script that interfaces with the DLL
├── libcalc.dll # Compiled shared library (built from calculator.asm)
└── README.md # Project documentation


---

##  Setup and Usage

###  Prerequisites

- Windows OS  
- [Python 3.x](https://www.python.org/)  
- [NASM](https://www.nasm.us/)  
- [GCC](https://www.mingw-w64.org/) (MinGW for Windows)

###  Build Instructions

1. **Assemble the assembly code**:

   nasm -f win64 calculator.asm -o calculator.obj

2.**Link it into a DLL**:

   gcc -shared -o libcalc.dll calculator.obj

3.**Run the Python calculator**:

   python calculator.py

## Usage Example
Enter first number: 18  
Enter second number: 88  
Choose operation (+ - * /): *  
Result: 1584

## Technical Challenges
Windows x64 Calling Convention
RCX – first argument

RDX – second argument

RAX – return value

Foreign Function Interface
Required careful ctypes type definitions to ensure compatibility between Python and assembly.

Division Handling
Used CQO to sign-extend RAX into RDX before calling IDIV for signed division

## Learning Outcomes
Hands-on experience with assembly language

How to build and use shared libraries

Using Python ctypes to interact with native code

Concepts in cross-language development

## Future Enhancements
Add floating-point arithmetic support

Implement advanced functions (√, ^, %, etc.)

Add GUI using Tkinter or PyQt

Extend to support memory functions

Improve exception and error handling
