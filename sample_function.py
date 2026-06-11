def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}! Welcome to Python."


if __name__ == "__main__":
    example_name = "World"
    print(greet(example_name))
    print(greet("Alice"))
    print(greet("venkatesh"))
