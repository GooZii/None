import random

sifre="+-/*!&#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"




son_sifre=""

sayı=int(input("Kaç defa tekrar etsin?"))

for i in range(sayı):
    son_sifre+=random.choice(sifre)

print(son_sifre)
