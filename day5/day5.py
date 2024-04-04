import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for letter_keys in range(0,nr_letters):
    randomizer = random.randint(0, 25)
    password += letters[randomizer]

for number_keys in range(0, nr_numbers):    
    randomizer = random.randint(0, 9)
    password += numbers[randomizer]

for symbol_keys in range(0, nr_symbols):    
    randomizer = random.randint(0, 8)
    password += symbols[randomizer]
    
password = password
final_password = ""

for keys in range(0, len(password)):
    randomizer = random.randint(0, len(password)-1)
    final_password += password[randomizer]
    password_list = list(password)
    password_list.pop(randomizer)
    password = ''.join(password_list)

print(final_password)

