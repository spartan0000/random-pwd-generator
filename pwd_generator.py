#random password generator
#ask user for pwd length 

import string
import random

#possible characters
characters = list(string.ascii_letters + string.digits + "!@#$%^&*")

def createPassword(length):
	
	#take input and covert from string to integer
	length = int(length)
	
	random.shuffle(characters)

	password = []

	for i in range(length):
		password.append(random.choice(characters))

	random.shuffle(password)

	password = "".join(password)
	print(password)


initialQuestion = input("Do you want to generate a password (y or n)  ")

if initialQuestion == 'y':
	length = input("How long do you want your password to be?  ")
	createPassword(length)

elif initialQuestion == 'n':
	print("Exiting program")
	quit()
else:
	print('Invalid input')
	quit()
