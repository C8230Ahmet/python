import random
def sayı(x):
    sayı = random.randint(1, x)
    tahmin = 0
    while tahmin != sayı:
        tahmin = int(input(f'1 ile {x} arasında bir sayı tahmin et :'))
        if tahmin < sayı:
            print("Çok az söyledin")
        elif tahmin > sayı:
            print(("Çok söyledin"))
    print("Bravo sayıyı buldun")
sayı(10)
