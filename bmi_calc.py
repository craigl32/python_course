#BMI calculator

height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))

bmi = weight / (height * height)
clean_number = round(bmi, 2)

print("Your BMI is :", clean_number)
if bmi < 18.5:
    print("You are underweight")

else: print("you are overweight")

