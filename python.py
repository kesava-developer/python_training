# Python variable examples

# Variables can store different data types
integer_value = 42
float_value = 3.14
string_value = "Hello, Python!"
boolean_value = True

# Multiple assignment
x, y, z = 1, 2.5, "three"

# Variables can be reused and updated
counter = 0
counter += 1

# Use formatted strings to print variable values
print("integer_value:", integer_value)
print(f"float_value: {float_value}")
print("string_value:", string_value)
print("boolean_value:", boolean_value)
print("x, y, z:", x, y, z)
print("counter:", counter)

# Example of a variable holding the result of an expression
total = integer_value + x
print(f"total = integer_value + x = {total}")

# Constants are usually named in ALL_CAPS by convention
PI = 3.14159
print(f"PI constant: {PI}")

# Variables can change type during runtime
data = "now a string"
print("data before:", data)
data = 100
print("data after:", data)
