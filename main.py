"""
ask user to input a move
computer player will randomly generate move 
display the moves (print)
determine the winner
"""

import random 

play_again = "Y"

while play_again == "Y": 
  player_move = input("Enter your move: ").lower()


  while player_move != "rock" and player_move != "paper" and player_move != "scissors":
    player_move = input("Invalid move. Enter only scissors, paper, rock: ")

  random_number = random.randint(1, 3)

  if random_number == 1:
    computer_move = "rock"
  elif random_number == 2:
    computer_move = "paper"
  else: 
    computer_move = "scissors"

  print()
  print ("You played " + player_move)
  print ("Computer played " + computer_move)

  if player_move == computer_move:
    print ("Tie")
  elif player_move == "rock" and computer_move == "scissors":
    print ("you win")
  elif player_move == "paper" and computer_move == "rock":
    print ("You win")
  elif player_move == "scissors" and computer_move == "paper":
    print ("You win")
  else:
    print ("You lose")

  print()
  play_again = input("Do you want to play this again? Y or N? ").upper()
  print ()


  while play_again != "Y" and play_again != "N":
    play_again = input("Invalid input. Enter only Y or N: ").upper()

if play_again == "N".upper():
  print ()
  print("Have a good day! ")



 
 


