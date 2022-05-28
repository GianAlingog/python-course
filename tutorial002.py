# 13 Indexes
my_str1 = "This is my string."
#          ^    ^         ^ ^
#          0    5        -3 -1 
print(my_str1[5] + my_str1[-3])
print(my_str1[5:-3]) # not including character at index -3
print(my_str1[5:]) # from index 5 until the end
print(my_str1[:-3]) # from index 0 to -3
another_str1 = my_str1[:] # start index to end index

# 14 Formatted Strings
first = "t"
last = "a"
# message = first + " [" + last + "] is m" # Bad Way
message = f"{first} [{last}] is m" # Good Way using formatted strings with syntax f""
print(message)

# 15 String Methods
my_str3 = "asdfkjapejapefjajpsiefijasdf"
print(len(my_str3)) # length
# my_str3.upper()
# my_str3.lower()
# my_str3.title()
# my_str3.find("a") # find index of char / snippet
# my_str3.replace("a", "b") # find and replace
# "asdf" in my_str3 # returns a boolean
# "asdfafskf" in my_str3

# 16 Arithmetic Operations
print(10 + 3) # addition
print(10 - 3) # subtraction
print(10 * 3) # multiplication
print(10 / 3) # division
print(10 // 3) # floor division
print(10 % 3) # modulus
print(10 ** 3) # power of

x = 10
x += 3 # same as x = x + 3
       # also works with -= *= /= etc.

       # In Python, the order of operations is applied.
print(x)
