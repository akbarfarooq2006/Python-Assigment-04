


def joke():
    JOKE: str = "\n'Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'\n"
    print("\nwlcome to joke bot 🤖")
    
    your_input = input("What do you want 🧐? ").capitalize().strip()
    if your_input =="Joke":
        print(JOKE)
    else:
        print("Sorry I only tell jokes.")
    
    while True:
        response = input("\nDo you want to hear another joke? [yes/no] ").lower()
        if response in ["yes", "y"]:
            joke()
        elif response in ["no", "n"]:
            print("Goodbye! 👋")
            break
        else:
            print("\nInvalid input. Please enter 'yes/y' or 'no/n'.")
    
            
        
        


if __name__ == "__main__":
    joke()


