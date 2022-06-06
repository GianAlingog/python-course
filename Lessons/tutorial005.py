# 28 2D Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(matrix[2][2])
for row in matrix:
    for item in row:
        print(item)

# 29 List Methods
matrix.append([10, 11, 12])
# matrix.insert(index, value)
# matrix.remove(index)
# matrix.clear()
# matrix.pop()
# matrix.index(index)
# [13, 14, 15] in matrix # False
# matrix.count(value)
# matrix.sort()
# matrix.reverse()
# matrix.copy()

# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# remove duplicates by converting to set

# 30 Tuples
my_tuple = (1, 2, 3)
# my_tuple.count()
# my_tuple.index()
# immutable

# 31 Unpacking
coordinates = (1, 2, 3)
# coordinates[0] * coordinates[1] * coordinates[2] # normal

# x = coordinates[0] # variable assignment
# y = coordinates[1]
# z = coordinates[2]

x, y, z = coordinates # unpacking

# 32 Dictionaries
# Used for storing key-value pairs
my_dict = {
    "name": "F",
    "age": 15,
    "loml": True
}
print(my_dict["loml"]) # bad way
print(my_dict.get("loml")) # good way (can set default value as another param)

# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "<!>") + " "
# print(output)

# 33 Emoji Converter
# message = input("> ")
# words = message.split(" ")
# emojis = {
#     ":)": "🙂",
#     ":(": "🙁"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)
