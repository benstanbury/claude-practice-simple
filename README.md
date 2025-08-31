# Claude Practice Simple

A Python project with intentionally inefficient code designed for optimization practice and performance improvement exercises.

## Purpose

This repository contains deliberately poorly written Python code that demonstrates common performance anti-patterns and inefficiencies. It's designed to be used as a practice ground for:

- Code optimization techniques
- Performance profiling
- Algorithm improvement
- Best practices implementation

## What's Inefficient?

The `main.py` file contains numerous performance issues including:

### Algorithm Inefficiencies
- **Nested loops where single loops would suffice** - Using O(n²) complexity where O(n) is possible
- **Bubble sort implementation** - Using O(n²) sorting instead of built-in O(n log n) methods
- **Manual duplicate removal** - O(n²) approach instead of using sets
- **Inefficient prime checking** - Checking all numbers up to n instead of √n

### Data Structure Problems
- **String concatenation in loops** - Creating new string objects repeatedly
- **Redundant list operations** - Multiple unnecessary copies and iterations
- **Poor memory usage** - Storing unnecessary intermediate results

### Redundant Calculations
- **Recalculating random seeds** - Unnecessary function calls in loops
- **Recomputing sums** - Calculating the same values multiple times
- **Redundant sorting** - Sorting already sorted data
- **Inefficient modulo operations** - Using subtraction loops instead of modulo operator

### Poor Programming Practices
- **Unnecessary variable resets** - Resetting counters inside loops
- **Inefficient condition checking** - Complex nested conditions for simple operations
- **Missing built-in optimizations** - Reimplementing functionality that Python provides efficiently

## Running the Code

```bash
python main.py
```

The program will process a list of 1000 random numbers and perform various operations, displaying timing information to help measure performance improvements.

## Optimization Opportunities

This code provides excellent opportunities to practice:

1. **Algorithmic optimization** - Replace O(n²) algorithms with O(n) or O(n log n) alternatives
2. **Built-in usage** - Utilize Python's optimized built-in functions and data structures
3. **Memory optimization** - Reduce unnecessary object creation and copying
4. **Code simplification** - Remove redundant calculations and operations

## Expected Improvements

With proper optimization, you should be able to achieve:
- **10-100x performance improvements** in most operations
- **Significant memory usage reduction**
- **Cleaner, more readable code**
- **Better algorithmic complexity**

## Challenge

Try to optimize this code while maintaining the same functionality. See how much you can improve the execution time and memory usage!

## License

This project is for educational purposes. Feel free to use it for learning and practice.