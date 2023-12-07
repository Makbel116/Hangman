from random import choice
from hang_man_word_list import random_words
from hang_man_art import HANGMAN

# Initialize variables
guessed_letter=""
choosen_word=choice(random_words)
word_length=len(choosen_word)
found_letters=["_"]*word_length
attempts=0


def accept_guess():
  """
    Accepts a guess from the user and checks if it is valid.
    """
  global guessed_letter
  guessed_letter=(input("put your guess:\n")).lower()
  if len(guessed_letter)!=1:
    print("please enter a valid answer!!")
    accept_guess()
    print()
  else:
    checking_guess()
    print()


def checking_guess():
  """
    Checks if the guessed letter is in the chosen word.
    """
  global found_letters,attempts
  if guessed_letter in choosen_word:
    if guessed_letter in choosen_word:
      for i in range(word_length):
          if guessed_letter == choosen_word[i]:
              found_letters[i] = guessed_letter
      found_word="".join(found_letters)
      print(found_word)
      if found_word == choosen_word:
          print(f"Congrats!! you just won!! the word was ' {choosen_word}'" )
      else:
          accept_guess()
  else:
      attempts+=1
      hanging(attempts)


def hanging(attempts:int):
  """
  Prints the hangman art based on the number of attempts.
  """
  if attempts == 6:
    print(HANGMAN[6])
    print("You Lose!!!")
    print(f"the word was '{choosen_word}' ")
  elif attempts == 5:
    print(HANGMAN[5])
    print("Wrong guess!! try again")
    accept_guess()
  elif attempts == 4:
    print(HANGMAN[4])
    print("Wrong guess!! try again")
    accept_guess()
  elif attempts == 3:
    print(HANGMAN[3])
    print("Wrong guess!! try again")
    accept_guess()
  elif attempts == 2:
    print(HANGMAN[2])
    print("Wrong guess!! try again")
    accept_guess()
  elif attempts == 1:
    print(HANGMAN[1])
    print("Wrong guess!! try again")
    accept_guess()
  else:
    print(HANGMAN[0])
    print("Wrong guess!! try again")
    accept_guess()