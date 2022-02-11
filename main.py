import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

playerChoice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors"))
computerChoice = random.randint(0, 2)

if playerChoice == 0:
    print(f"Player Choice : \n{rock}")
    if computerChoice == 1:
        print(f"Compter Choice : \n{paper}")
        print("Computer Has Won!!!")
    elif computerChoice == 0:
        print(f"Compter Choice : \n{rock}")
        print("It is a draw!!!")
    else:
        print(f"Compter Choice : \n{scissors}")
        print("Player Has Won!!!")

if playerChoice == 1:
    print(f"Player Choice : \n{paper}")
    if computerChoice == 1:
        print(f"Compter Choice : \n{paper}")
        print("It is a draw!!!")
    elif computerChoice == 0:
        print(f"Compter Choice : \n{rock}")
        print("Player Has Won!!!")
    else:
        print(f"Compter Choice : \n{scissors}")
        print("Computer Has Won!!!")

if playerChoice == 2:
    print(f"Player Choice : \n{scissors}")
    if computerChoice == 1:
        print(f"Compter Choice : \n{paper}")
        print("Player Has Won!!!")
    elif computerChoice == 0:
        print(f"Compter Choice : \n{rock}")
        print("Computer Has Won!!!")
    else:
        print(f"Compter Choice : \n{scissors}")
        print("It is a tie!!!")
