import random
import string
from englishWords import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hang_man():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    print(word)
    lives = len(word_letters) + 3
    print(f'My lives {lives}')
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print(used_letters)

        # letters used
        # it turns this list into, or iterable into a string, separated by whatever the string is before the dot join
        print(f'You have {lives} lives and you have used these letters: ', ' '.join(used_letters))
        # we need to tell the user what the current word is, but with dashes where the characteres that they haven't guessed are.
        # I am going to create a list where every single letter that they have guessed is shown and all the letters that they haven't guessed, are just dashes.
        word_listp = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_listp))
        user_letter = input('Guess a letter: ').upper()
        # alphabet - used_letters: This gives you a set of letters that are in the alphabet but not in the set of used letters.
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 #take away a life if wrong
                print('Letter is not in the word')
        elif user_letter in used_letters:
            print('You have already used that character, Please try again.')
        else:
            print('Invalid character. Please try again.')

        # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print(f'Sorry you died the word was {word}')
    else:
        print(f'You guessed the word {word}!')


hang_man()
