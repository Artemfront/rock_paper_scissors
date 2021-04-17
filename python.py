import random 

def play():
    rock = 1
    paper = 2
    scissors = 3
    user = int(input("What do you want to choose? '1' for rock, '2' for paper, '3' for scissors \n "))
    computer = random.choice([1, 2, 3])

    if user == computer:
        return "It is a tie"

    elif (user == 1 and computer == 2):
        print("I won!")
    elif (user == 1 and computer == 3):
        print("You won!")
    elif (user == 2 and computer == 1):
        print("I won!")
    elif (user == 2 and computer == 3):
        print("You won!")
    elif (user == 3 and computer == 1):
        print("I won!")
    elif (user == 3 and computer == 2):
        print("You won!")
    print(input())
print(play())
