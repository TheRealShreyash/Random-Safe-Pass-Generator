import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$&*_"

while 1:
    password_len = int(input("What length of your password you would like to be generated: "))
    password_count = int(input("How many passwords you would like to be generated: "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Here you go! : ", password)