import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()") 

def generatePass():
    password_length = int(input("how long u want ur passsword to be"))

    random.shuffle(characters)

    password = []
    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("do u want to generate passowrd (Y/N) : ")

if option == "Y" or "y":
    generatePass()
elif option == "N" or "n":
    print("terminated")
    quit()
else:

    print("input Y or N")
    quit()