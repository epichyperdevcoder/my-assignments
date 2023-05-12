"""
Write a Python program to calculate the sum of the digits in an integer

Your program should take an integer as input and output the sum of all the digits in the integer.
You do not need to validate the input.

Sample input:
19234581

Sample output:
33
"""

n = input("Enter a number: ")

total = 0

for i in n:
  total += int(i)

print(total)
