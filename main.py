from art import logo
import random

# Function to set the difficulty
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "hard":
    print("You have 5 attempts remaining to guess a number.")
    return 5
  else:
    print("You have 10 attempts remaining to guess a number.")
    return 10

# Function to compare the two numbers
def compare_number(guess, actual, attempts):
  """Checks guess against the actual number and returns the number of attempts left"""
  if guess > actual:
    attempts -= 1
    print("Too high.")
    print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess a number.")
    return(attempts)
  elif guess < actual:
    attempts -= 1
    print("Too low")
    print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess a number.")
    return(attempts)
  else:
    print (f"You got it. The answer was {actual}")

print(logo)
print("Welcome to the Number Guessing Game!")
target = random.randint(1, 100)

i = set_difficulty()
number_chosen = int(input("Make a guess: "))

while compare_number(number_chosen, target, i) != 0 and number_chosen != target:
  i -= 1
  number_chosen = int(input("Make a guess: "))