"""
Write a Python program that creates a list randList with 50 random integers from 1 to 100 (inclusive)

Use a for loop to assign the odd and even numbers in randList to oddList and evenList, respectively

Output the three lists as shown:

Random list:  [92, 31, 85, 46, 82, 81, 38, 22, 68, 8, 97, 56, 6, 60, 37, 24, 73, 85, 29, 67, 10, 51, 28, 28, 87, 83, 89, 90, 52, 81, 94, 25, 86, 32, 78, 59, 13, 35, 45, 86, 52, 23, 66, 23, 66, 55, 78, 87, 86, 44]
Odd list:  [31, 85, 81, 97, 37, 73, 85, 29, 67, 51, 87, 83, 89, 81, 25, 59, 13, 35, 45, 23, 23, 55, 87]
Even list:  [92, 46, 82, 38, 22, 68, 8, 56, 6, 60, 24, 10, 28, 28, 90, 52, 94, 86, 32, 78, 86, 52, 66, 66, 78, 86, 44]
"""
import math

randList = []

for i in range(51):
  randList[i] = math.random(1, 100)

oddList = []

for i in randList:
  if i % 2 == 0:
    evenList.append(i)
  else:
    oddList.append(i)

print("Random list: ", randList)
print("Odd list: ", oddList)
print("Even list: ", evenList)
