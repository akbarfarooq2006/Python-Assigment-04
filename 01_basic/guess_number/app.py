import random

def main():
   secrte_number=random.randint(1,100)
   print("🎊 Wwlcome to Number guessing game... \n")
   
   while True:
       guess = int(input("Guess the number (1-100): "))
       
       if guess == secrte_number:
           print(f"🎉 Congratulations! You've guessed the correct number which is {guess}")
           while True:
                play_again = input("Do you want to play again? (yes/no): \n").lower()
                if play_again in ["yes", "y"]:
                   main()
                elif play_again in ["no", "n"]:
                   print("Thanks for playing!")
                   return
       elif guess < secrte_number:
           print("Too low!  Try again.")
       else:
           print("Too high! Try again.")

   
if __name__ == '__main__':
    main()
