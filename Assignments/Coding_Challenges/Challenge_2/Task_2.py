# 2. List overlap
# Using these lists:
#
# list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
# list_b = ['dog', 'hamster', 'snake']
# Determine which items are present in both lists.
# Determine which items do not overlap in the lists.

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

# Snake is missing from do not overlap task. I would suggest not using the list that you
# created in list_not_overlap unless you make this programmatically. For example:
new_list = list_a + list_b
# you can then test each word to see if it unique.