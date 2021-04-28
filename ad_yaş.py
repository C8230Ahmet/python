ad_1 = input("Bir ad girin :")
yaş_1 = int(input("Bu kişinin yaşını girin :"))
ad_2 = input("Başka bir ad girin :")
yaş_2 = int(input("Bu kişinin yaşını girin :"))
ad_3 = input("Sonuncu adı girin :")
yaş_3 = int(input("Bu kişinin yaşını girin :"))
adlar = [ad_1, ad_2, ad_3]
yaşlar = [yaş_1, yaş_2, yaş_3]
max_yaş = max(yaşlar)
a = yaşlar.index(max_yaş)
print("En yaşlı kişi", adlar[a])
