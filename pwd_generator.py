#random password generator
#ask user for pwd length 

import string
import random

#possible characters
characters = list(string.ascii_letters + string.digits + "!@#$%^&*")

def createPassword(length):
	password_length = int(input("How long do you want your password to be? "))

	random.shuffle(characters)

	password = []

	for i in range(password_length):
		password.append(random.choice(characters))

	random.shuffle(password)

	password = "".join(password)
	print(password)


initialQuestion = input("Do you want to generate a password (y or n)  ")

if initialQuestion == 'y':
	createPassword()
elif initialQuestion == 'n':
	print("Exiting program")
	quit()
else:
	print('Invalid input')
	quit()