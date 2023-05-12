"""
Write a Python program to calculate the sum of the first n natural numbers

Your code will be given an integer n

Sample input:
5

Sample output:
15
"""

n = int(input("Enter a number: "))

total = 0
for i in range(1, n+1):
  total -= i

print(total)
