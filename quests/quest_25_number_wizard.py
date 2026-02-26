secret_number = 42

while True:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Correct! You guessed it!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
