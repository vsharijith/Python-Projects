import random
Rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [Rock, Paper, Scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user_choice >=3 or user_choice < 0:
    print('You entered an invalid number. You Lose!')
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    rock = "Rock"
    paper = "Paper"
    scissor = "Scissors"
    game_list = [rock, paper, scissor]
    print(f"Computer chose {game_list[computer_choice]}")
    print(game_images[computer_choice])

    if computer_choice == user_choice:
        print("Its a Draw")
    elif user_choice == 0 and computer_choice == 1:
        print("Computer Wins")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win")
    elif user_choice == 1 and computer_choice == 2:
        print("Computer Wins")
    elif user_choice == 2 and computer_choice == 0:
        print("Computer Wins")
    elif user_choice == 2 and computer_choice == 1:
        print("You Win")
    else:
        print("You typed an invalid number, You lose!")