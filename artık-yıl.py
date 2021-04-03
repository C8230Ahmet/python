year = int(input("Enter the year : "))
div4 = year % 4
div100 = year % 100
div400 = year % 400
leap = not div4 and not div100 and not div400
print(year, "is a leap year : ", leap)