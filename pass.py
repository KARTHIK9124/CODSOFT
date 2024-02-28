import random 
import math

def password_generator(length):
    password = ""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    for i in range(length):
        new = math.floor(random.random() * len(characters)) 
        password += characters[new]
    return password

pass_len = int(input("Enter password length: "))
gen_password = password_generator(pass_len)
print("Your password is:", gen_password)