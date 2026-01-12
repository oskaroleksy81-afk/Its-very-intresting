import random


znaki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

dlugosc = int(input("Podaj długość hasła: "))

haslo = ""

for _ in range(dlugosc):
    losowy_znak = random.choice(znaki)
    haslo += losowy_znak

print(haslo)


 