Author:
Moulaye Adama Sidibé
THROBAC – Functional Roman Calculator
November 2025 (Date of the Program)

Description:
THROBAC is a Python console-based Roman Numeral Calculator.
This improved functional version restructures the original program into modular functions and adds full Roman numeral validation.

The program:
Converts Roman numerals to integers
Performs arithmetic operations
Converts results back to Roman numerals
Validates Roman numeral rules
Supports exponentiation
Allows continuous calculations until user exits

Features:
Roman Numeral Validation
Valid Roman characters only (I, V, X, L, C, D, M)
Repetition rule validation (no IIII, XXXX, etc.)
Subtractive notation validation (IV, IX, XL, XC, CD, CM)
Range validation (1–3999)

Supported Operations:
Addition (+)
Subtraction (−)
Multiplication (*)
Division (/ with quotient and remainder)
Exponentiation (^)

Program Structure:
Fully modular design(multiple functions)
Separate functions for:
Conversion
Validation
Arithmetic operations
Uses a main() function

Loop-based execution until user quits

How to Run:
Requirements
Python 3 installed

Run the Program:
Open terminal in the project folder and run:
python throbac_functional.py
Or on Windows:
py throbac_functional.py

Example:
Enter first Roman Number(no spaces): X
Enter second Roman Number(no spaces): V
Enter an operator(+,-,/,^,*): +

Output:
Value of X: 10
Value of V: 5
Operator: +
Digital sum is: 15
Roman Sum is: XV

Changes From Initial version:
Code refactored into reusable functions
Added Roman numeral validation rules
Increased supported range to 3999
Added exponentiation operator (^)
Added loop for repeated calculations
Improved program structure and readability
