import string
import random

# print(string.printable)


def generatePassword(num):
    password = ''
    for n in range(num):
        x = random.randint(0, 63)
        password += string.printable[x]
    return password


print(generatePassword(10))
