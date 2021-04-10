print("cevapları \"Var\" yada \"Yok\" olarak cevaplayınız")
kadayıf = str(input("sende kadayıf var mı? :"))
fındık_fıstık_ceviz = str(input("sende fındık, fıstık veya ceviz var mı? :"))
şeker = str(input("sende şeker var mı? :"))
yumurta =str(input("sende yumurta var m? :"))

if kadayıf == "Var" :
  kadayıf = True
else :
  kadayıf = False
if fındık_fıstık_ceviz == "Var" :
  fındık_fıstık_ceviz = True
else :
  fındık_fıstık_ceviz = False
if şeker == "Var" :
  şeker = True
else :
  şeker = False
if yumurta == "Var" :
  yumurta = True
else :
  yumurta = False
yaparsın = kadayıf and fındık_fıstık_ceviz and şeker and yumurta
if yaparsın ==  True :
  print("sen kadayıf yaparsın")
else :
  print("yeterli malzeme yok")

print("git deneme")
