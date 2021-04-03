money_invested = int(input("Yatıracağınız Para: "))
duration = int(input("Kaç Gün Boyunca: "))
interest = int(input("Yüzde Kaç Faiz İle: "))
profit = money_invested*(1+interest/100)**duration-money_invested
print("Kazancınız:", int(profit))
total_money= profit + money_invested
print("Toplam Paranız:", int(total_money))