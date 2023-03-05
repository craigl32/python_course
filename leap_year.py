year = int(input("Enter year: "))
if year % 4 == 0:
    print("Leap year")
elif year != 100:
    print("Not a leap year")
elif  year % 400  == 0:
    print("Leap year")