"""
Simple Calculator Module
A basic calculator implementation for demonstrating Claude Code capabilities
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def calculate(operation, a, b):
    """
    Perform calculation based on operation
    
    Args:
        operation (str): Operation to perform ('add' or 'subtract')
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Result of the calculation
    """
    if operation == 'add':
        return add(a, b)
    elif operation == 'subtract':
        return subtract(a, b)
    else:
        raise ValueError(f"Unknown operation: {operation}")

if __name__ == "__main__":
    print("Simple Calculator")
    print("="*20)
    print(f"5 + 3 = {calculate('add', 5, 3)}")
    print(f"10 - 4 = {calculate('subtract', 10, 4)}")