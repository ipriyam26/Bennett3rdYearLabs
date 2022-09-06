M,R = [int(element) for element in input().split()]
wages = [int(element) for element in input().split()]
wages.sort(reverse=True)
working_days = 0
current_wage = 0
for wage in wages:
   current_wage += wage
   working_days += 1
   if current_wage >= R:
       break
print(M-working_days)
    

