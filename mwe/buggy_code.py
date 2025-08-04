"""
Buggy Code Example
This file contains intentional bugs for demonstrating Claude Code's debugging capabilities
"""

def divide_numbers(a, b):
    # Bug: No zero division check
    result = a / b
    return result

def find_max(numbers):
    # Bug: Doesn't handle empty list
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num == num  # Bug: Using == instead of =
    return max_num

def count_vowels(text):
    # Bug: Missing some vowels
    vowels = ['a', 'e', 'i']  # Missing 'o' and 'u'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def main():
    print("Testing buggy functions...")
    
    # This will cause ZeroDivisionError
    print(f"10 / 0 = {divide_numbers(10, 0)}")
    
    # This will cause IndexError with empty list
    print(f"Max of [] = {find_max([])}")
    
    # This will give incorrect count
    print(f"Vowels in 'hello world' = {count_vowels('hello world')}")

if __name__ == "__main__":
    main()