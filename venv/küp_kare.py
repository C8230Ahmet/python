çift= []
tek = []
for i in range(1,20):
    if i % 2 == 0:
        küp = i**3
        çift.append(küp)
    else:
        kare = i**2
        tek.append(kare)
print(çift)
print(tek)