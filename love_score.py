print("Welcome to the Love calculator")
name1 = input("What is your first name? ")
name2 = input("What is the second name? ")

combined_name = name1 + " " + name2
print(combined_name)
lower_case_name = combined_name.lower()
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

print(love_score)

