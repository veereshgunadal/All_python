import random

def play():
    
    player_choice = input(" What's your choice? rock(r), paper(p), scissor(s): \n")
    computer_choice = random.choice(["r", "p", "s"])
    print(f" computer_choice : {computer_choice} ")
    
    if player_choice == computer_choice:
        return "Its tie"
    
    if is_win(player_choice, computer_choice):
        return "Player win"
    
    return "Computer win"

def is_win(player, computer):
    if ((player == "r" and computer == "s") or 
        (player == "s" and computer == "p") or
        (player == "p" and computer == "r")):
        return True
    
    else:
        return False

print(play())