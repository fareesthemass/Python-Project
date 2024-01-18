#Random Password Generator

import random
print("Welcome to the random Password generator!")
a=int(input("Enter how many passwords needed :"))
b=int(input("Enter how much lenth needed :"))
c='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*;~<>'
print("Here is your passwords:")
for i in range(a):
    pwd=''
    for x in range(b):
        pwd=pwd+random.choice(c)
    print(pwd)

