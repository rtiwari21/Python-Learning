# Write a program to guess the secret number ,
# if its low you print too low or else too high , run the loop until you find the secret number and in exit print the number of tries in which you were successfull

secret_number = 27
i = 1
while i > 0:
    guess = int(input("Enter your guess: "))
    if guess > secret_number:
        print("Your guess is too high")
    elif guess < secret_number:
        print("Your guess is too low")
    elif guess == secret_number:
        break
    i += 1
print(i)