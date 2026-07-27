# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def get_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def get_average(numbers):
    return get_sum(numbers) / len(numbers)

def get_maximum(numbers):
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum

def get_minimum(numbers):
    minimum = numbers[0]
    for n in numbers:
        if n < minimum:
            minimum = n
    return minimum

if __name__ == "__main__":
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Error: N must be a positive integer.")
    else:
        numbers = []
        for i in range(1, count + 1):
            num = int(input(f"Enter number {i}: "))
            numbers.append(num)

        print("\nResults:")
        print(f"Sum:     {get_sum(numbers)}")
        print(f"Average: {get_average(numbers)}")
        print(f"Maximum: {get_maximum(numbers)}")
        print(f"Minimum: {get_minimum(numbers)}")
