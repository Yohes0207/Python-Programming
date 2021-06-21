age = input('Your age is',)
if int(age) <= 7:
    print('You are a child')
elif int(age) <= 12:
    print('You are a kid')
elif int(age) < 18:
    print('You are Minor')
elif int(age) <=40:
    print('You are Major')
else:
    print('You are Senior Citizen')
