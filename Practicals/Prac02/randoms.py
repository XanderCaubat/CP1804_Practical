import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# line 1 answer:    numbers.txt in between 5 and 20
#                   smallest number is 6, largest number is 20

# line 2 answer:    numbers.txt in between 3 and 10
#                   smallest number is 3, largest number is 9
#                   no, the increment is in + 2. only 4 possible outcomes (3, 5, 7 and 9)

# line 3 answer:    float numbers.txt in between 2.5 and 5.5
#                   smallest number is 2.9596245192822135, largest number is 5.282878794323553

print(random.randint(1, 100))

