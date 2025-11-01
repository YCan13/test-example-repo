def hello_world():
    """A simple function that returns 'Hello, World!'"""
    return "Hello, World!"

def add_numbers(a, b):
    """Add two numbers together"""
    return a + b

if __name__ == "__main__":
    print(hello_world())
    print(f"5 + 3 = {add_numbers(5, 3)}")