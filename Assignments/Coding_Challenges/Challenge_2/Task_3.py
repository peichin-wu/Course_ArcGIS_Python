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

#all good, but add some comments to show your activity.