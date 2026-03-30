# Task 04 - Expand Subject Codes
# Write a function called expand_subject_codes(codes)
# that takes a list of short subject codes and returns a new list
# with the full subject names.
#
# Use the following code table:
# ENG -> English
# MAT -> Mathematics
# SCI -> Science
# HIS -> History
# ART -> Art
#
# If a code is not recognised, ignore it.
#
# Example:
# expand_subject_codes(["MAT", "SCI", "XYZ", "ENG"])
# returns ["Mathematics", "Science", "English"]

def expand_subject_codes(codes):
    code_mapping = {
        "ENG": "English",
        "MAT": "Mathematics",
        "SCI": "Science",
        "HIS": "History",
        "ART": "Art"
    }
    return [code_mapping.get(code) for code in codes]
    pass


def main():
    user_input = input("Enter subject codes separated by commas: ")
    codes = [code.strip().upper() for code in user_input.split(",") if code.strip() != ""]
    print(expand_subject_codes(codes))


if __name__ == "__main__":
    main()
