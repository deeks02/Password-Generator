#Password Generator

import string
import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
digits = "0123456789"
symbols = "!@#$%^&*()_+=-\\|{}[];'/?.,<>:"

all_combs = uppercase + lowercase + digits + symbols

def password_generator(amount):
    for x in range(amount):
        password = "".join(random.sample(all_combs,random.randint(8,16)))
        print(password)

def strengthen_password(userpass,desired_length):
    add_on = desired_length - len(userpass)
    password_to_add = "".join(random.sample(all_combs,add_on))
    new_password = userpass + password_to_add
    print(new_password) 

def main():
    choice = input("Press (G) to generate a new password or press (S) to strengthen your password:").upper()

    if choice == 'G' :
        amount = int(input("Enter the amount of the passwords you wish to generate:"))
        password_generator(amount)

    elif choice == 'S' :
        userpass = input("Enter the password to be strengthened:")
        desired_length = int(input("Enter the desired length of the password:"))
        strengthen_password(userpass,desired_length)

    else:
        print("Invalid input... Please enter (G) or (S)")

main()