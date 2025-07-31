import random

def play_game():
    number = random.randint(1, 10)
    tries = 0
    print("🎲 Welcome to the Number Guessing Game!")

    while True:
        guess = input("Guess a number between 1 and 10: ")
        tries += 1

        if not guess.isdigit():
            print("❌ Please enter a valid number.")
            continue

        guess = int(guess)

        if guess == number:
            print(f"🎉 Correct! You guessed it in {tries} tries.")
            break
        elif guess < number:
            print("📉 Too low. Try again!")
        else:
            print("📈 Too high. Try again!")

play_game()
