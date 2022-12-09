import random
from words import words
import string

def get_valid_word(words):
  word = random.choice(words)     # randomly chooses something from the list
  while '-' in word or ' ' in word:
    word = random.choice(words)
  return word.upper()

def hangman():
  word = get_valid_word(words)
  word_letters = set(word)  #variable that saves all the letters in a word as a set
  alphabet = set(string.ascii_uppercase)
  used_letters = set()      # what the user has guessed

  lives = 10

  # Getting user input
  while len(word_letters) > 0 and lives > 0:
    # letters used
    # ' '.join(['a', 'b', 'cd'])  --> 'a b cd'
    print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

    # what current word is (W - R D)
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word is: ', ' '.join(word_list))


    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:      # if this is a valid character in alphabet that I haven't used yet, then I'm gonna add this to used_letter
      used_letters.add(user_letter)
      if user_letter in word_letters:               # if the letter that I just guessed in the word, then I'm gonna remove that letter from word_letters
        word_letters.remove(user_letter)
      
      else:
        lives-=1
        print('Letter is not in the word')

    elif user_letter in used_letters:
      print('You already used that character. Please try again!')

    else:
      print('Invalid character. Please try again! ')

  if lives == 0:
    print('You died! The word was ', word)
  else:
    print('You guessed the word ', word)

hangman()
