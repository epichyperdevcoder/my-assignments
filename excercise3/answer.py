"""
Write a Python program to find the largest number in each list in a list

Your code will be given a list of positive numbers seperated by commas.
Your code should keep accepting numbers until the user enters 'done'.

Sample input:
1,2,3,4,5
6,7,8,9,10
done

Sample output:
5,10
"""

accepting_answers = True

lists = []

while accepting_answers:
  answer = input()
  if answer == "done":
    accepting_answers = False
  else:
    new_list = []
    for number in answer.split(","):
      new_list.append(int(number))
    lists.append(new_list)

largest_list = []

for list in lists:
  largest = 0
  for number in list:
    if number > largest:
      largest = number
  largest_list.append(str(largest))

print(",".join(largest_list))

# Flag was here!
