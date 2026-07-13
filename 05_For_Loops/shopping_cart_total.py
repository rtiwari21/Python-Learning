#write a program to calculate the total cost of all the items in the shopping cart . prices = [10,20,30]

prices=[10,20,30]
total=0
total1=0
for i in prices:
    total=sum(prices)
print(total)

# Another way to write this
for price in prices:
    total1+=price
print(total1)