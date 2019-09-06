# 1. Ask a user for their first name and age. Print "[NAME] is [AGE] years old"
# userInput = input("Enter your name ")
# userAge = int(input("Enter your age "))
# print(f"{userInput} is {userAge}")


# 2. Ask the user to enter their age. Check if they entered a value between 0 and 125.
# If valid, print "REAL AGE". If invalid print “NOT A REAL AGE!!!”
# userInput = int(input("Enter your age "))
# if userInput >= 0 and userInput <= 125:
#     print("REAL AGE")
# else:
#     print("NOT A REAL AGE!!!")


# 3. Use a for loop to print every 4 numbers from -50 to 50.
# for index in range(-50, 50, 4):
#     print(index)


# todo go back over this until i get it right <------------------------
# 4. Ask the user to enter a number to add to a total.
# Keep asking the user to enter a number until they enter 0.
# Afterward, print the total of all numbers entered.
# userInput = int(input("Enter a number to add to a total "))
#
# while userInput != 0:
#     userInput = int(input("Try again "))
#     total = userInput + userInput
# print(total)


# 5. Create an array of 4 names. Print one string that has all of the arrays separated by commas.
# nameArray = ["David", "Kenn", "Kevin", "John"]
# for index in nameArray:
#     print(index + ", ")


# 6. Create a function that’s passed three integer numbers.
# Print the sum of the first two numbers and return the product of the second two numbers.
# def intNumb(num1, num2, num3):
#     sum = num1 + num2
#     print(sum)
#     product = num2 * num3
#     print(product)
#
# intNumb(2, 12, 4)

#
# 7. Create the class Boardgame with name, price, pieceCount, and publisher
# properties/attributes. Create a class method that will change the price of the book.
# Outside of the class, create three objects of the class Boardgame.
# Print the three boardgame objects using the newly created objects.
# class Boardgame:
#     def __init__(self, name, price, pieceCount, publisher):
#         self.name = name
#         self.price = price
#         self.pieceCount = pieceCount
#         self.publisher = publisher
#     def changePrice(self, newPrice):
#         self.price = newPrice
#     def printAll(self):
#         print(f'{self.name}, {self.price}, {self.pieceCount}, {self.publisher}')
#
# game1 = Boardgame("Halo", "$25", "60piece", "Bungie")
# game2 = Boardgame("Chess", "$15", "20piece", "Oldstuff")
# game3 = Boardgame("Uno", "$5", "100piece", "ancient")
#
# game1.printAll()
# game2.printAll()
# game3.printAll()


# todo go back over this one <-------------------------------
# 8. Create a function that takes a string array and returns a string array with the
# letter 's' at the end of each element. Call the function.
# def someArray(str):
#     print(str + "'s")
#
#
# someArray("David")


# todo go back over this one
# 9. Create a function that has a parameter of an integer array and returns only
# the positive numbers in the array. Call the function
# def newParam(int):
#     numArray = [2, 4, 16, 7, 18, 9]
#     for index in numArray:
#         print(index)
#
#
# newParam(2)

# todo go back over this one
# 10. Create a Puppy class. It should have properties name and color.
# Create a program that will ask a user to enter the name,
# then the color of a puppy until they enter 'q' to quit. Put each entry in an array.
class Puppy:
    def __init__(self, name, color):
        self.name = name
        self.color = color


def newPuppy():
    userInput = ''
    while userInput != 'q':
        emptyArray = []
        userInput = input("Ready to quit hit 'q' ")
        userName = input("enter the name ")
        userColor = input("enter the color ")
        emptyArray.append(userName)
        emptyArray.append(userColor)

    print(emptyArray)


newPuppy()

# todo <-- the code below was an attempt to make the function work from within the class 
#         def newPuppy():
#                 userInput = ''
#                 while userInput != 'q':
#                     userName = input("enter the name ")
#                     userColor = userInput ("enter the color")
#
#                     Puppy(self.name(userName))
#
#                     # newArray.append(userColor)
#
#                 print(newArray)
#
#
# newPuppy()
