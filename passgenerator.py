import random

def password_generator(length,strength):
    weak = "abcdefghijklmnopqrstuvwxyz"
    medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    strong = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()0123456789 "
    password=''
    if strength == 0:
        for i in range(length):
            password = password + random.choice(weak)

    if strength == 1:
        for i in range(length):
            password = password + random.choice(medium)

    if strength == 2:

        for i in range(length):
            password = password + random.choice(strong)
    
    return password

