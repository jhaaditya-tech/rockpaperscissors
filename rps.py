#Rock Paper Scissors Project
#Developed by Aditya Jha 08-Aug-2022

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#The ASCI for the hand is taken from Angela Yu

import random
list_data=[rock, paper, scissors]
list_var=["rock","paper","scissors"]
user_data=int(input("What do you Choose? Choose: Rock 0 ; Paper 1 ; Scissors 2 :::: "))
comp_data=random.randint(0,2)


if user_data<3:
    user_var = list_var[user_data]
    comp_var = list_var[comp_data]
    print(f"Your Choice: {user_var}")
    print(list_data[user_data])

    if (user_data == 0 and comp_data == 0) or (user_data == 1 and comp_data == 1) or (
            user_data == 2 and comp_data == 2):
        print(f"Computer Choice: {comp_var}")
        print(list_data[comp_data])
        print("It is a draw game")
    if (user_data == 0 and comp_data == 2) or (user_data == 1 and comp_data == 0) or (
            user_data == 2 and comp_data == 1):
        print(f"Computer Choice: {comp_var}")
        print(list_data[comp_data])
        print("You win")
    if (user_data == 2 and comp_data == 0) or (user_data == 0 and comp_data == 1) or (
            user_data == 1 and comp_data == 2):
        print(f"Computer Choice: {comp_var}")
        print(list_data[comp_data])
        print("Computer Wins")
else:
    print("Please enter the valid number as mentioned in description")
