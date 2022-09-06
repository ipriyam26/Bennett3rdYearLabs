# You have been appointed as a coach of Bennett Basketball team. Your task is to select players in your team. You believe that short-height student plays better than the tall student.

# All the students are standing in a line, you think a student is short if he/she is shorter than both of his/her neighbors. First and last student is not short at all. You will select all short students for your team.

# Find the maximum number of students that you can select in your team. You can reorder the students in a line as you wish.  

n = int(input())
heights = [int(element) for element in input().split()]

