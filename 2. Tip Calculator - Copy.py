print("Welcome to Tip Calculator")

total_bill = input("What was the total bill? \n $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15?\n")
people = input("How many people to split the bill?\n")

payable = (float(total_bill) + (float(total_bill)*float(tip_percentage)/100))/int(people)
final_amount = round(payable, 2)

print(f"Each persom should pay: ${final_amount}")
