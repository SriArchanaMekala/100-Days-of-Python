import random
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
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
game_images = [rock, paper, scissors]
if user_choice >= 0 or user_choice <=2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])


print(f"Computer chose:{computer_choice}")
if user_choice >= 3 or user_choice < 0:
    print("You've entered an invalid number. You lose!")
elif user_choice == 0 and computer_choice ==2:
    print("You win!")
elif computer_choice ==0 and user_choice ==2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")
