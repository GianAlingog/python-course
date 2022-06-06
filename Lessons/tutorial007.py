# 41 Classes
# class Point:
#     def move(self):
#         print("move")
    
#     def draw(self):
#         print("draw")


# my_point = Point()
# my_point.draw()
# my_point.move()
# my_point.x = 20
# my_point.y = 10
# print(my_point.x)

# Making a new object makes a new "instance" of the class
# and is different from other objects from the same class
# Ex. declaring my_point2 = Point() will not have the x and y attributes

# 42 Constructors
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(f"({point.x}, {point.y})")

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}!")


person = Person("John")
person.talk()
print(person.name)

# 43 Inheritance
# Reuse code. D.R.Y. Don't Repeat Yourself.

class Animal:
    def walk(self):
        print("walk")

class Dog(Animal):
    def bark(self):
        print("Woof!")


class Cat(Animal):
    def meow(self):
        print("Meow!")

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.meow()

# 44 Modules
# Organization, More than one file, Reusable Code
import converters as conv
# Normally, you would put imports on the top of the file
# But for the purpose of organizing the lessons, it is placed here.

# You can also import specifics
# from converters import kgs_to_lbs
print(conv.kgs_to_lbs(40))
print(conv.lbs_to_kgs(90))


from utils import find_max

print(find_max([10, 3, 6, 2]))
