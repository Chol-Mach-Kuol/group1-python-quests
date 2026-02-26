secret_number = 7

while True:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Correct! You guessed it!")
        break
