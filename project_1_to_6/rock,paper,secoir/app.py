import random 

def play():
    computer = random.choice(["r","p","s"])
    while True:
        user = input("What's your choice? 'r' for rock, 'p' for papper & 's' for scissors.")
        if user in ['r', 'p','s']:
            break
        print(f"Is in ''{user}'' Invalid input. Please choose 'r', 'p', or's' ")


    # r>s , s>p and p>r
    if user == computer:
        print(f"Computer chose {computer}. It's a tie!")
    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        print(f"🎈Computer chose {computer}. You win!")
    else:
        print(f" Computer chose {computer}. You lose!")
    





play()