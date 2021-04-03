aylar = [['January', 31], ['February', 28], ['March', 31], ['April', 30], ['May', 31], ['June', 30], ['July', 31], ['August', 31], ['September', 30], ['October', 31], ['November', 30], ['December', 31]]
ilkbahar = [aylar[2],aylar[3],aylar[4]]
yaz = [aylar[5],aylar[6],aylar[7]]
sonbahar = [aylar[8],aylar[9],aylar[10]]
kış = [aylar[11],aylar[0],aylar[1]]
print(ilkbahar)
print(yaz)
print(sonbahar)
print(kış)
yaz_gün_sayısı = yaz[0][1] + yaz[1][1] + yaz[2][1]
ilkbahar_gün_sayısı = ilkbahar[0][1] + ilkbahar[1][1] + ilkbahar[2][1]
sonbahar_gün_sayısı = sonbahar[0][1] + sonbahar[1][1] + sonbahar[2][1]
kış_gün_sayısı = kış[0][1] + kış[1][1] + kış[2][1]
print("Yaz toplam bu kadar gün :" + yaz_gün_sayısı)
print("Kış toplam bu kadar gün :" + kış_gün_sayısı)
print("İlkbahar toplam bu kadar gün :" + ilkbahar_gün_sayısı)
print("Sonbahar toplma bu kadar gün :" + sonbahar_gün_sayısı)