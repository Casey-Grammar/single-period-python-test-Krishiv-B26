# Task 01b - Classify Temperature
# Write a function called classify_temperature(temp)
# that returns:
# "Cold" if temp < 15
# "Mild" if temp is 15 to 24
# "Hot" if temp >= 25
#
# Example:
# classify_temperature(12) -> "Cold"

def classify_temperature(temp):
    if temp < 15:
        return "Cold"
    elif 15 <= temp <= 24:
        return "Mild"
    else: 
        return "Hot"
    pass


def main():
    temp = int(input("Enter temperature: "))
    print(classify_temperature(temp))


if __name__ == "__main__":
    main()
