# ANSI color codes
GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
END = '\033[0m'

# Get user's name
name = input(f"{GREEN}What's your name? {END}")

# Greet the user
print(f"{BLUE}Hello, {name}! Welcome to Python programming!{END}")

# Ask for two numbers
print(f"\n{GREEN}Let's do some math!{END}")
num1 = float(input(f"{GREEN}Enter first number: {END}"))
num2 = float(input(f"{GREEN}Enter second number: {END}"))

# Calculate and show results    
sum_result = num1 + num2
product_result = num1 * num2

print(f"\n{BLUE}Results:{END}")
print(f"{GREEN}Sum: {num1} + {num2} = {sum_result}{END}")
print(f"{GREEN}Product: {num1} * {num2} = {product_result}{END}")

# Add division with error handling
try:
    division_result = num1 / num2
    print(f"{GREEN}Division: {num1} / {num2} = {division_result}{END}")
except ZeroDivisionError:
    print(f"{RED}Error: Cannot divide by zero!{END}")   