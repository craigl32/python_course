age = int(input("Enter your current age: "))

years_reaming = 90 - age
days_reaming = 365 * years_reaming
weeks_reaming = years_reaming * 52
months_reaming = years_reaming * 12

print(f"You have {days_reaming} days, {weeks_reaming} weeks, {months_reaming} months and {years_reaming} years , you are {age} years old.")
