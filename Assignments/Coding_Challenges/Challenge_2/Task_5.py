
# 5. User input 2
word = input("Please type a word ")
letter_scores = {
    "a": 1,"e": 1,"i": 1,"o": 1,"u": 1,"l": 1,"n": 1,"r": 1,"s": 1,"t": 1,
    "d": 2,"g": 2,
    "b": 3,"c": 3,"m": 3,"p": 3,
    "f": 4,"h": 4,"v": 4,"w": 4,"y": 4,
    "k": 5,
    "j": 8,"x": 8,
    "q": 10,"z": 10
}
count=0
for i in word:
    count = count + letter_scores[i]

print(count)

# Works if I provide a word, but anything else throws a key error, this is becasue your code right now
# does not check to see if the input is correct before calculating the score.