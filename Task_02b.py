# Task 02b - Extract Even Numbers
# Write a function called extract_even_numbers(numbers)
# that takes a list of integers and returns a new list
# containing only the even numbers.
#
# Example:
# extract_even_numbers([1, 2, 3, 4, 5, 6]) -> [2, 4, 6]

def extract_even_numbers(numbers):
    extract_even_numbers = [num for num in numbers if num % 2 == 0]
    return extract_even_numbers 
    pass


def main():
    user_input = input("Enter numbers separated by commas: ")
    numbers = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]
    print(extract_even_numbers(numbers))


if __name__ == "__main__":
    main()
