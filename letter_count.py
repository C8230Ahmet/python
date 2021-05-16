sentence = str(input("Write a sentence: ")).lower()
letters = set(sentence)
let_count ={}
for i in letters:
    let_count[i] = sentence.count(i)
print(let_count)
