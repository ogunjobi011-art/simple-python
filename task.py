# 1. What is a variable in Python?
# Answer: A variable is a named reference (or label) that points to an object in memory.
# 2. How do you create a variable in Python?
# Answer: By assigning a value to a name using the assignment operator (=).
x = 10
# 3. Can variable names start with a number? Example: 1name = "Max"
# Answer: No! Variable names cannot start with a digit. It causes a SyntaxError.
# 4. Write code to create a variable called age with value 25
age = 25
# 5. Write code to create name = "Kelechi"
name = "Kelechi"
# 6. What will x = 5; y = x; print(y) output?
# Answer: 5
x = 5
y = x
print("Q6:", y)
# 7. How do you check the type of a variable?
# Answer: Using the built-in type() function.
print("Q7:", type(age))
# 8. What is the difference between = and ==?
# Answer: '=' is the assignment operator; '==' is the comparison operator (checks equality).
# 9. Can you change the value of a variable after creating it?
# Answer: Yes, Python variables can be dynamically reassigned at any time.
# 10. What is variable assignment?
# Answer: Binding a variable name to an object in memory using '='.
# 11. Create 3 variables in one line: a=1, b=2, c=3
a, b, c = 1, 2, 3
# 12. What is the output of a, b = 10, 20; print(a, b)?
# Answer: 10 20
a, b = 10, 20
print("Q12:", a, b)
# 13. Swap two variables a=5, b=10 without a third variable
a = 5
b = 10
a, b = b, a
print("Q13 swapped:", a, b) 
 # a is 10, b is 5
# 14. What are the rules for naming variables in Python?
# Answer:
# - Must start with a letter (a-z, A-Z) or an underscore (_)
# - Cannot start with a number
# - Can only contain letters, numbers, and underscores (a-z, A-Z, 0-9, _)
# - Case-sensitive (age, Age, AGE are different)
# - Cannot use reserved keywords (like if, class, def)
# 15. Which is valid: my-var, my_var, my var?
# Answer: my_var is the only valid name.
# 16. Is Name and name the same variable?
# Answer: No, Python is case-sensitive.
# 17. What is a constant? How do we write it in Python?
# Answer: A variable whose value is intended not to change. By convention (PEP 8), written in ALL_CAPS.
MAX_LIMIT = 100
# 18. Create a variable PI = 3.14
PI = 3.14
# 19. What happens if you write x = 10; x = 20; print(x)?
# Answer: Outputs 20 because the variable x is reassigned/overwritten.
# 20. How do you delete a variable?
# Answer: Using the 'del' keyword.
temp_var = 100
del temp_var
# 21. Create variable school = "Noun"
school = "Noun"
# 22. Create is_student = True
is_student = True
# 23. What is the output of name = "Attah"; print(name * 2)?
# Answer: AttahAttah (string repetition)
print("Q23:", "Attah" * 2)
# 24. Fix this: 2nd_name = "Maxwell"
# Fix: Variables cannot start with digits.
second_name = "Maxwell"
# 25. Fix this: class = "Python"
# Fix: 'class' is a reserved keyword.
class_name = "Python"
# 26. What does id() do with a variable?
# Answer: Returns the unique memory address identifier of the object.
print("Q26 id:", id(school))
# 27. What is None? Create a variable with None
# Answer: None represents the absence of a value (null).
empty_val = None
# 28. Assign same value "Python" to 3 variables x,y,z in one line
x = y = z = "Python"
# 29. What is dynamic typing? Give example
# Answer: Variable types are determined automatically at runtime and can change.
dynamic_var = 10      # int
dynamic_var = "Text"  # now str
# 30. Create variable price = 100 then increase it by 50 using shorthand
price = 100
price += 50
print("Q30 price:", price)
# 31. What is snake_case? Give example
# Answer: Words written in lowercase separated by underscores.
# Example: student_first_name = "John"
# 32. What is camelCase? Give example
# Answer: First word lowercase, following words capitalized with no spaces.
# Example: studentFirstName = "John"
# 33. Which naming is Python standard for variables?
# Answer: snake_case (PEP 8 standard).
# 34. What will print(x) output if x was never created?
# Answer: Raises NameError: name 'x' is not defined.
# 35. Create a variable storing your full name, age, and state
my_profile = {"full_name": "Kelechi Attah", "age": 25, "state": "Lagos"}
# 36. a=10; b=20; a=b; print(a)
# Output: 20
a = 10; b = 20; a = b
print("Q36:", a)
# 37. x="5"; y="10"; print(x+y)
# Output: 510 (string concatenation)
print("Q37:", "5" + "10")
# 38. x=5; y=10; print(x+y)
# Output: 15 (integer addition)
print("Q38:", 5 + 10)
# 39. a=True; print(type(a))
# Output: <class 'bool'>
print("Q39:", type(True))
# 40. num = 10; num = num + 5; print(num)
# Output: 15
num = 10
num = num + 5
print("Q40:", num)
# 41. a=5; a+=3; print(a)
# Output: 8
a = 5
a += 3
print("Q41:", a)
# 42. a=10; b=a; b=20; print(a)
# Output: 10 (integers are immutable, a remains 10)
a = 10; b = a; b = 20
print("Q42:", a)
# 43. x,y = 5; Why error?
# Answer: TypeError: cannot unpack non-iterable int object.
# Unpacking requires an iterable on the right side with matching count (e.g. x, y = 5, 5).
# 44. first_name = "John"; last_name="Doe"; print(first_name + last_name)
# Output: JohnDoe
print("Q44:", "John" + "Doe")
# 45. first_name = "John"; last_name="Doe"; print(first_name + " " + last_name)
# Output: John Doe
print("Q45:", "John" + " " + "Doe")
# 46. How do you take user input and store in a variable?
# Answer: user_data = input("Enter prompt: ")

# 47. Write code to ask for name and print "Hello "
# name_input = input("Enter your name: ")
# print(f"Hello {name_input}")

# 48. What is the difference between local and global variable?
# Answer:
# - Local variable: Defined inside a function, accessible only within that function.
# - Global variable: Defined outside functions, accessible throughout the module.

# 49. Write a program with global keyword
counter = 0
def increment_counter():
    global counter
    counter += 1
increment_counter()
print("Q49 global counter:", counter)

# 50. What is del keyword? Example
# Answer: Deletes a variable name or reference from memory.
sample = "hello"
del sample
# 51. Can a variable store function? Example: x = print
# Answer: Yes, functions are first-class objects in Python.
my_printer = print
my_printer("Q51: Function stored in a variable!")
# 52. What is variable shadowing?
# Answer: When a local variable inside a function shares the same name as a global variable, hiding the global one inside the local scope.
# 53. Create variable with value containing apostrophe: I'm a student
quote_str = "I'm a student"  # or 'I\'m a student'
# 54. How to make a variable value not changeable? Can we in Python?
# Answer: Python has no native const keyword. We use UPPERCASE naming by convention,
# or immutable structures like tuples, frozenset, or typing.Final.
# 55. What is _ variable used for in Python?
# Answer:
# 1. Throwaway variable when a value is intentionally ignored (e.g. for _ in range(3)).
# 2. In interactive REPL, holds the result of the last evaluated expression.
# 56. What is output: x=10; y=20; x,y=y,x; print(x,y)
# Output: 20 10
x, y = 10, 20
x, y = y, x
print("Q56:", x, y)
# 57. Create variable a = 100 inside function and outside. Which prints?
# Answer: Inside the function, the local variable prints. Outside, the global prints.
# 58. What are keywords? Can we use them as variable names?
# Answer: Reserved words with special predefined meanings in Python syntax.
# No, they cannot be used as variable names.
# 59. List 5 Python keywords
# Answer: if, elif, else, while, for (also: def, class, return, True, False, import)
# 60. What is type() vs isinstance()?
# Answer:
# - type(x) returns the exact type and does not consider inheritance.
# - isinstance(x, Class) checks if x is an instance of Class OR any subclass of it.
# 61. Create variable my_list that holds 3 names
my_list = ["Ada", "Chidi", "Emeka"]
# 62. Create variable data that holds dict {"name":"Max", "age":20}
data = {"name": "Max", "age": 20}
# 63. Explain x = y = z = 0
# Answer: Chained assignment. All three variables reference the exact same integer object 0.
# 64. What is unpacking? a,b,c = [1, 2, 3]
# Answer: Assigning each element of an iterable to individual variables in order.
a, b, c = [1, 2, 3]
# 65. What is output: a=[1, 2]; b=a; b.append(3); print(a)
# Output: [1, 2, 3] because both a and b point to the same mutable list in memory.
a = [1, 2]
b = a
b.append(3)
print("Q65:", a)
# 66. How to make copy of variable not reference?
# Answer: Use .copy(), slicing [:], list(a), or copy.deepcopy(a).
original = [1, 2]
cloned = original.copy()
# 67. What is memory reference for variables?
# Answer: Variables store pointers (memory addresses) to objects, not the raw data values directly.
# 68. Write code to print all variables created so far
# print(dir())  # or print(locals())
# 69. What is difference between x is None and x == None?
# Answer:
# 'x is None' checks identity (same memory singleton), which is faster and recommended.
# 'x == None' calls equality method __eq__(), which can be overridden.
# 70. Create a variable for your phone number. Should it be int or string? Why?
# Answer: String! Because:
# 1. Preserves leading zeros (e.g. "08012345678").
# 2. Supports symbols like '+' or '-'.
# 3. Phone numbers are identifiers, not numbers to do math on.
phone_number = "08012345678" 
# 71. what are the 4 main data types in Python?
# Answer: int, float, str, bool
# 72.list 3 numerical data types in Python
# Answer: int, float, complex
# 73. what is the difference between int and float?
# Answer: int is whole numbers without decimal points, float is numbers with decimal points.
# 74. what is string data type in Python?
# Answer: A sequence of characters enclosed in single, double, or triple quotes.
# 75. what is boolean data type in Python? what value does it hold?  
# Answer: A data type that can only have two values: True or False.
# 76.  76. What type is 10? What type is 10.5?
# Answer: 10 is int; 10.5 is float.
# 77. What type is "10"?
# Answer: str (string).
# 78. What type is 'a'?
# Answer: str (Python has no single-character char type).
# 79. What type is True?
# Answer: bool (boolean).
# 80. What type is [1, 2, 3]?
# Answer: list.
# 81. What type is (1, 2, 3)?
# Answer: tuple.
# 82. What type is {1, 2, 3}?
# Answer: set.
# 83. What type is {"a": 1}?
# Answer: dict (dictionary).
# 84. What type is None?
# Answer: NoneType.
# 85. How to check data type?
# Answer: Using type(variable) or isinstance(variable, expected_type).
# 86. Convert int 10 to string
print("Q86:", str(10))
# 87. Convert "10" to int
print("Q87:", int("10"))
# 88. What happens: int("hello")?
# Answer: Raises ValueError: invalid literal for int() with base 10: 'hello'
# 89. Convert float 10.5 to int. What happens?
# Answer: int(10.5) gives 10. It truncates (chops off) the decimal portion.
print("Q89:", int(10.5))
# 90. Convert int 0 to bool. What is result?
# Answer: False
print("Q90:", bool(0))
# 91. Convert int 1 to bool
# Answer: True
print("Q91:", bool(1))
# 92. Convert empty string "" to bool
# Answer: False (empty strings are falsy)
print("Q92:", bool(""))
# 93. What is str(100) + str(200)?
# Output: "100200"
print("Q93:", str(100) + str(200))
# 94. What is int("10.5")? Will it work?
# Answer: No, it raises ValueError! You must convert to float first: int(float("10.5")).
# 95. How to convert list to tuple?
my_tuple = tuple([1, 2, 3])
print("Q95:", my_tuple)
# 96. How do you create a string? Give 3 ways
s1 = 'Single quote'
s2 = "Double quote"
s3 = """Triple quote"""
# 97. What is difference between single ' and double "?
# Answer: No semantic difference. Single quotes can enclose double quotes directly, and vice versa.
# 98. How to create multi-line string?
multi_str = """This is line 1
This is line 2"""
# 99. What is output: len("Python")
# Output: 6
print("Q99:", len("Python"))
# 100. What is s[0] if s="Python"?
# Output: 'P'
print("Q100:", "Python"[0])
# 101. What is slicing? s[0:3] for s="Python"
# Answer: Extracting part of a sequence [start:stop:step]. "Python"[0:3] gives 'Pyt'.
print("Q101:", "Python"[0:3])
# 102. What is s[-1] for s="Python"?
# Output: 'n' (last character)
print("Q102:", "Python"[-1])
# 103. What does "python".upper() do?
# Output: "PYTHON"
print("Q103:", "python".upper())
# 104. What does "PYTHON".lower() do?
# Output: "python"
print("Q104:", "PYTHON".lower())
# 105. What is string concatenation? Example
# Answer: Joining strings together using +.
print("Q105:", "Hello" + " " + "World")
# 106. Can we multiply string? "Hi" * 3?
# Answer: Yes, gives "HiHiHi".
print("Q106:", "Hi" * 3)
# 107. What is f-string? Example
# Answer: Formatted string literal prefixed with 'f' to embed expressions in {}.
user_score = 95
print(f"Q107: Score is {user_score}")
# 108. Write f-string: name="Max", age=20 => "My name is Max and I am 20"
m_name = "Max"
m_age = 20
print(f"Q108: My name is {m_name} and I am {m_age}")
# 109. What is strip()?
# Answer: A string method that removes leading and trailing whitespace/characters.
print("Q109:", "  hello  ".strip())
# 110. How to check if "python" is inside "I love python"?
print("Q110:", "python" in "I love python")  # True
# 111. What is list? Is it mutable?
# Answer: An ordered, indexed collection of items. Yes, it is mutable.
# 112. What is tuple? Is it mutable?
# Answer: An ordered, indexed collection of items. No, it is immutable.
# 113. Difference between list and tuple?
# Answer:
# - Lists use [] and are mutable (can add, remove, change items).
# - Tuples use () and are immutable (cannot be changed after creation).
# 114. What is dict? Give example
# Answer: A collection of key-value pairs.
student = {"name": "Tolu", "grade": "A"}
# 115. What is set? Give example
# Answer: An unordered collection of unique elements.
unique_nums = {1, 2, 3}
# 116. Can set have duplicate values?
# Answer: No. Duplicates are automatically removed.
# 117. Can list have different data types? Example
# Answer: Yes.
mixed_list = [10, "Hello", 3.14, True]
# 118. What is mutable vs immutable? List 2 each
# Answer:
# Mutable: Can be changed in-place (e.g. list, dict).
# Immutable: Cannot be changed in-place (e.g. int, str, tuple).
# 119. What is output: a=[1, 2]; a[0]=99; print(a)
# Output: [99, 2]
a_list = [1, 2]
a_list[0] = 99
print("Q119:", a_list)
# 120. What is output: a=(1,2); a[0]=99; print(a) Will it work?
# Answer: No, raises TypeError: 'tuple' object does not support item assignment.
# 121. What type is []?
# Answer: list
# 122. What type is ()?
# Answer: tuple
# 123. What type is {}? Is it dict or set?
# Answer: dict (empty dictionary).
# 124. How to create empty set?
empty_set = set()
# 125. How to create empty dict?
empty_dict = {}  # or dict()
# 126. What is type([]) vs type({})?
# Answer: <class 'list'> vs <class 'dict'>
# 127. What is indexing?
# Answer: Accessing a specific element in a sequence using its numeric index (starting at 0).
# 128. What is output: len([1, 2, 3, 4])
# Output: 4
print("Q128:", len([1, 2, 3, 4]))
# 129. What is bool([]) vs bool([0])?
# Answer: bool([]) is False (empty list); bool([0]) is True (list contains an element).
print("Q129:", bool([]), bool([0]))
# 130. What is bool("") vs bool(" ")?
# Answer: bool("") is False (empty string); bool(" ") is True (contains a space).
print("Q130:", bool(""), bool(" "))
# 131. Write code to check if variable x is integer using isinstance()
check_x = 42
print("Q131:", isinstance(check_x, int))
# 132. What is complex data type? Example: 3+5j
# Answer: A number with a real part and an imaginary part (j).
comp = 3 + 5j
print("Q132:", comp.real, comp.imag)
# 133. How many data types can a list hold at once?
# Answer: Unlimited / any combination of types.
# 134. Convert list = [1, 2, 2, 3] to set. What happens?
# Answer: set([1, 2, 2, 3]) becomes {1, 2, 3} (duplicate 2 removed).
print("Q134:", set([1, 2, 2, 3]))
# 135. What is NoneType?
# Answer: The type of the singleton object None, denoting absence of a return/value.
# 136. What is difference between == and is for data types?
# Answer: == checks equality of values; 'is' checks whether they are the identical memory object.
# 137. Write code that takes input and prints its data type
# user_val = input("Enter something: ")
# print("Type is:", type(user_val))  # Always str from input()
# 138. Create variable for each data type: int, float, str, bool, list, tuple, dict, set
v_int = 1
v_float = 2.5
v_str = "Python"
v_bool = True
v_list = [1, 2]
v_tuple = (1, 2)
v_dict = {"a": 1}
v_set = {1, 2} 
# 139. What will type(True) return? Is bool subclass of int?
# Answer: Returns <class 'bool'>. Yes, bool is a subclass of int in Python.
print("Q139:", type(True), issubclass(bool, int))
# 140. Explain why 0.1 + 0.2 != 0.3 in Python
# Answer: Due to binary floating-point representation (IEEE 754), 0.1 and 0.2 cannot be
# represented exactly in binary base-2. 0.1 + 0.2 evaluates to 0.30000000000000004.
print("Q140:", 0.1 + 0.2 == 0.3, "Actual:", 0.1 + 0.2)
# 141. List 7 arithmetic operators in Python
# Answer: + (add), - (subtract), * (multiply), / (divide), // (floor divide), % (modulus), ** (exponent)
# 142. What is +? Give example
print("Q142 (+):", 5 + 3)  # 8
# 143. What is -? Example
print("Q143 (-):", 10 - 4)  # 6
# 144. What is *? Example
print("Q144 (*):", 4 * 3)  # 12
# 145. What is /? Example. What type does it return?
# Answer: Division operator. Always returns a float.
print("Q145 (/):", 8 / 2, type(8 / 2))  # 4.0 <class 'float'>
# 146. What is //? Example
# Answer: Floor division (divides and truncates down to nearest whole number).
print("Q146 (//):", 7 // 2)  # 3
# 147. What is %? Example. What is 10 % 3?
# Answer: Modulus operator (returns remainder). 10 % 3 = 1.
print("Q147 (%):", 10 % 3)
# 148. What is **? What is 2**3?
# Answer: Exponentiation operator (power). 2 ** 3 = 8.
print("Q148 (**):", 2 ** 3)
# 149. What is output: 10 / 3
# Output: 3.3333333333333335
print("Q149:", 10 / 3)
# 150. What is output: 10 // 3
# Output: 3
print("Q150:", 10 // 3)
# 151. What is output: 10 % 3
# Output: 1
print("Q151:", 10 % 3)
# 152. What is operator precedence? What is 2 + 3 * 4?
# Answer: The order of evaluation (BODMAS/PEMDAS). Multiplication takes precedence over addition: 2 + 12 = 14.
print("Q152:", 2 + 3 * 4)
# 153. What is 2 ** 3 ** 2? Explain
# Answer: 512. Exponentiation binds right-to-left: 3 ** 2 = 9, then 2 ** 9 = 512.
print("Q153:", 2 ** 3 ** 2)
# 154. Calculate area of rectangle: length=10, width=5
rect_length = 10
rect_width = 5
rect_area = rect_length * rect_width
print("Q154 Area:", rect_area)
# 155. Calculate simple interest using operators: (P * R * T) / 100
p, r, t = 1000, 5, 2
si = (p * r * t) / 100
print("Q155 Simple Interest:", si)
# 156. List 6 comparison operators
# Answer: ==, !=, >, <, >=, <=
# 157. What is ==? Example
print("Q157 (==):", 5 == 5)  # True
# 158. What is !=? Example
print("Q158 (!=):", 5 != 3)  # True
# 159. What is > and <?
print("Q159 (> and <):", 10 > 5, 2 < 1)  # True, False
# 160. What is >= and <=?
print("Q160 (>= and <=):", 5 >= 5, 4 <= 3)  # True, False
# 161. What is output: 5 == 5.0
# Output: True (values are numerically equal)
print("Q161:", 5 == 5.0)
# 162. What is output: "5" == 5
# Output: False (different types)
print("Q162:", "5" == 5)
# 163. What is output: 10 > 5
# Output: True
print("Q163:", 10 > 5)
# 164. What is output: True == 1
# Output: True (in Python bool inherits from int where True == 1)
print("Q164:", True == 1)
# 165. What is output: False == 0
# Output: True (False == 0)
print("Q165:", False == 0)
# 166. What are and, or, not?
# Answer: Logical operators:
# - and: True if both conditions are True
# - or: True if at least one condition is True
# - not: Reverses the boolean state
# 167. What is output: True and False
# Output: False
print("Q167:", True and False)
# 168. What is output: True or False
# Output: True
print("Q168:", True or False)
# 169. What is output: not True
# Output: False
print("Q169:", not True)
# 170. What is output: 5>3 and 10>5
# Output: True
print("Q170:", 5 > 3 and 10 > 5)
# 171. What is output: 5>10 or 10>5
# Output: True
print("Q171:", 5 > 10 or 10 > 5)
# 172. List 5 assignment operators
# Answer: =, +=, -=, *=, /= (also //=, %=, **=)
# 173. What is +=? Example
val = 5
val += 3  # val = val + 3
print("Q173 (+=):", val)  # 8
# 174. What is -=? Example
val = 10
val -= 4  # val = val - 4
print("Q174 (-=):", val)  # 6
# 175. What is *=? Example
val = 4
val *= 3  # val = val * 3
print("Q175 (*=):", val)  # 12
# 176. What is /=? Example
val = 10
val /= 2  # val = val / 2
print("Q176 (/=):", val)  # 5.0
# 177. What is x+=1 same as?
# Answer: x = x + 1
# 178. What is difference between = and +=?
# Answer: '=' assigns a brand new value; '+=' adds a value to the current variable and reassigns.
# 179. What is in operator? Example
# Answer: Checks if an item exists within an iterable.
print("Q179 (in):", 'a' in 'apple')  # True
# 180. What is not in? Example
# Answer: Checks if an item does not exist within an iterable.
print("Q180 (not in):", 'z' not in 'apple')  # True
# 181. What is is operator? Example
# Answer: Identity operator that checks if both variables point to the exact same object in memory.
val_none = None
print("Q181 (is):", val_none is None)  # True
# 182. What is difference between is and ==?
# Answer: '==' checks value equality; 'is' checks memory reference/identity.
# 183. What is output: a=[1, 2]; b=[1, 2]; a==b vs a is b
a_obj = [1, 2]
b_obj = [1, 2]
print("Q183:", a_obj == b_obj, a_obj is b_obj)  # True False
# 184. What is output: "a" in "apple"
# Output: True
print("Q184:", "a" in "apple")
# 185. What is output: 3 in [1, 2, 3]
# Output: True
print("Q185:", 3 in [1, 2, 3])
# 186. What is output: "key" in {"key":1}
# Output: True
print("Q186:", "key" in {"key": 1})
# 187. Does it check values or keys in dict?
# Answer: By default, it checks KEYS (use dict.values() to check values).
# 188. What is bitwise &, |? Example
# Answer: Bitwise AND (&) and bitwise OR (|) operating on binary bits.
# 5 is 0101, 3 is 0011 -> 5 & 3 = 0001 (1), 5 | 3 = 0111 (7)
print("Q188 (&, |):", 5 & 3, 5 | 3)
# 189. What is ternary operator in Python? Example: a=10 if x>5 else 20
# Answer: A single-line conditional: value_if_true if condition else value_if_false
test_x = 8
ternary_result = 10 if test_x > 5 else 20
print("Q189:", ternary_result)
# 190. Write program using ternary to check even/odd
num_check = 7
parity = "Even" if num_check % 2 == 0 else "Odd"
print("Q190 Parity:", parity)
# 191. What is operator chaining? Example: 1<2<3
# Answer: Linking comparisons without multiple 'and' statements.
# 1 < 2 < 3 is evaluated as (1 < 2) and (2 < 3) -> True.
print("Q191:", 1 < 2 < 3)
# 192. What is output: 10 + 20 * 30 / 10
# Output: 70.0 (20 * 30 = 600; 600 / 10 = 60.0; 10 + 60.0 = 70.0)
print("Q192:", 10 + 20 * 30 / 10)
# 193. How to force precedence? Using brackets ()
print("Q193:", (10 + 20) * (30 / 10))  # 90.0
# 194. Write code: Take two numbers and print +, -, *, /, %, //
def demo_arithmetic(n1, n2):
    print(f"{n1} + {n2}  = {n1 + n2}")
    print(f"{n1} - {n2}  = {n1 - n2}")
    print(f"{n1} * {n2}  = {n1 * n2}")
    print(f"{n1} / {n2}  = {n1 / n2}")
    print(f"{n1} % {n2}  = {n1 % n2}")
    print(f"{n1} // {n2} = {n1 // n2}")
# 195. Write code: Take age and check if age >=18 using comparison
def check_adulthood(person_age):
    return "Adult" if person_age >= 18 else "Minor"
# 196. Write code: Check if number divisible by both 3 and 5 using logical operator
def check_div_3_and_5(number):
    return number % 3 == 0 and number % 5 == 0
# 197. Write code: Check if letter is vowel using in operator
def is_vowel(char):
    return char.lower() in "aeiou"
# 198. Write code: Use assignment operator to double a number 3 times
double_num = 5
double_num *= 2  # 10
double_num *= 2  # 20
double_num *= 2  # 40
print("Q198 Doubled 3 times:", double_num)
# 199. Explain BODMAS in Python
# Answer:
# B - Brackets: ()
# O - Orders (exponents): **
# D / M - Division and Multiplication: /, //, %, * (evaluated left-to-right)
# A / S - Addition and Subtraction: +, - (evaluated left-to-right)
# 200. Create small calculator using all arithmetic operators
def run_calculator(num1, num2):
    print("=== Mini Calculator ===")
    print(f"{num1} + {num2}  = {num1 + num2}")
    print(f"{num1} - {num2}  = {num1 - num2}")
    print(f"{num1} * {num2}  = {num1 * num2}")
    if num2 != 0:
        print(f"{num1} / {num2}  = {num1 / num2}")
        print(f"{num1} // {num2} = {num1 // num2}")
        print(f"{num1} % {num2}  = {num1 % num2}")
    else:
        print("Division by zero is undefined")
    print(f"{num1} ** {num2} = {num1 ** num2}")
run_calculator(10, 3)
# 201
user_name = input("Enter your name: ")
print(user_name.upper())
# 202
# x = 10; del x; print(x) raises NameError.
# 203
a, b = 10, "10"
# a + b raises TypeError because int and str cannot be added.
# 204
a, b = "Python", "Java"
a, b = b, a
# 205
a, b, c = 5, 10, 15
print("Q205:", a + b + c)  # 30
# 206
x = 50
print("Q206:", id(x))
# 207
first, last = "Attah", "Maxwell"
full_name = f"{first} {last}"
# 208
# Valid: __name, _age, age_, age2
# Invalid: 2age
# 209
x = 5
x = x + x
x = x + x
print("Q209:", x)  # 20
# 210
count = 0
while count < 10:
    count += 1
print("Q210:", count)
# 211
# Python is dynamically typed, so types are assigned at runtime.
# 212
# data = [1][2][3] raises IndexError.
data = [1, 2, 3]
data2 = data
data2[0] = 99
print("Q212:", data)  # [99, 2, 3]
# 213
data = [1, 2, 3]
data2 = data.copy()
data2[0] = 99
# 214
student1, student2, student3 = "Ada", "Chidi", "Emeka"
students = [student1, student2, student3]
print("Q214:", students)
# 215
# globals() returns global variables; locals() returns current local variables.
# 216
student_maths_score_2024 = 85
# 217
x, y = 10, 20
print(x, y) if x > y else print(y, x)  # Valid; prints 20 10
# 218
a, b = 10, 20
result = a if a > b else b
print("Q218:", result)
# 219
# Emoji identifiers such as 😀 = 10 are invalid syntax.
# Python identifiers may contain some Unicode letters, but emojis are not valid identifiers.
# 220
a, _b, c = [1, 2, 3]
# _b receives a value that is usually intended to be ignored.
# 221
price, qty = 19.99, 3
total = price * qty
print("Q221:", total)
# 222
input_name = input("Name: ")
input_age = int(input("Age: "))
print(input_name, input_age)
# 223
# x = 10 uses an integer literal.
# x = int(10) explicitly converts 10 to int; both produce an int.
# 224
is_logged_in = False
is_logged_in = not is_logged_in
print("Q224:", is_logged_in)
# 225
a = None
print("Q225:", a is None)  # True
# 226
x = 10
def my_func():
    x = 5
    print("Inside:", x)
my_func()
print("Outside:", x)
# 227
# Use uppercase naming by convention.
MAX_CONNECTIONS = 100
# 228
text = "NOUN"
length = len(text)
print("Q228:", length)
# 229
name = "Kelechi"
name = name + " Noun"
print("Q229:", name)
# 230
# Backslashes create escape sequences such as \n.
file_path = r"C:\new\folder"
# Alternative: file_path = "C:\\new\\folder"
# 231
print("Q231:", type(1 / 2))  # float
# 232
print("Q232:", type(2 // 2))  # int
# 233
# "True" is a string; True is a boolean.
# 234
print(int(True), int(False))  # 1 0
# 235
print("Q235:", str(True) + str(False))  # TrueFalse
# 236
print("Q236:", bool("False"))  # True; non-empty strings are truthy.
# 237
value = ""
print(value == "", len(value) == 0)
# 238
s = " python is easy "
s = s.strip().upper().replace("EASY", "POWERFUL")
print("Q238:", s)
# 239
# "python"[100] raises IndexError.
# 240
print("Q240:", "python"[1:100])  # ython; no error
# 241
# Strings are immutable. "python"[0] = "P" raises TypeError.
# 242
s = "python"
print("Q242:", s[::-1])
# 243
print("Q243:", len(" "), len(""))  # 1 0
# 244
age = "20"
age = int(age) + 5
print("Q244:", age)
# 245
print(list("abc"))   # ['a', 'b', 'c']
print(["abc"])       # ['abc']
# 246
print("Q246:", [1, 2, 3] * 2)  # [1, 2, 3, 1, 2, 3]
# 247
print("Q247:", (1, 2, 3) * 2)
# 248
# Dictionaries do not support multiplication by an integer.
# 249
# Lists cannot be dictionary keys because they are mutable.
example_dict = {(1, 2): "tuple key"}  # Tuples can be keys.
# 250
print("Q250:", set([1, 1, 2, 2, 3]))  # {1, 2, 3}
# 251
numbers_set = {1, 2}
numbers_set.add(3)
# 252
numbers_list = [1, 2]
numbers_list.append(3)
# 253
items = [1, 2, 3]
result = items.append(4)
print("Q253:", items, result)  # append returns None
# 254
a = [1, 2]
b = a
b = [3, 4]
print("Q254:", a)  # [1, 2]
# 255
tuple_value = (1, 2, 3)
list_value = list(tuple_value)
list_value.append(4)
tuple_value = tuple(list_value)
# 256
d = {"name": "Max", "dept": "NOUN"}
keys = list(d.keys())
values = list(d.values())
print("Q256:", keys, values)
# 257
values = [1, 2]
print(isinstance(values, list), type(values) == list)
# isinstance() is usually better because it supports subclasses.
# 258
# None can represent a missing value or an uninitialized result.
result = None
# 259
infinity = float("inf")
print("Q259:", infinity, type(infinity))
# 260
print("Q260:", int(True) + int(False) + int(True))  # 2
# 261
x = 10.5
if isinstance(x, int):
    kind = "int"
elif isinstance(x, float):
    kind = "float"
else:
    kind = "other"
print("Q261:", kind)
# 262
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
# Shallow copies share nested objects; deep copies copy nested objects too.
# 263
a = "5"
b = int(a)
c = float(b)
print("Q263:", c)  # 5.0
# 264
different_types = [10, 2.5, "Python", True, [1, 2]]
# 265
print("Q265:", bool([0]))  # True; the list is non-empty.
# 266
# bytes is immutable binary data; bytearray is mutable binary data.
# 267
text_number = str(123)
decimal_number = float("123")
print(text_number, decimal_number)
# 268
# ["a"]["b"]["c"] raises TypeError because list indices must be integers.
# 269
complex_number = complex(2, 3)
print("Q269:", complex_number)  # (2+3j)
# 270
user_value = input("Enter a value: ")
try:
    converted_value = int(user_value)
    detected_type = type(converted_value)
except ValueError:
    converted_value = user_value
    detected_type = type(converted_value)
print(converted_value, detected_type)
# 271
print("Q271:", 2 * 3 * 2)  # 6 * 2 = 12
# 272
print("Q272:", -3 * 2)  # -6
# 273
print("Q273:", (-3) ** 2)  # 9
# 274
print("Q274:", 10 + 3 * 2 ** 2)  # 22
# 275
weight, height = 70, 1.75
bmi = weight / (height ** 2)
print("Q275:", bmi)
# 276
x = 15
print("Q276:", 10 <= x <= 20)
# 277
print("Q277:", 5 == 5 and 10 == 10 and 15 == 20)  # False
# 278
print("Q278:", 5 == 5 or 10 == 20 or 15 == 20)  # True
# 279
print("Q279:", not (5 > 3))  # False
# 280
print(not 0, not 1, not "")  # True False True
# 281
print(False and (10 / 0))  # False; the division is not evaluated.
# 282
print(True or (10 / 0))  # True; the division is not evaluated.
# 283
print(10 % 2 == 0 and 10 % 3 == 0)  # False
print(15 % 2 == 0 and 15 % 3 == 0)  # False
# 284
number = 14
print(number % 2 == 0)
# 285
number = 12
print(number % 2 == 0 and number > 10)
# 286
a = 5
a += 2 ** 3
print("Q286:", a)  # 13
# 287
x = 10
x //= 3
print("Q287:", x)  # 3
# 288
x = 2
x *= 3
x *= 2
print("Q288:", x)  # 12
# 289
# x = x + 1 creates and assigns a new result.
# x += 1 is augmented assignment and may update mutable objects in-place.
# 290
print("Q290:", "ab" in "abc" and "d" not in "abc")  # True
# 291
letter = input("Enter a letter: ")
print(letter.lower() in "python")
# 292
a, b = 1000, 1000
print(a is b)  # Implementation-dependent; do not use is for value comparison.
a, b = 10, 10
print(a is b)  # Often True because of integer interning.
# 293
print([] == [], [] is [])  # True False
# 294
a, b, c = 5, 5, 5
same_value = a == b and b == c
print(same_value)
# 295
if (n := len([1, 2, 3])) > 2:
    print("Q295:", n)
# 296
def repeat_input():
    while True:
        value = input("Enter text (or exit): ")
        if value.lower() == "exit":
            break
        print(value)

# repeat_input()
# 297
print("Q297:", 10 & 2)  # 2
# 298
print("Q298:", 10 | 2)  # 10
# 299
a, b = 5, 10
a ^= b
b ^= a
a ^= b
print("Q299:", a, b)
# 300
def mini_calculator():
    first = float(input("First number: "))
    operator = input("Operator (+, -, *, /, %, //, **): ")
    second = float(input("Second number: "))

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        result = first / second
    elif operator == "%":
        result = first % second
    elif operator == "//":
        result = first // second
    elif operator == "**":
        result = first ** second
    else:
        result = "Invalid operator"

    print("Result:", result)

# mini_calculator()