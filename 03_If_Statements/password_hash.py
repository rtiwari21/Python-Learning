import hashlib

username = input("Enter your username: ")
password = input("Enter your password: ")

hashed = hashlib.sha256(password.encode("utf-8")).hexdigest() # encode the password
print(password)
print(hashed)