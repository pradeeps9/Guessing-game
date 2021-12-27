import random

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 to 100")
secret_num = random.randint(1, 100)
print(f"This is for you {secret_num}")

win = False

def choose_level ():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return 10
  elif level == 'hard':
    return 5
  else :
    return 0

  
attempts = choose_level()
guess = 0

while attempts != 0 and guess != secret_num :
  print(f"You have {attempts} attempts remaining to guess the number")
  guess = int(input("Make a guess: "))

  if guess > secret_num:
    print("Too high. \nGuess again")
  elif guess < secret_num:
    print("Too low. \nGuess again")
  else:
    print(f"You got it! The answer was {secret_num}")

  attempts -= 1

