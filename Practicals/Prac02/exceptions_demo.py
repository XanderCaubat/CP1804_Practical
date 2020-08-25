"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Undefined.")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers.txt!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. answer: It occurs if the input are non-numeric (ex. a, #, ? etc.).
# 2. answer: It occurs if denominator is 0.
# 3. answer: Yes.
