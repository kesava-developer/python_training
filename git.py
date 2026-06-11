# Define a function
def greet(name):
    return f"Hello, {name}!"

# Call the function
message = greet("Alice")
print(message)  # Output: Hello, Alice!

# Function with multiple parameters
def add_numbers(a, b):
    total = a + b
    return total

result = add_numbers(10, 20)
print(result)   