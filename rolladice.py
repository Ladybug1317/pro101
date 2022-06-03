import random
response = 'y'
while response == 'y':
    number = random.randint(1,6)
    if number == 1:
        print("[*]")

    if number == 2:
        print("[**]")

    if number == 3:
        print("[***]")

    if number == 4:
        print("[****]")

    if number == 5:
        print("[*****]")

    if number == 6:
        print("[******]")
    
    response = input("press y to roll dice again and b to exit")