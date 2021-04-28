sıcaklık = float(input("Bir sıcaklık değeri girin :"))
tür = input("C mi F mi? :")
if tür == "C":
    print(sıcaklık*(9/5)+32, "F")
if tür == "F":
    print((sıcaklık-32) * 59, "c")