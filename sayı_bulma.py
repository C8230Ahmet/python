import random
x = 10
sayı = random.randint(1, x)
tahmin = int(input("Tuttuğum sayıyı bul: "))
while tahmin != sayı:
    tahmin = int(input("Tuttuğum sayıyı bul: "))
    if tahmin > sayı:
     print("Çok yukarı gittin")
    elif tahmin < sayı :
        print("Çok az söyledin")
    if tahmin == sayı :
        print("Doğru bildin")