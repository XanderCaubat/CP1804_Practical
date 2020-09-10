"""
CP1404/CP5632 Practical 05
Suggested Solution
Count word occurrences in a string
This example is in the lecture notes 3 different ways
"""

word_count = {}
string = input("String: ")
words = string.split()
for word in words:
    count = word_count.get(word, 0)
    word_count[word] = count + 1
words = list(word_count.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_count[word]))