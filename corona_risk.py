age = input("Are you a cigarette addict older than 75 years old?")
chronic = input("Do you have a severe chronic disease?")
immune = input("Is your immune system too weak?")
if age == "Yes":
    age = True
else:
    age = False
if chronic == "Yes":
    chronic = True
else:
    chronic = False
if immune == "Yes":
    immune = True
else:
    immune = False
risk = (age or chronic or ((age or chronic) and immune))
if risk == True:
    print("You are in risky group")
else:
    print("You are not in risky group")