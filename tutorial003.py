# 19 Logical Operators
high_income = True
bad_credit = True

if high_income and not bad_credit:
    print("T")
else:
    print("F")

# and, or, not logical operator

# 20 Comparison Operators
temp = 30

if temp > 30: # >, <, ==, !=
    print("It's a hot day.")
else:
    print("It's not a hot day.")

username = "FeltyX"

if len(username) < 3:
    print("Must be at least 3 characters")
elif len(username) > 50:
    print("Must be less than 50 characters")
else:
    print(f"Username set to {username}")

# 21 Weight Conversion
# weight = int(input("What is your weight? "))
# unit = input("(L)bs or (K)gs ")
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"Your weight is {converted}kgs")
# elif unit.upper() == "K":
#     converted = weight / 0.45
#     print(f"Your weight is {converted}lbs")

# 22 While Loops
i = 0
while i < 5:
    print("*" * i)
    i += 1
print("Done")

# 23 Guessing Game
# secret_number = 3
# max_guesses = 3
# current_guess = 1
# while current_guess <= max_guesses:
#     guess = int(input("Guess: "))
#     current_guess += 1
#     if guess == secret_number:
#         print("You won :)")
#         break
# else:
#     print("You lost :(")
