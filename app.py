# Importing
from math import *

# ------------------------
# Hello World
# ------------------------
print("Hello World")
print("\n")

# ------------------------
# Drawing Shape
# ------------------------
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
print("\n")

# ------------------------
# Variables and Data Types
# ------------------------
character_name = "John"
character_age = "35"
print("There once was a man named "+ character_name +", ")
print("he was "+character_age+" years old. ")

character_name = "Mike"
character_age = "35"
print("He really liked the name "+character_name+", ")
print("but didn't like being "+character_age+".")
print("\n")

# ------------------------
# Working with Strings
# ------------------------
phrase = "Giraffe Academy"
print(phrase + " is cool")
print(phrase.lower() + " " +phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Elephant"))
print("\n")

# ------------------------
# Working with Number
# ------------------------
print(-2.0987)
print(3 * (4+5))
my_num = 5
print(my_num)
print(str(my_num))
my_num = -5
print(abs(my_num))
print(pow(3,2)) #3 pangkat 2
print(max(4,6))
print(min(4,6))
print(round(3.28))
print(floor(3.28))
print(ceil(3.28))
print(sqrt(36))
print("\n")

# ------------------------
# Getting Input From User
# ------------------------
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are" + age)
print("\n")

# ------------------------
# List in Python
# ------------------------
friends = ["Kevin", "Karen", "Jim", "Oscar","Toby"]
print(friends)
print(friends[0])
print(friends[1:])
print(friends[1:3]) # startdi:berhentisebelum
friends[1] = "Mike"
print(friends[1])
print("\n")

# ------------------------
# List Function
# ------------------------
lucky_numbers=[4,8,15,16,23,42]
friends = ["Kevin","Karen", "Karen", "Jim", "Oscar","Toby"]

friends.append("Creed")
print(friends)
friends.insert(1, "Kelly") # Insert di index 1, yang sebelumnya index 1 dan seterusnya kepinggir
print(friends)
friends.extend(lucky_numbers)
print(friends)
friends.remove("Jim")
print(friends)
friends.pop() # Pop an item of off the list (Remove last element)
print(friends)
# friends.clear() remove all element in list
print(friends.index("Kevin"))
# print(friends.index("Mike")) not found
print(friends.count("Karen"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)
print("\n")

# ------------------------
# Tuple in Python : Tuple is like list, but immutable aka gabisa dirubah.
# ------------------------
coordinates = (4,5)
print(coordinates[1])
print("\n")

# ------------------------
# If Statement
# ------------------------

is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not male but are tall")
else:
    print("You are neither male nor tall")

print("\n")

# ------------------------
# Comparison
# ------------------------
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))
print("\n")

# ------------------------
# Dictionary
# ------------------------
#Key in Dictionary can be Number
monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}
print(monthConversions["Dec"])
print(monthConversions.get("Jan"))
print(monthConversions.get("jul","Not A Valid key"))
print("\n")

# ------------------------
# Loop While
# ------------------------
i = 1
while i<= 10:
    print(i)
    i += 1

print("Done with Loop")
print("\n")

# ------------------------
# Loop For
# ------------------------

for letter in "Girrafe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

for index in range(10): #range itu dari 0-9
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0 :
        print("First Iteration")
    else:
        print("Not First Iteration")

# ------------------------
# 2D List and Nested Loop
# ------------------------

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for column in row:
        print(column)
