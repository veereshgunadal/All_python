import random
from wo import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6    

    while len(word_letters) > 0 and lives > 0:
        print(f"You left lives {lives} You used letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(word_list)
        print("current word: ",' '.join(word_list))
        
        print(word)
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives-1
                print("letter is not in word")

        elif user_letter in used_letters:
            print("You have already entered")
    
        else:
            print("Invalid char")
    if lives == 0:
        print("game over ")
    else:
        print(f"guessed word is {word} ")

hangman()