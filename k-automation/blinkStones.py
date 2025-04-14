import time

def transform_numbers(numbers, blinks):
    for _ in range(blinks):
        new_numbers = []
        for num in numbers:
            if num == 0:
                new_numbers.append(1)  # Replace 0 with 1
            elif num == 1:
                new_numbers.append(num * 2024)  # Multiply 1 by 2024
            elif 10 <= num < 100:  # Two-digit numbers
                new_numbers.extend(map(int, str(num)))  # Split into individual digits
            elif len(str(num)) % 2 == 0:  # Even number of digits
                mid = len(str(num)) // 2
                new_numbers.append(int(str(num)[:mid]))  # First half
                new_numbers.append(int(str(num)[mid:]))  # Second half
            elif num == 1000:  # Special case for 1000
                new_numbers.extend([10, 0])  # Split into 10 and 0
            else:
                new_numbers.append(num * 2024)  # Multiply all other numbers by 2024
        numbers = new_numbers
    return numbers

def main():
    # Input numbers and blinks
    try:
        numbers_input = "773 79858 0 71 213357 2937 1 3998391"  # Example input for testing
        print("Numbers: ", numbers_input)
        blinks_input = "25"  # Example input for testing

        numbers = list(map(int, numbers_input.split()))
        blinks = int(blinks_input)

        # Measure time complexity
        start_time = time.time()
        # Transform the numbers
        transformed_numbers = transform_numbers(numbers, blinks)
        end_time = time.time()

        # Output results
        print("Transformed Numbers: ", transformed_numbers)
        print("Number of Stones:", len(transformed_numbers))
        print(f"Time Complexity: {end_time - start_time:.6f} seconds")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
