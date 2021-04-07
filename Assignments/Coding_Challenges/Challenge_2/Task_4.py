# 4. User input
age = input("What is your age? ")
retire_age = 65 - int(age)
print('There are '+str(retire_age)+' years until you reach retirement.')

# Works fine, but fails if I give any input other than an int. Make sure you catch that problem
# and warn the user.