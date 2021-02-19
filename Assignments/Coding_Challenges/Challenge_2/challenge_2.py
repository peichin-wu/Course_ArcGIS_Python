# 1. List values
number_list = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
del number_list[3:10]
print(number_list)

# 2. List overlap
list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']
list_both = []
for i in list_a:
    for j in list_b:
        if i==j:
            list_both.append(i)
print(list_both)
list_not_overlap = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
for i in list_a:
    for j in list_b:
        if i==j:
            list_not_overlap.remove(i)
print(list_not_overlap)

# 3. Given a singe phrase, count the occurrence of each word
my_string = 'hi dee hi how are you mr dee'

a = my_string.split(" ")
unique_list=[]
for word in a:
    if word in unique_list:
        continue
    else:
        count = 0
        for i in a:
            if (word == i):
                 count = count+1
        print(word,count)
    unique_list.append(word)
# 4. User input
age = input("What is your age? ")
retire_age = 65 - int(age)
print('There are '+str(retire_age)+' years until you reach retirement.')

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

