import requests
import random

# Hangman drawing stages
HANGMAN_STAGES = [
    # Stage 0: Empty gallows
    """
  _____
  |   |
      |
      |
      |
      |
    ===
    """,
    # Stage 1: Rope
    """
  _____
  |   |
  |   |
      |
      |
      |
    ===
    """,
    # Stage 2: Head
    """
  _____
  |   |
  |   |
  O   |
      |
      |
    ===
    """,
    # Stage 3: Left eye
    """
  _____
  |   |
  |   |
  0   |
      |
      |
    ===
    """,
    # Stage 4: Right eye
    """
  _____
  |   |
  |   |
  0 0 |
      |
      |
    ===
    """,
    # Stage 5: Mouth (sad expression)
    """
  _____
  |   |
  |   |
  0 0 |
   -  |
      |
    ===
    """,
    # Stage 6: Torso
    """
  _____
  |   |
  |   |
  0 0 |
   -  |
  |   |
    ===
    """,
    # Stage 7: Left arm
    """
  _____
  |   |
  |   |
  0 0 |
   -  |
 /|   |
    ===
    """,
    # Stage 8: Right arm
    """
  _____
  |   |
  |   |
  0 0 |
   -  |
 /|\  |
    ===
    """,
    # Stage 9: Left leg
    """
  _____
  |   |
  |   |
  0 0 |
   -  |
 /|\  |
 /    |
    ===
    """,
    # Stage 10: Right leg
    """
  _____
  |   |
  |   |
  0 0 |
   -  |
 /|\  |
 / \  |
    ===
    """,
    # Stage 11: Left hand
    """
  _____
  |   |
  |   |
  0 0 |
   -  |
/|\  |
/ \  |
    ===
    """,
    # Stage 12: Right hand (game over)
    """
  _____
  |   |
  |   |
  0 0 |
   -  |
/|\\\ |
/ \  |
    ===
    """
]


# API se words fetch karna
def fetch_words():
    url = "https://www.randomlists.com/data/words.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return []

# Hangman game
def hangman():
    # Words fetch karna
    words = fetch_words()
    if not words:
        print("No words available. Exiting...")
        return
    
    while True:
        # Random word chunna
        word = random.choice(words).lower()
        word_letters = set(word)  # Word ke unique letters
        guessed_letters = set()   # User ne kaunse letters guess kiye
        wrong_guesses = 0         # Galat guesses ka count
        max_wrong = len(word)+3        # Maximum galat guesses allowed
        
        print("\nWelcome to Hangman!")
        print("Try to guess the word, one letter at a time.")
        
        while wrong_guesses < max_wrong:
            # Current state dikhana
            print(HANGMAN_STAGES[wrong_guesses])
            print("Word: ",end="")
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print("\n")
            print(f"Guessed letters: {guessed_letters}")
            print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
            
            # User se guess w
            guess = input("Guess a letter: ").lower().strip()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue
            else:
                guessed_letters.add(guess)
            
            # Check the guess right or wrong
            if guess not in word_letters:
                print("Wrong guess!")
                wrong_guesses += 1
            
            # Check the iser win or lose
            if all(letter in guessed_letters for letter in word_letters):
                print(f"\n🎈🥳 Congratulations! You guessed the word: {word}")
                break
        
        # if user lose
        if wrong_guesses == max_wrong:
            print(HANGMAN_STAGES[wrong_guesses])
            print(f"😒 Game Over! The word was: {word}")
        
        # Play again
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower().strip()
            if play_again in ['yes', 'y', 'no', 'n']:
                break
            print("Please enter 'yes' or 'no'.")
        if play_again in ['no', 'n']:
            print("Thanks for playing! Goodbye!")
            break

# Game start
hangman()