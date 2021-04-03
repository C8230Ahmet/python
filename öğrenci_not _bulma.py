names = ["David", "Michael", "John", "James", "Greg", "Mark", "William",
"Richard", "Thomas", "Steven", "Mary", "Susan", "Maria", "Karen",
"Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]
scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97,98]
öğrenci_ad = input("Öğrenci adını girin :")
a = names.index(öğrenci_ad)
öğrenci_not = scores[a]
print(f'{öğrenci_ad} isimli öğrencinin notu: {öğrenci_not}')