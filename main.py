#!/usr/bin/env python3

import time
import random

def slow_number_processor():
    """
    An intentionally inefficient number processing function with multiple performance issues:
    - Nested loops where they're not needed
    - Redundant calculations
    - Poor data structure choices
    - Unnecessary function calls
    - Memory inefficient operations
    """
    
    # Generate a list of numbers (inefficiently)
    numbers = []
    for i in range(1000):
        # Inefficient: recalculating random seed every iteration
        random.seed(time.time())
        numbers.append(random.randint(1, 100))
    
    print(f"Generated {len(numbers)} numbers")
    
    # Inefficient sum calculation with nested loops
    total_sum = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:  # Only add when indices match (completely unnecessary loop)
                total_sum += numbers[i]
    
    print(f"Sum of all numbers: {total_sum}")
    
    # Inefficient duplicate removal
    unique_numbers = []
    for num in numbers:
        is_duplicate = False
        for existing in unique_numbers:
            if num == existing:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_numbers.append(num)
    
    print(f"Found {len(unique_numbers)} unique numbers")
    
    # Inefficient sorting using bubble sort
    sorted_numbers = unique_numbers.copy()
    n = len(sorted_numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                # Inefficient swap
                temp = sorted_numbers[j]
                sorted_numbers[j] = sorted_numbers[j + 1]
                sorted_numbers[j + 1] = temp
    
    print(f"Sorted unique numbers: {sorted_numbers[:10]}...")  # Show first 10
    
    # Inefficient statistical calculations
    mean = calculate_mean_slowly(sorted_numbers)
    median = calculate_median_slowly(sorted_numbers)
    
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median}")
    
    # Inefficient prime number detection
    prime_count = 0
    for num in sorted_numbers:
        if is_prime_slowly(num):
            prime_count += 1
    
    print(f"Prime numbers found: {prime_count}")
    
    return sorted_numbers

def calculate_mean_slowly(numbers):
    """Calculate mean with unnecessary complexity"""
    total = 0
    # Inefficient: recalculating sum instead of using previous result
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                total += numbers[i]
    
    # Inefficient division
    count = 0
    for _ in numbers:
        count += 1
    
    return total / count if count > 0 else 0

def calculate_median_slowly(numbers):
    """Calculate median inefficiently"""
    # Inefficient: sorting again even though numbers are already sorted
    temp_list = []
    for num in numbers:
        temp_list.append(num)
    
    # Bubble sort again (unnecessary)
    n = len(temp_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if temp_list[j] > temp_list[j + 1]:
                temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]
    
    # Inefficient median calculation
    length = len(temp_list)
    if length % 2 == 0:
        return (temp_list[length // 2 - 1] + temp_list[length // 2]) / 2
    else:
        return temp_list[length // 2]

def is_prime_slowly(n):
    """Extremely inefficient prime checking"""
    if n < 2:
        return False
    
    # Inefficient: checking all numbers up to n instead of sqrt(n)
    for i in range(2, n):
        # Inefficient modulo calculation
        remainder = n
        while remainder >= i:
            remainder -= i
        if remainder == 0:
            return False
    
    return True

def string_operations_slowly():
    """Inefficient string operations for demonstration"""
    print("\nPerforming inefficient string operations...")
    
    # Inefficient string concatenation
    result = ""
    words = ["python", "is", "great", "for", "optimization", "practice"]
    
    for word in words:
        # Inefficient: creating new string objects repeatedly
        for char in word:
            result = result + char
        result = result + " "
    
    print(f"Concatenated string: {result.strip()}")
    
    # Inefficient character counting
    char_counts = {}
    for char in result:
        char_counts[char] = 0  # Reset count each time (wrong!)
        for c in result:  # Count entire string for each character
            if c == char:
                char_counts[char] += 1
    
    print(f"Character counts: {dict(list(char_counts.items())[:5])}")  # Show first 5

if __name__ == "__main__":
    print("Starting inefficient number processing...")
    start_time = time.time()
    
    processed_numbers = slow_number_processor()
    string_operations_slowly()
    
    end_time = time.time()
    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")
    print("This code has many optimization opportunities!")