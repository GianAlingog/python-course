# 13
my_str1 = "This is my string."
#          ^    ^         ^ ^
#          0    5        -3 -1 
print(my_str1[5] + my_str1[-3])
print(my_str1[5:-3]) # not including character at index -3
print(my_str1[5:]) # from index 5 until the end
print(my_str1[:-3]) # from index 0 to -3
another_str1 = my_str1[:] # start index to end index

# 14
