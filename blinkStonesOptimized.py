'''
============================================================================================================
============================================================================================================

Advanced Approach: Recursive Pre-Computation
Instead of processing all transformations on-the-fly for each blink, we can:

Pre-compute the transformations for each unique number encountered.
Store these transformations in a dictionary for reuse.
Recursive Computation: Each blink builds on the results of the previous one using only pre-computed values.
This approach avoids redundant recalculations, especially for large numbers of blinks.

How It Works
Memoization for Transformations:

Store transformations for numbers in a dictionary so they’re computed only once per unique input.
Recursive Transformation:

For each blink, compute the transformation recursively using memoized results, drastically reducing redundant operations.
Memory-Efficient Tracking:

The dictionary stores only necessary intermediate results and avoids materializing massive lists.

============================================================================================================
============================================================================================================

What’s Improved?

Memoization:
The compute_transformations function stores results of transformations for reuse.
Each unique number is transformed only once, no matter how many times it appears.

Reduced Redundancy:
Eliminates repetitive string operations and unnecessary intermediate list creation.

Scalable for High Blink Counts:
Handles large numbers of blinks by focusing only on unique transformations.

Advantages:
Time Efficiency: By memoizing transformations, we save time on repetitive calculations.
Memory Efficiency: The frequency dictionary avoids creating massive intermediate lists.
Scalability: Works well even for very high blink counts.

============================================================================================================
============================================================================================================
'''

import time
from collections import defaultdict

# Memoization dictionary for precomputed transformations
transformation_cache = {}

def compute_transformations(num):
    """Compute the transformation for a single number."""
    if num in transformation_cache:
        return transformation_cache[num]

    if num == 0:
        result = [1]  # Replace 0 with 1
    elif num == 1:
        result = [num * 2024]  # Multiply 1 by 2024
    elif 10 <= num < 100:  # Two-digit numbers
        tens, ones = divmod(num, 10)
        result = [tens, ones]
    elif len(str(num)) % 2 == 0:  # Even number of digits
        num_str = str(num)
        mid = len(num_str) // 2
        first_half = int(num_str[:mid])
        second_half = int(num_str[mid:])
        result = [first_half, second_half]
    elif num == 1000:  # Special case for 1000
        result = [10, 0]
    else:
        result = [num * 2024]  # Multiply all other numbers by 2024

    transformation_cache[num] = result
    return result

def transform_numbers(numbers, blinks):
    # Initialize frequency dictionary
    freq = defaultdict(int)
    for num in numbers:
        freq[num] += 1

    # Process blinks
    for _ in range(blinks):
        print("Blinks: ", _ + 1)
        new_freq = defaultdict(int)
        for num, count in freq.items():
            transformations = compute_transformations(num)
            for transformed_num in transformations:
                new_freq[transformed_num] += count
        freq = new_freq

    return freq

def main():
    # Input numbers and blinks
    try:
        numbers_input = "773 79858 0 71 213357 2937 1 3998391"  # Example input for testing
        print("Numbers: ", numbers_input)
        blinks_input = "75"  # Example input for testing

        numbers = list(map(int, numbers_input.split()))
        blinks = int(blinks_input)

        # Measure time complexity
        start_time = time.time()
        # Transform the numbers
        transformed_freq = transform_numbers(numbers, blinks)
        end_time = time.time()

        # Calculate total stones
        total_stones = sum(transformed_freq.values())

        # Output results
        print("Number of Stones:", total_stones)
        print(f"Time Complexity: {end_time - start_time:.6f} seconds")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
