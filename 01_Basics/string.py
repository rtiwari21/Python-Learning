# String

course = 'This is a Python course'
print(course[0])  # starts the index from starting i.e 0
print(course[-1])  # starts from end of the string
print(course[1:5])  # print from index 1 to 5
print(course[:])  # prints the entire string
print(len(course))  # Number of character in the string
print(course[1:-1])  # will take the middle characters from 1 index to -1
s = "abcdefg"
s[1:5:1]     # 'bcde'  → normal forward slice
s[1:5:2]     # 'bd'    → forward, skipping every other char
s[5:1:-1]    # 'fedc'  → backward, from index 5 down to (not including) index 1
s[::-1]      # 'gfedcba' → backward, entire string