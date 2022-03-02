#print(3+3*3/3-3)
print(round(8/3, 2))
print(9//4)
result = 4/2
result /=2
print(result)
score = 0
score += 1
#print(score)
#print("Your score is " + str(score))
#print(f"Your score is {score}") #using f character to avoid writing out str



#Day 2 challenge:

print("Welcome to the tip calculator!\n")
total_bill = int(input("What was the total bill?\n"))
tip = input("How much tip percentage would you like to give? 10, 12, or 15? \n")
people = input("How many people to split the bill? \n")

indiv_tip_perc = int(tip)/(100* int(people))
indiv_tip_perc = int(indiv_tip_perc)
tip_percentage = print((indiv_tip_perc) * (total_bill))
print(f"Each person should pay {tip_percentage}")
    