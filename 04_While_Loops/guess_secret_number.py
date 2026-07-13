# Guess the secret number with 3 retries

secret_number = 5
i = 0

while i < 3:  # Optionally have an else part
    guess_number = int(input("Guess: "))
    i += 1
    if guess_number == secret_number:
        print("Correct")
        break   # terminate the while loop
else:
    print("You failed")