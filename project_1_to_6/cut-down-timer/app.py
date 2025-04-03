import time
import os
import winsound

def clear_screen():
    # Screen clear karne ke liye (cross-platform)
    os.system('cls' if os.name == 'nt' else 'clear')
    


def play_beep():
   
    if os.name == 'nt':  
        import winsound
        winsound.Beep(5000, 1900)  
    
    
    
    
    
    
    
def cutdown_timer(seconds):
    while seconds:
        min,sec = divmod(seconds,60)  # this function wll give me time in this format 250 sec -->  4 min : 10 sec
        timer = '{:02d}:{:02d}'.format(min,sec)
        clear_screen()
        print("Timer working.")
        print(timer , end="\r")
        time.sleep(1)
        seconds -= 1
        
    clear_screen()
    print("Time's up! ⏰")
    play_beep()
    # play again logic
    while True:
        print("Do you want to start again? (Y/N): ", end="")
        choice = input().lower()
        if choice in ["y","yes"]:
            call()
            break
        elif choice in ["n","no"]:
            print("Thanks for using this timer!")
            exit()
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")  
    
    
    
    
    
    
    
def call():
    while True:
        try:
            seconds = int(input("Enter time in seconds: "))
            if seconds <= 0 :
                print("Please enter a positive number.")
                continue
            else:
                cutdown_timer(seconds)
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    
# first time call 
call()
    
    
    