import figures
import random
import rules

#Game Intro
print("*"*60)
print("Welcome in the great game: Paper-Rock-Scissors-Lizard-Spock!")
print("*"*60)
read_rules = input("Do you want to quick recap the rules? (y/n)? ")

if read_rules.lower() == "y":
    print(rules.rules)
else:
    print("So let's go!")

print("*"*60)
print("1-Paper, 2-Rock, 3-Scissors, 4-Lizard, 5-Spock")
print("*"*60)

#User choice
user_choice = (int(input("Type figure number: "))-1)
move = ["Paper", "Rock", "Scissors", "Lizard", "Spock"]
figure_picture = [figures.paper, figures.rock, figures.scissors, figures.lizard, figures.spock]
print(f"So, your move is: {move[user_choice]}")
print(figure_picture[user_choice])

print("-"*70)

#Computer choice
computer_choice=random.randint(0,4)
print(f"Computer choice is: {move[computer_choice]}")
print(figure_picture[computer_choice])

#Game results
congratulation = "Congratulation! You win!"
solace = "You lose.\nDon't worry - try again."

if move[user_choice] == move[computer_choice]:
    print("It's a tie game!")
    exit()
#Paper
if move[user_choice] == "Paper" and (move[computer_choice] == "Rock" or move[computer_choice] == "Spock"):
    print(congratulation)
    print(f"Paper beats {move[computer_choice]}.")
#Rock
elif move[user_choice] == "Rock" and (move[computer_choice] == "Scissors" or move[computer_choice] == "Lizard"):
    print(congratulation)
    print(f"Rock crushes {move[computer_choice]}.")
#Scissors
elif move[user_choice] == "Scissors" and (move[computer_choice] == "Paper" or move[computer_choice] == "Lizard"):
    print(congratulation)
    print(f"Scissors cuts {move[computer_choice]}.")
#Lizard
elif move[user_choice] == "Lizard" and (move[computer_choice] == "Paper" or move[computer_choice] == "Spock"):
    print(congratulation)
    print(f"Lizard wins against {move[computer_choice]}.")
#Spock
elif move[user_choice] == "Spock" and (move[computer_choice] == "Rock" or move[computer_choice] == "Scissors"):
    print(congratulation)
    print(f"Spock smashes {move[computer_choice]}.")
else:
    print(solace)