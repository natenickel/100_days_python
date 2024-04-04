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


print("Welcome to Rock, Paper, Scissors!")

option_list = [rock, paper, scissors]

user_input = int(input("Type 1 to choose rock 2 to choose paper and 3 to choose scissors\n"))
user_throw = option_list[user_input - 1]

computer_input = random.randint(1,3)
computer_throw = option_list[computer_input - 1]
outcome = "b"
if user_input == computer_input:
    outcome = "its a draw!"
if user_input == 1 and computer_input == 2 or user_input == 2 and computer_input == 3 or user_input == 3 and computer_input == 1:
    outcome = ("You lose sorry.")
if user_input == 2 and computer_input == 1 or user_input == 1 and computer_input == 3 or user_input == 3 and computer_input == 2:
    outcome = ("You win!")

print(f"You threw\n {user_throw}\n they threw\n {computer_throw}\n {outcome}")
