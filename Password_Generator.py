
#Password_Generator 
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = [
    '0','1','2','3','4','5','6','7','8','9'
    ]
symbols = [
    '!','@','#','$','%','&','*','(',')','-','_','=',
    '+','[',']','{','}',';',':',',','.','<','>','?','/','|'
    ]
import random

print("Welcome to the Password Generator!")
size = int(input("How many caracters would you like your password to be? \n"))
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))

password_lists = []

if size == (nr_letters+nr_numbers+ nr_symbols):
    for char in range(1, nr_letters + 1):
        password_lists.append(random.choice(letters))

    for char in range(1, nr_numbers + 1):
        password_lists.append(random.choice(numbers))

    for char in range(1, nr_symbols + 1):
        password_lists.append(random.choice(symbols))
    
    # O termo SHUFFLE embaralha as letras da lista funciona apenas com listas.
    random.shuffle(password_lists) 
    
    # the Password that will be provided to the user
    password = ""   
    for char in password_lists:
        password += char
    print(f"Your password is: {password}")
else :
    print("The number of characters in your password must equal the sum of the number of letters, numbers, and symbols.")

