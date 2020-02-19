import string
import random

# print(string.printable)

num = int(input('Z ilu znaków ma składać się hasło? : '))

def generatePassword(num):
    password = ''
    for n in range(num):
        x = random.randint(0, 63)
        password += string.printable[x]
    return password

print('Twoje hasło to: ' + generatePassword(num))

