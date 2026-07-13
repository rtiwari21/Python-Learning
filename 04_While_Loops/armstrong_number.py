#8.Armstrong Number
number = input("Enter a number: ")
i=0
total = 0

while i < len(number):
    total= total + int(number[i])**len(number)
    i+=1
if int(number) == total:
    print(f'Armstrong Number : {total}')
else:
    print(f'Not Armstrong Number : {total}')