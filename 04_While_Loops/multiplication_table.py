#5. Print the multiplication table of any number.

number = int(input("Enter a number: "))
i=1
while i<=10:
    mul= i * number
    print(f'{number} * {i}  = {mul}')
    i+=1