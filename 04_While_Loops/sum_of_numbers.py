#6.Find the sum of numbers from 1 to N.

n=int(input("enter the number"))
i=0
num=0

while i<=n:
    num=num+i
    i=i+1
print(f'Sum = {num}')