#Library required
import random

#Introduction and display of options
print("Made by cn1Qu9n.\n")
print(
    "Easy: 3 tries to guess numbers 0 to 10.\nHard: 5 tries to guess numbers 0 to 20.\n"
)

#Variables
Easy_List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Hard_List = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
]
Easy = str(random.choice(Easy_List))
Hard = str(random.choice(Hard_List))
Answer = 0


#Definitions of functions
def Level():
    Difficulty = input("Difficulty (Easy/Hard): ")
    if Difficulty == "Easy":
        Easy_Level()
    elif Difficulty == "Hard":
        Hard_Level()
    else:
        print(
            "Invalid input. Only \"Yes\" or \"No\" is allowed (Case sensitive). Please try again."
        )
        Level()


def Easy_Level():
    Tries = 0
    while Tries < 3:
        Tries = Tries + 1
        Answer = input("Enter your guess: ")
        if Answer < Easy:
            print("The number is higher!")
        elif Answer > Easy:
            print("The number is lower!")
        elif Answer == Easy:
            print("You won!\n")
            Resume()
    else:
        print("You lost!")
        Resume()


def Hard_Level():
    Tries = 0
    while Tries < 5:
        Tries = Tries + 1
        Answer = input("Enter your guess: ")
        if Answer < Hard:
            print("The number is higher!")
        elif Answer > Hard:
            print("The number is lower!")
        elif Answer == Hard:
            print("You won!\n")
            Resume()
    else:
        print("You lost!")
        Resume()


#To determine whether to resume
def Resume():
    Keep_Playing = input("Do you want to continue playing (Yes/No)? ")
    print("\n")
    if Keep_Playing == "Yes":
        Level()
    elif Keep_Playing == "No":
        print("Exiting...")
        exit()
    else:
        print("Invalid input. Only \"Yes\" or \"No\" is allowed (Case sensitive). Please try again.")
        Resume()

#Start of functions
Level()
