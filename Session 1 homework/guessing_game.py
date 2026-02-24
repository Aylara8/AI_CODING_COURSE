import random

# The computer picks a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("--- The Hot & Cold Guessing Game ---")
print("I am thinking of a number between 1 and 100.")

while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1
    
    # Calculate how far away the guess is
    # abs() makes sure the number is positive
    difference = abs(secret_number - guess)

    if guess == secret_number:
        print(f"BINGO! You found it in {attempts} tries!")
        break
    elif difference <= 5:
        print("You're ON FIRE! (Extremely close)")
    elif difference <= 15:
        print("You're getting WARM!")
    elif difference <= 30:
        print("You're COLD.")
    else:
        print("You're FREEZING!")
