#Challenge numbers = [5,2,5,2,2] design the F pattern

for i in [2,2]:
    for j in range(5,10,5):
        print("x"*j)
    print("x"*i)
print("x"*2)

#- done by mosh code -PAttern F
numbers = [5,2,5,2,2]
for i in numbers:
    print("x"*i)

  #Challenge - pattern F by me

for i in [2,2]:
    for j in range(5,10,5):
        print("x"*j)
    print("x"*i)
print("x"*2)

#- done by mosh code for pattern F
numbers = [5,2,5,2,2]
for i in numbers:
    print("x"*i)

#done by raghav - pattern F
for i in range(6):
    if(i==0 or i==2):
        print("*"*5)
    else:
        print("*"*2)

#done by Mosh for pattern F

numbers = [5,2,5,2,2]
for i in numbers:
    output = ''
    for j in range(i):
        output += 'x'
    print(output)