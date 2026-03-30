# Task 01a - Calculate Total
# Write a function called calculate_total(price, quantity)
# that returns the total cost.
#
# Example:
# calculate_total(4.5, 3) -> 13.5

def calculate_total(price, quantity):
    total = price * quantity
    return total


def main():
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    total = calculate_total(price, quantity)
    print(total)


if __name__ == "__main__":
    main()
