# ATM Machine
balance = 10000
print("Menu \n Check Balance \n Deposit \n Withdraw \n Exit")

while True:
    userInput = input("> ").lower()

    if userInput == "withdraw":
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw > balance:
            print("Insufficient Balance\nYour current balance is: ", balance)
        else:
            balance -= withdraw
            print("Current Balance:", balance)
    elif userInput == "deposit":
        deposit = int(input("Enter the amount you want to deposit: "))
        balance += deposit
        print("Your balance is: ", balance)
    elif userInput == "check balance":
        print("Current Balance:", balance)
    elif userInput == "exit":
        break
    else:
        print("Invalid Input, please enter again")
print("Thank you for using this ATM")