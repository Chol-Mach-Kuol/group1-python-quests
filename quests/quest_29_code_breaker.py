secret_code = 42

for attempt in range(1, 4):
    guess = int(input(f"Attempt {attempt} - Enter your guess: "))

    if guess == secret_code:
        print("Correct! You have cracked the code!")
        break
    elif attempt < 3:
        print("Wrong guess. Try again.")
    else:
        print(f"Out of attempts! The secret code was {secret_code}.")
