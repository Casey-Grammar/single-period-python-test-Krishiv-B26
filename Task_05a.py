# Task 05a - Find the Largest Number
# Write a function called find_largest(numbers)
# that takes a list of integers and returns the largest value.
#
# Example:
# find_largest([4, 9, 2, 7]) -> 9
#
# You may assume the list will contain at least one number.

def find_largest(numbers):
    find_largest = max(numbers)
    return find_largest
    pass

def main():
    user_input = input("Enter numbers separated by commas: ")
    numbers = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]
    print(find_largest(numbers))


if __name__ == "__main__":
    main()
