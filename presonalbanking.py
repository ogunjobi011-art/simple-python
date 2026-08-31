# A variable is a named container in memory used to store data. In Python:
#  1. Basic integer assignment
# 2. Basic string assignment
# user_name = "Alex"
# 3. Basic float assignment
# account_balance = 1500.75
# 4. Basic boolean flag
# is_logged_in = True
# 5. Reassigning a variable to a new value
# score = 10
# score = 25  # score is now 25
# 6. Dynamic typing (changing the data type of an existing variable)
# data = 100        # integer
# data = "Pending"  # now it's a string
# 7. Multiple assignment in a single line
# x, y, z = 10, 20, 30
# 8. Assigning the same value to multiple variables
# total = counter = initial_value = 0
# 9. Variable using Python's snake_case naming standard
# max_withdrawal_limit = 5000
# # 10. Swapping two variables without a temporary variable
# a = 5
# b = 10
# a, b = b, a  # a is now 10, b is now 5
# # 11. Storing the result of an arithmetic expression
# price = 50
# tax = 0.08
# total_price = price + (price * tax)
# # 12. Augmented assignment (updating a variable in place)
# wallet = 100
# wallet += 50   # wallet is now 150 (same as wallet = wallet + 50)
# # 13. String concatenation using variables
# first_name = "Jane"
# last_name = "Doe"
# full_name = first_name + " " + last_name
# # 14. Variable formatting using f-strings
# product = "Laptop"
# cost = 999.99
# message = f"The {product} costs ${cost:.2f}"
# # 15. Storing None (representing the absence of a value or null state)
# session_token = None
# # 16. Constant convention (uppercase naming indicates it shouldn't be modified)
# MAX_LOGIN_ATTEMPTS = 3
# PI = 3.14159
# # 17. Storing a collection (list) in a variable
# bank_transactions = [100.0, -25.50, 200.0, -50.0]
# # 18. Storing a dictionary (key-value structure) in a variable
# customer_profile = {"id": 101, "name": "Sarah", "active": True}
# # 19. Initializing a variable from a built-in function return value
# password = "supersecretpass"
# password_length = len(password)  # 15
# # 20. Variable scope in a loop
# total_sum = 0
# for number in [1, 2, 3, 4, 5]:
#     total_sum += number  # total_sum is 15

# A data type defines the kind of value a variable can hold and what operations can be performed on it.
# Common built-in types in Python:
# Numbers:`int`, `float`, `complex`
# Text: `str`
# Boolean: `bool` (`True` or `False`)
# Sequences & Collections:`list`, `tuple`, `range`, `dict`, `set`, `frozenset`
# Binary & Special: `bytes`, `bytearray`, `NoneType`
# You can check any variable's type using `type(variable)`.
# # 1. Integer (int) - positive and negative whole numbers
# user_id = 4509
# # 2. Large Integer (with underscores for readability)
# national_debt = 1_000_000_000  # 1000000000
# # 3. Float (float) - decimal numbers
# interest_rate = 0.045
# # 4. Float using scientific notation
# scientific_value = 1.5e-4  # 0.00015
# # 5. Complex Number (complex) - real and imaginary parts
# impedance = 3 + 4j
# # 6. Single-line String (str)
# greeting = "Welcome to your account"
# # 7. Multi-line String (str)
# email_template = """Dear Customer,
# Your statement is ready for download.
# Thank you."""
# # 8. Boolean True (bool)
# has_overdraft_protection = True
# # 9. Boolean False (bool)
# is_account_locked = False
# # 10. List (list) - ordered, mutable collection
# currencies = ["USD", "EUR", "GBP", "JPY"]
# # 11. Tuple (tuple) - ordered, immutable collection (cannot be altered)
# branch_coordinates = (40.7128, -74.0060)
# # 12. Dictionary (dict) - key-value pairs
# account = {"account_number": "ACC123", "tier": "Gold", "balance": 7450.00}
# # 13. Set (set) - unordered collection of unique elements
# unique_tags = {"savings", "checking", "investment", "savings"}  # duplicate "savings" is discarded
# # 14. FrozenSet (frozenset) - immutable set
# immutable_permissions = frozenset(["READ", "WRITE", "EXECUTE"])
# # 15. Range (range) - sequence of numbers often used in loops
# transaction_indices = range(1, 6)  # produces 1, 2, 3, 4, 5
# # 16. NoneType (None) - singleton object representing null/empty
# pending_transfer = None
# # 17. Bytes (bytes) - immutable raw byte sequences
# byte_payload = b"encrypted_data_string"
# # 18. ByteArray (bytearray) - mutable sequence of bytes
# raw_buffer = bytearray(5)  # bytearray(b'\x00\x00\x00\x00\x00')
# # 19. Type checking with type()
# val = 42.5
# print(type(val))  # <class 'float'>
# # 20. Type checking with isinstance() (best practice)
# is_valid_type = isinstance(user_id, int)  # True

# casting is converting a value from one data type into another.
# 1. **Implicit Casting:** Python automatically converts types without data loss (e.g., adding `int` and `float` produces a `float`).
# 2. **Explicit Casting:** You manually convert data using conversion functions such as `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, `dict()`, `ord()`, and `chr()`.
# # 1. Implicit Conversion: int + float -> float
# num_int = 10
# num_float = 2.5
# result = num_int + num_float  # 12.5 (implicitly converted to float)
# # 2. Float to Integer (int()) - truncates the decimal part (does not round)
# exact_amount = 99.85
# whole_dollars = int(exact_amount)  # 99
# # 3. Numeric String to Integer
# pin_string = "4821"
# pin_number = int(pin_string)  # 4821
# # 4. Binary String to Integer (with base specification)
# binary_str = "1011"
# decimal_val = int(binary_str, 2)  # 11
# # 5. Hexadecimal String to Integer
# hex_str = "1A"
# decimal_from_hex = int(hex_str, 16)  # 26
# # 6. Integer to Float (float())
# count = 5
# ratio = float(count)  # 5.0
# # 7. Decimal String to Float
# rate_str = "3.14159"
# rate_num = float(rate_str)  # 3.14159
# # 8. Integer to String (str())
# account_id = 90812
# id_as_text = str(account_id)  # "90812"
# # 9. Float to String
# balance = 450.50
# balance_text = "$" + str(balance)  # "$450.5"
# # 10. Boolean to String
# is_admin = True
# status_text = "Admin status: " + str(is_admin)  # "Admin status: True"
# # 11. Integer to Boolean (bool()) - 0 is False, any non-zero number is True
# zero_bool = bool(0)    # False
# pos_bool = bool(100)   # True
# neg_bool = bool(-5)    # True
# # 12. String to Boolean - empty string "" is False, any non-empty string is True
# empty_bool = bool("")         # False
# non_empty_bool = bool("yes")  # True
# space_bool = bool(" ")        # True (contains whitespace character)
# # 13. Empty Collections to Boolean - empty collections evaluate to False
# empty_list_bool = bool([])    # False
# filled_list_bool = bool([1])  # True
# # 14. List to Tuple (tuple())
# card_numbers = [1234, 5678, 9012]
# immutable_cards = tuple(card_numbers)  # (1234, 5678, 9012)
# # 15. Tuple to List (list())
# location_tuple = (12.9716, 77.5946)
# location_list = list(location_tuple)  # [12.9716, 77.5946]
# # 16. List to Set (set()) - removes duplicates
# raw_deposits = [50, 100, 50, 200, 100]
# unique_deposits = set(raw_deposits)  # {50, 100, 200}
# # 17. Set to List (list()) - converts back to an indexable list
# unique_list = list(unique_deposits)  # [50, 100, 200]
# # 18. String to List of Characters
# word = "BANK"
# char_list = list(word)  # ['B', 'A', 'N', 'K']
# # 19. List of Key-Value Tuples to Dictionary (dict())
# pairs = [("USD", 1.0), ("EUR", 0.92), ("GBP", 0.79)]
# currency_map = dict(pairs)  # {'USD': 1.0, 'EUR': 0.92, 'GBP': 0.79}
# # 20. Character to ASCII Code (ord()) and ASCII Code back to Character (chr())
# ascii_code = ord('A')      # 65 (char -> int)
# character = chr(65)        # 'A' (int -> char)

