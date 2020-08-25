"""
CP1404/CP5632 - Practical
Files
"""

# 1.
out_file = open('name.txt', 'w')
name.txt = input("Enter your name.txt: ")
print(name.txt, file=out_file)
out_file.close()

# 2.
in_file = open('name.txt', 'r')
first_line_str = in_file.readline()
print("Your name.txt is ", first_line_str)
in_file.close()

# 3.
in_file = open('numbers.txt', 'r')
first_line = int(in_file.readline())
second_line = int(in_file.readline())
result = first_line + second_line
print(result)
in_file.close()

# 4.
in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)