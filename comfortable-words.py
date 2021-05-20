word = set(str(input("Enter a word: ")).lower())
left = {"a","e"}
right = {"u","ı","o","i","ö"}
both = left.intersection(right)
if word.isdisjoint(left) == True:
    print("uses only left hand")
elif word.isdisjoint(both) == True:
    print("uses both hands")
if word.isdisjoint(right) == True: 
    print("uses only right hand")
