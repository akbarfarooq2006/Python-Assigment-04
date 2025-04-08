# Constant for the sentence start
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

def main():
    # Prompt the user for an adjective, noun, and verb
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")
    
    # Create the fun sentence using the user inputs
    sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    
    # Print the final sentence
    print(sentence)

if __name__ == "__main__":
    main()