import random
from words import words
import string

def main():
    print("Welcome to hangman!\n")
    word = get_word()
    alphabet = set(string.ascii_uppercase)
    current_word = set(word)
    used_letters = set()
    lives = 10
    
    while len(current_word) > 0 and lives > 0:
        print(lives, "lives left, you have used:", " ".join(used_letters), "\n")
        show_current_word = [letter if letter in used_letters else "-" for letter in word]
        print("current word:", " ".join(show_current_word), "\n")
        print("Guess a letter: ", end="")
        guess = input().upper()
        if guess not in alphabet:
            print("\nPlease enter a valid letter.")
        else:
            if guess in used_letters:
                print("\nYou have already used that letter.")
            else:
                used_letters.add(guess)
                if guess in word:
                    current_word.remove(guess)
                else:
                    print("\nYour letter", guess, "is not in the word.")
                    lives -= 1
        print("")
    if lives == 0:
        print("Sorry. You lose. Better luck next time. The word was", word)
    else:
        print("Congratulations. You win. You guessed", word)

def get_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()
    
main()
