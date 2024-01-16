import random

password_lengh = int( input('Jak dlugie ma byc Haslo'))

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

safe_Passwort = random.choice(characters)

for i in range(password_lengh):
    safe_Passwort += random.choice(characters)


password_lengh = ""



print(safe_Passwort)
