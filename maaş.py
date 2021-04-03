haftalik_cal_suresi = int(input("Haftalık kanuni çalışma süresi nedir? "))
fazla_mesai_oranı = float(input("Fazla mesai yüzdesi nedir? "))
maas = float(input("Haftalık maaşın ne kadar? "))
calisilan_sure = float(input("Bu hafta kaç saat çalıştın? "))

saatlik_ucret = maas / haftalik_cal_suresi
if calisilan_sure > haftalik_cal_suresi :
  toplam_maas = maas + (calisilan_sure - haftalik_cal_suresi) * saatlik_ucret * fazla_mesai_oranı
  print("Alınacak maaş: ", toplam_maas)
else :
  print("Alınacak maaş: ", saatlik_ucret * calisilan_sure)