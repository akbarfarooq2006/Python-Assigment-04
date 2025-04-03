import random




def guess_number(x1,x2):
    while True:
        print("Slect  the level of the game...")
        print("1.low")
        print("2.medium")
        print("3.high")
        level = input().lower().strip()
        if level not in ['low','medium', 'high',"1","2","3"]:
            print("⚠️Invalid level of input Select Correct")
            continue
        if level in ['low', "1"]:
            level="low"
            tries = 14
            x2=x2
        elif level in ['medium', "2"]:
            level="medium"
            tries = 10
            x2+=20
            
        elif level in ['high', "3"]:
            level="high"
            tries = 6
            x2+=35
        break

    random_number = random.randint(x1,x2)

    copy_tries =tries
    score=0
    
    
    print(" *** Welcome to the Number Gussing ****  ")
    print(f"Guess a number between {x1} and {x2}. You have {tries} tries. \n")
    print(f"*** Game Lavel is {level} *** \n")
    
    
    while tries > 0:
        print(f"You have {tries} tries left.")
        try:
            number_guess_by_user = int(input("Enter a guess number "))
            if number_guess_by_user < x1 or number_guess_by_user > x2:
                print("⚠️⚠️ Warning Number should be between", x1, "and", x2 ,"\n")# use to restrict to put number b/w x1 and x2
                continue
        except ValueError:
            print("⚠️Invalid input. Please enter a number. \n")
            continue
        
        if number_guess_by_user < random_number:
            print("Too low. Try again. \n")
        elif number_guess_by_user > random_number:
            print("Too high. Try again. \n")
        else:
            print(f"🥳 Congratulations! You guessed the number {random_number} correctly in {copy_tries - tries + 1} tries!")
            # Increase score
            score+=1
            print(f"🎈Your score is {score}")
            # Play again option jeetne ke baad
            while True:
                play_again = input("Do you want to play this game again? (yes✅/no❌): ").lower().strip()
                if play_again in ['yes', 'y', 'no', 'n']:
                    break
                print("Please enter 'yes' or 'no'.")
            if play_again in ['yes', 'y']:
                print("\n**** Welcome again to play this game ****")
                guess_number(x1, x2)
            else:
                print(f"🎈Your score is {score}")
                print("Thanks for playing!")
    
            return
        
        
        tries -= 1
        
        if tries == 0:
            print(f"Game Over! The number was {random_number}. Better luck next time!")
            # logic of play again
            while True:
                play_again = input("Do you want to play this game again? (yes✅/no❌): ").lower().strip()
                if play_again in ['yes',"y","n", 'no']:
                    break
                print("Please enter 'yes' or 'no'.")
            if play_again in ['yes', 'y']:
                print(" \n****Welcome again to play this game****")
                guess_number(x1, x2)  
            else:
                
                print(f"\n 🎈Your score is {score}")
                print("Thanks for playing!")
    
            return  
        
        
        
# Callung Functions 
guess_number(1,15)
        


