print("Welcome to the bill calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12 or more? "))
people = int(input("How many people would you like to split the bill ? "))
bill_with_tip = bill * (tip / 100) + bill
print(bill_with_tip)
bill_per_person = round(bill_with_tip / people, 2)
print(f"Each person should pay {bill_per_person}")