import random
def get_choices():
    player_choice = input("enter any choice from 1-rock , 2-paper , 3-scissors")
    options = ["rock" , "paper" , "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice , "computer" : computer_choice}
    return choices

def check_win(player , computer):
    print( f"you chose {player} computer chose {computer}")

    if player == computer:
        return print("it is a tie")
    elif player == "rock":
     if computer == "scissors":
      return "rock smashes scissors"
    elif player == "paper":
     if computer == "rock":
      return print("paper covers rock")
    elif player == "rock":
     if computer == "scissors":
      return print("scissors covers rock")
    else:
      print("rock smashes scissors")

choices = get_choices()
result = check_win(choices["player"] , choices["computer"])
print(result)
    