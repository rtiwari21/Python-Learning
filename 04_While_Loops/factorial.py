#7. Find the product of numbers from 1 to N (factorial).

n=int(input("enter the number"))
i=1
num=1

while i<=n:
    num=num*i
    i=i+1
print(f'Product = {num}')