"""
Write a Python program to count the number of vowels in a given text.

Your program should ask the user to enter a text and then print the number of vowels in the text.

Sample input:
The quick brown fox jumps over the lazy dog.

Sample output:
11
"""

text = input("Enter a text: ")

vowels = ["a", "e", "i", "o", "u"]

count = 0

for i in text:
  if i == vowels[0] or vowels[1] or vowels[2] or vowels[3] or vowels[4]:
    count += 1

print(count)
