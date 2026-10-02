# 1. What is a variable in Python, and why is it important?
# Answer: A variable is a named reference (or identifier) that points to an object in computer memory.
# In Python, variables do not store values directly; they act as labels or pointers bound to objects.
# Importance: They allow programmers to store, retrieve, label, modify, and reuse data dynamically
# throughout a program without hardcoding values or managing raw memory addresses.


# 2. How do you create a variable in Python?
# Answer: By writing a valid identifier name, followed by the assignment operator (=), and the value or expression.
# Python dynamically determines the type and allocates memory at runtime without explicit type declarations.
student_score = 95
student_name = "Maxwell"
is_registered = True


# 3. What rules must be followed when naming a Python variable?
# Answer:
# - Must begin with a letter (a-z, A-Z) or an underscore (_).
# - Cannot begin with a digit (0-9).
# - Can only contain alphanumeric characters and underscores (a-z, A-Z, 0-9, _). No spaces or special symbols allowed.
# - Case-sensitive: 'score', 'Score', and 'SCORE' are three completely distinct variables.
# - Cannot be any of Python's reserved keywords (e.g., if, for, while, def, class, return, import).
# - PEP 8 Convention: Variable names should use lowercase words separated by underscores (snake_case).


# 4. Why can a variable name not begin with a number?
# Answer: Python's lexical analyzer (tokenizer) identifies tokens from left to right. When it sees a leading digit,
# it immediately expects a numeric literal (such as an integer, float, or scientific notation like 10e3).
# If identifiers could start with digits, the parser could not distinguish between numbers and variable names (e.g., 123 vs 123var).


# 5. What is variable reassignment?
# Answer: Variable reassignment is the act of binding an existing variable name to a new value or object in memory.
counter = 1
counter = 5  # Reassigned to 5


# 6. What happens when you assign a new value to an existing variable?
# Answer:
# 1. Python creates (or references) the new object in memory.
# 2. The variable's reference pointer is redirected to point to the new object.
# 3. The reference count of the old object decreases by 1.
# 4. If no other variable references the old object, Python's garbage collector frees it from memory.


# 7. What is the difference between assigning a value and comparing two values?
# Answer:
# - Assignment (=): A statement that sets a variable on the left to reference the value/object on the right.
# - Comparison (==): An expression that checks if two values are equal and evaluates to a boolean (True or False).
x = 10        # Assignment
is_equal = (x == 10)  # Comparison -> True


# 8. Can one variable store different types of values at different times? Explain.
# Answer: Yes. Python is dynamically typed. Data types belong to the objects in memory, not the variable names.
# A variable name is merely a label that can be bound to any object type at runtime.
dynamic_var = 100          # int
dynamic_var = "Now text"   # str
dynamic_var = [1, 2, 3]    # list


# 9. What is multiple assignment in Python?
# Answer: Assigning values to multiple variables in a single line of code.
# Form 1: Simultaneous assignment / unpacking:
var_a, var_b, var_c = 10, 20, 30
# Form 2: Chained assignment (all point to the same object):
x_val = y_val = z_val = 0


# 10. How can you swap the values of two variables without creating a third variable?
# Answer: Using Python's tuple packing and unpacking syntax: a, b = b, a
num_a = 5
num_b = 10
num_a, num_b = num_b, num_a
# num_a is now 10, num_b is now 5


# 11. What is the difference between a variable and a constant in Python?
# Answer:
# - Variable: A named reference whose value can change throughout program execution.
# - Constant: A named identifier whose value is intended to remain unchanged.
# Python has no built-in 'const' keyword. By PEP 8 convention, constants are written in ALL_CAPS:
MAX_BUFFER_SIZE = 1024
PI = 3.1415926535


# 12. What happens when you try to use a variable that has not been defined?
# Answer: Python raises a NameError at runtime.
# Python looks for the name in the Local, Enclosing, Global, and Built-in (LEGB) scopes.
# If not found, execution halts: NameError: name 'my_variable' is not defined.


# 13. Why is it important to use meaningful variable names?
# Answer:
# - Improves readability and maintainability of the codebase.
# - Makes code self-documenting, reducing the need for excessive comments.
# - Prevents logic bugs during collaboration and long-term project maintenance.
# Example: 'student_average_score' is clear; 's' or 'x1' is ambiguous.


# 14. What is the difference between local and global variables?
# Answer:
# - Local Variable: Defined inside a function; accessible only within that function's scope; deleted when the function exits.
# - Global Variable: Defined outside any function at the module level; accessible by any function in the module.
# To modify a global variable inside a function, the 'global' keyword must be used.
app_status = "Online"  # Global

def check_status():
    local_msg = "Checking..."  # Local
    return f"{app_status}: {local_msg}"

# 15. What is a data type in Python?
# Answer: A data type is a classification that tells the Python interpreter what kind of value
# a piece of data holds, what operations can be performed on it, and how it is stored in memory.


# 16. What are the main built-in data types in Python?
# Answer:
# - Numeric: int, float, complex
# - Text: str
# - Sequence: list, tuple, range
# - Mapping: dict
# - Set Types: set, frozenset
# - Boolean: bool
# - Binary: bytes, bytearray, memoryview
# - None Type: NoneType (None)


# 17. What is the difference between an integer and a floating-point number?
# Answer:
# - Integer (int): Whole numbers (positive, negative, or zero) without a decimal point (e.g., 25, -7).
#   Python 3 ints have arbitrary precision (can grow as large as memory permits).
# - Floating-point number (float): Numbers containing a decimal point or exponential notation (e.g., 3.14, -0.5, 1e-4).
#   Stored in IEEE 754 64-bit double-precision format.


# 18. What is the difference between a number and a string containing a number?
# Answer:
# - A number (5) is of type int/float and supports arithmetic: 5 + 5 gives 10.
# - A string containing a number ("5") is text (str). The + operator concatenates: "5" + "5" gives "55".
# Mathematical operations like "5" - 2 raise a TypeError.


# 19. What is a Boolean data type?
# Answer: The bool data type represents logical truth values. In Python, bool is a subclass of int,
# where True behaves as 1 and False behaves as 0 in arithmetic operations.


# 20. What are the two possible Boolean values in Python?
# Answer: True and False (case-sensitive; must start with an uppercase letter).


# 21. What is a string, and how is it different from a number?
# Answer: A string (str) is an ordered, immutable sequence of Unicode characters enclosed in quotes ('...', "...", or """...""").
# Unlike numbers, strings represent text, support indexing (s[0]), slicing (s[1:4]), concatenation, and text methods,
# but cannot be used in arithmetic operations like division or subtraction.


# 22. What is a list in Python?
# Answer: A list is an ordered, mutable (changeable) collection of items enclosed in square brackets [...].
# Lists can contain items of different data types and allow duplicate values.
sample_list = [10, "Hello", 3.14, True, 10]


# 23. What is a tuple, and how is it different from a list?
# Answer: A tuple is an ordered, immutable sequence of elements enclosed in parentheses (...).
# Differences from list:
# - Mutability: Lists can be modified (items added, removed, changed); tuples cannot be altered after creation.
# - Syntax: Lists use square brackets []; tuples use parentheses ().
# - Hashability: Tuples of immutable items are hashable (can be dict keys or set items); lists cannot.
# - Performance: Tuples consume less memory and have faster creation/iteration overhead.
sample_tuple = (1, 2, 3)


# 24. What is a set, and what makes it different from a list?
# Answer: A set is an unordered, unindexed collection of unique, hashable elements defined using {...} or set().
# Differences from list:
# - Duplicates: Sets automatically eliminate duplicate entries; lists keep all duplicates.
# - Indexing: Sets cannot be indexed (s[0] raises TypeError); lists are indexed.
# - Lookup: Membership testing ('x in s') is O(1) constant time in a set, but O(n) linear time in a list.
sample_set = {1, 2, 3, 3, 2}  # Evaluates to {1, 2, 3}


# 25. What is a dictionary in Python?
# Answer: A dictionary (dict) is an ordered (since Python 3.7) collection of key-value pairs enclosed in curly braces {key: value}.
# Dictionaries provide fast lookup, insertion, and deletion by key via an underlying hash table.
sample_dict = {"name": "Maxwell", "score": 98}


# 26. What is the difference between a dictionary’s key and its value?
# Answer:
# - Key: The unique identifier used to look up an entry. Keys must be unique and immutable/hashable (e.g., str, int, tuple).
# - Value: The actual data associated with a key. Values can be of any data type, can contain duplicates, and are mutable.


# 27. Which Python data types are mutable, and which are immutable?
# Answer:
# - Mutable (can be modified in-place):
#   list, dict, set, bytearray
# - Immutable (cannot be modified after creation):
#   int, float, complex, str, tuple, frozenset, bytes, bool

# 28. Why would you choose a tuple instead of a list?
# Answer:
# 1. Data Integrity: Protects data from unintended modification (read-only safety).
# 2. Dictionary Keys / Set Items: Tuples are hashable, so they can be dictionary keys or set elements.
# 3. Memory & Speed: Tuples are more memory-efficient and faster to iterate over than lists.
# 4. Semantic Clarity: Signals that the collection represents a fixed record (e.g., RGB colors, latitude/longitude).

# 29. What is an operator in Python?
# Answer: An operator is a special symbol or keyword that instructs the interpreter to perform a specific
# mathematical, relational, logical, or bitwise operation on one or more operands (values or variables).

# 30. What are arithmetic operators used for?
# Answer: Used to perform standard mathematical calculations on numbers:
# + (addition), - (subtraction), * (multiplication), / (division), // (floor division), % (modulus), ** (exponentiation).

# 31. What is the difference between division and floor division?
# Answer:
# - Division (/): Always returns a float representing the exact quotient (e.g., 7 / 2 = 3.5, 4 / 2 = 2.0).
# - Floor Division (//): Divides and rounds down to the nearest lower integer (e.g., 7 // 2 = 3, -7 // 2 = -4).

# 32. What does the modulus operator do?
# Answer: The modulus operator (%) returns the remainder of integer division.
# Example: 10 % 3 = 1 (because 10 = 3 * 3 + 1). Used to check even/odd numbers (n % 2 == 0) and cyclic limits.

# 33. What is the purpose of the exponentiation operator?
# Answer: The exponentiation operator (**) raises a base number to the power of an exponent (base ** exp).
# Example: 2 ** 3 = 8 (2 cubed); 16 ** 0.5 = 4.0 (square root).

# 34. What are comparison operators used for?
# Answer: Used to compare two values or expressions. They evaluate conditions and return a boolean (True or False).
# Operators: ==, !=, >, <, >=, <=.

# 35. What is the difference between greater than and greater than or equal to?
# Answer:
# - Greater than (>): Returns True strictly when the left operand is larger than the right (5 > 5 is False).
# - Greater than or equal to (>=): Returns True if the left operand is larger than OR equal to the right (5 >= 5 is True).

# 36. What is the difference between the assignment operator and the equality operator?
# Answer:
# - Assignment operator (=): Stores a value into a variable (e.g., x = 5).
# - Equality operator (==): Compares two values for equality and returns True or False (e.g., x == 5).

# 37. What are logical operators?
# Answer: Operators used to combine or negate boolean conditions: 'and', 'or', and 'not'.

# 38. What is the difference between the and and or logical operators?
# Answer:
# - 'and': Returns True only if BOTH conditions are True. Uses short-circuiting: stops at the first False.
# - 'or': Returns True if AT LEAST ONE condition is True. Uses short-circuiting: stops at the first True.

# 39. What does the not operator do?
# Answer: A unary logical operator that inverts the boolean value of an expression.
# 'not True' becomes False; 'not False' becomes True.

# 40. What are assignment operators, and why are they useful?
# Answer: Assignment operators set values to variables. Compound assignment operators (+=, -=, *=, /=, //=, %=, **=)
# perform an operation and reassign the result in one step (e.g., x += 5 is x = x + 5).
# They make code cleaner, more concise, and optimize in-place modifications on mutable objects.

# 41. What is operator precedence?
# Answer: The order of rules determining which operations are evaluated first in a compound expression.
# Order: Parentheses () > Exponents ** > Unary (+, -) > Multiply/Divide (*, /, //, %) > Add/Subtract (+, -) > Comparisons > not > and > or.

# 42. Why is understanding operator precedence important when writing Python expressions?
# Answer:
# - Prevents logical bugs where expressions evaluate in an unintended order (e.g., 2 + 3 * 4 equals 14, not 20).
# - Helps programmers know when to use parentheses () to ensure accurate calculations and clear readability.

# 43. What is a conditional statement in Python?
# Answer: A control flow structure that allows a program to execute specific blocks of code
# only when specified boolean conditions evaluate to True.

# 44. Why are conditional statements important in programming?
# Answer: They give programs decision-making intelligence, allowing code to branch, handle varying user inputs,
# react to different states, manage errors, and avoid purely linear, inflexible execution.

# 45. What is the purpose of an if statement?
# Answer: To test an initial condition; if that condition evaluates to True, the indented code block executes.
# If False, the block is skipped.

# 46. What is the purpose of an else statement?
# Answer: To provide a default fallback block of code that runs whenever all preceding if and elif conditions evaluate to False.

# 47. When should you use an elif statement?
# Answer: When testing multiple mutually exclusive conditions in a chain.
# 'elif' (else if) only evaluates if all preceding if/elif conditions in that block evaluated to False.

# 48. What is the difference between using multiple if statements and using if, elif, and else?
# Answer:
# - Multiple if statements: Each 'if' condition is evaluated independently. Multiple blocks can execute.
# - if-elif-else chain: The conditions are linked; execution stops after the first True condition is found. At most one block executes.

# 49. What happens when the condition inside an if statement is false?
# Answer: Python skips the indented block under the if statement and continues to the next elif, else, or following statement.

# 50. Can an if statement contain another if statement? What is this called?
# Answer: Yes. This is called a nested conditional statement (or nested if).

# 51. What is a nested conditional statement?
# Answer: An if, elif, or else block placed inside the body of another if, elif, or else block.
# Used when a second decision depends on a prior condition being satisfied first.

# 52. How would you use conditional statements to determine whether a student passed or failed?
student_mark = 65
passing_mark = 50

if student_mark >= passing_mark:
    result_status = "Passed"
else:
    result_status = "Failed"


# 53. How would you create a grading system using conditional statements?
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 0:
        return "F"
    else:
        return "Invalid Score"


# 54. How would you determine whether a number is positive, negative, or zero using conditional statements?
def check_number_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


# 55. How would you determine the largest of three numbers using conditional statements?
def find_largest_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


# 56. What could happen if the conditions in an if and elif structure are arranged incorrectly?
# Answer: Since conditions are evaluated from top to bottom and Python exits after the first True condition,
# placing broader conditions before narrower/stricter conditions causes logic errors and unreachable code.
# Example: If 'score >= 50' is written before 'score >= 90', a score of 95 triggers the '>= 50' block,
# and the '>= 90' block will never execute.


# 57. What is a function in Python?
# Answer: A named, reusable block of organized code designed to carry out a specific task.
# Defined using the 'def' keyword, it can take inputs (parameters), perform logic, and return outputs.

# 58. Why are functions useful in programming?
# Answer:
# - Reusability (DRY - Don't Repeat Yourself): Write code once, call it anywhere.
# - Modularity: Breaks complex programs into smaller, isolated, manageable tasks.
# - Maintainability & Debugging: Simplifies finding and fixing bugs within specific functions.
# - Abstraction: Allows users to call a function knowing what it does without worrying about how it works internally.

# 59. What is the difference between defining a function and calling a function?
# Answer:
# - Defining a function (def func(): ...): Specifying the blueprint, name, parameters, and instructions. The code does not execute yet.
# - Calling a function (func()): Executing the function's instructions by using its name followed by parentheses () and passing arguments.

# 60. What is a function parameter?
# Answer: A variable listed inside the parentheses in a function's definition (def statement).
# It acts as a named placeholder for the input data the function expects.

# 61. What is a function argument?
# Answer: The actual concrete value or expression passed to the function when it is invoked.

# 62. What is the difference between a parameter and an argument?
# Answer:
# - Parameter: The variable name in the function header definition (the placeholder).
# - Argument: The actual value supplied during the function call (the input value).
# Example: In 'def greet(name):', 'name' is a parameter. In 'greet("Maxwell")', '"Maxwell"' is the argument.


# 63. What is the purpose of the return statement in a function?
# Answer:
# 1. Terminates the execution of the function immediately.
# 2. Sends the computed result/value back to the caller.
# If omitted or written without an expression, the function returns None.


# 64. What is the difference between returning a value and printing a value from a function?
# Answer:
# - print(): Displays text to the console screen for humans to see. It does not return data to the program (evaluates to None).
# - return: Passes a value back to the calling code so it can be stored in a variable, used in math, or passed to other functions.


# 65. What is a default parameter?
# Answer: A parameter that has a predefined fallback value in the function definition.
# If the caller does not supply that argument, the default value is automatically used.
def greet_user(name="Guest"):
    return f"Hello, {name}!"


# 66. Can a function have more than one parameter? Explain.
# Answer: Yes. Functions can define multiple parameters separated by commas.
# They can be passed positionally or as keyword arguments. Python also supports arbitrary parameters (*args, **kwargs).
def calculate_rectangle_area(length, width):
    return length * width


# 67. What happens when you call a function without providing a required argument?
# Answer: Python raises a TypeError at runtime stating that required positional arguments are missing.
# Example: TypeError: calculate_rectangle_area() missing 1 required positional argument: 'width'


# 68. What is the difference between a function that accepts input and a function that does not?
# Answer:
# - Accepts input: Has parameters defined; produces customized output depending on arguments passed (e.g., def square(x): return x*x).
# - Does not accept input: Has empty parentheses (); performs a fixed action or accesses global/system state (e.g., def get_time(): ...).


# 69. How can functions be combined with conditional statements to solve a problem?
# Answer: A function can encapsulate conditional branching (if-elif-else) to examine input arguments,
# validate data, and return different outcomes depending on conditions.
def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# 70. Challenge: Complete Student Assessment System
# Design a Python program that uses variables, different data types, operators,
# conditional statements, and multiple functions to calculate average, determine grade, and pass/fail status.

def calculate_average(scores):
    """Calculates the average score from a list of numbers."""
    total = sum(scores)
    count = len(scores)
    return total / count


def assign_grade(average):
    """Assigns an academic letter grade based on the average."""
    if average >= 90.0:
        return "A"
    elif average >= 80.0:
        return "B"
    elif average >= 70.0:
        return "C"
    elif average >= 60.0:
        return "D"
    elif average >= 50.0:
        return "E"
    else:
        return "F"


def check_pass_fail(average, pass_mark=50.0):
    """Determines if student passed or failed."""
    if average >= pass_mark:
        return "PASSED"
    else:
        return "FAILED"


def generate_student_report(student):
    """Combines all functions to generate a complete student report."""
    student_name = student["name"]             # str
    student_id = student["id"]                 # str
    student_scores = student["scores"]         # list of ints/floats

    average = calculate_average(student_scores) # float
    grade = assign_grade(average)               # str
    status = check_pass_fail(average)           # str

    print("=" * 45)
    print("         STUDENT ACADEMIC REPORT             ")
    print("=" * 45)
    print(f"Student Name   : {student_name}")
    print(f"Student ID     : {student_id}")
    print(f"Scores         : {student_scores}")
    print(f"Average Score  : {average:.2f}")
    print(f"Letter Grade   : {grade}")
    print(f"Final Status   : {status}")
    print("=" * 45)


# Execution demo
if __name__ == "__main__":
    student_record = {
        "name": "Maxwell Johnson",
        "id": "NOUN/2026/042",
        "scores": [85, 78, 92, 68, 84]
    }
    generate_student_report(student_record)
