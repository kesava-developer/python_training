# functions_example.py

def say_hello():
    """Print a simple greeting."""
    print("Hello from a function!")

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def repeat_text(text, times=2):
    """Return text repeated a given number of times."""
    return text * times

def describe_person(name, age, city="Unknown"):
    """Return a formatted description using keyword args."""
    return f"{name} is {age} years old and lives in {city}."

def main():
    say_hello()

    total = add_numbers(5, 7)
    print("Sum:", total)

    repeated = repeat_text("Hi! ", 3)
    print("Repeated:", repeated)

    info = describe_person(name="Raghu", age=25, city="Bangalore")
    print(info)

if __name__ == "__main__":
    main()