import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while True:
        print("\n*** Welcome to the computer number guessing game *** ")
        print(f"Think a number between 1 & {x} and guide the computer till the your actual thought number \n")

        
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"\n🎈Yay! The computer guessed your number, {guess}, correctly! \n")
            while True:
                play_again = input("Do you want to play again? (Y/N): ").lower()
                if play_again == 'y':
                    computer_guess(x)
                elif play_again == 'n':
                    print("\nThanks for playing! ��")
                    break
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")
                    continue
    
    
computer_guess(1242)