# 34 Functions
# Define a set of code as a "function"
# If you want to use that code, call the function

# You cannot call the function before it's declared
def greet():
    print("Hi there!")
    print("Welcome aboard!")


print("Start")
greet()
# greet()
# greet()
print("Finish")

# 35 Parameters
# Make your functions more dynamic
def hello(name, age = 0):
    print(f"Hello there, {name}! I'm also {age} years old.")


# your_name = input("Your name: ")
# hello(your_name, 12)

# hello("J", 15)
# hello("K", 32)
# hello("F", 24)
# hello("Z") # will not give error if you set a default value
             # for the missing arguments

# 36 Keyword Arguments
# By default, we use positional arguments,
# wherein the order of the arguments that
# are passed in, matter. As that will be
# the order in which they are stored into the variables

# We use keyword arguments to "bypass" or
# ignore the order of which the arguments
# are passed in. See the example below.

hello(age=4, name="A")

# The function runs as intended even if the
# args are passed in a different order than
# the usual. This is because the keyword
# arguments pass them into the desired parameter

# You might use keyword arguments to use more readable code

# 37 Return Statement
def add(num_1=0, num_2=0):
    return num_1+num_2


# Return will return a value which you can store into a variable or print
def square(num):
    return num*num


result = add(5, 10)
print(result)
print(square(4))

# 38 Creating a Reusable Function
def emoji_converter(message):
    emojis = {
        ":)": "🙂",
        ":(": "🙁"
    }
    words = message.split(" ")
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


# message = input("> ")
# print(emoji_converter(message))

# 39 Exceptions
try:
    age = int(input("Age: "))
    income = 200000.00
    risk = income / age
    print(f"{age} & {risk}")
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid value")

# 40 Comments
# <- this is how you declare a comment
# use comments to explain what a block of code does
