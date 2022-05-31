# 24 Car Game
# game = True
# started = False
# print("""Welcome to the FEL car game!
# ========================================
# If you're new to the game, run the help command to get a list of instructions.
# Otherwise, have fun!
# ========================================""")
# while game:
#     user_input = input("FEL > ")
#     if user_input == "help":
#         print("""help - lists all commands
# start - starts the car
# stop - stops the car
# quit - quits the game""")
#     elif user_input == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started... Ready to go!")
#     elif user_input == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped.")
#     elif user_input == "quit":
#         print("Quitting the game... Thanks for playing!")
#         game = False
#     else:
#         print("I don't understand that...")

# 25 For Loops
# for item in range(5, 105, 5):
#     print(item)

from xml.etree.ElementPath import xpath_tokenizer


prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(total)

# 26 Nested Loops
for x in range(4):
    for y in range(4):
        print(f"({x}, {y})")

list_of_numbers = [5, 1, 5, 1, 1], [5, 1, 5, 1, 5], [1, 1, 1, 1, 5]
for w in list_of_numbers:
    for x in w:
        for y in range(x):
            print("x", end="")
        print("")
    print("")

# 27 Lists
names = ["J", "G", "T", "F", "B"]
print(names) # prints all
print(names[2])  # prints on index 2
print(names[2:])  # prints on index 2 onwards
print(names[:4])  # prints start until index 4 (not including)
print(names[2:4])

nums = [3, 4, 9, 6, 7]
max = nums[0]
for number in nums:
    if number > max:
        max = number
print(max)
