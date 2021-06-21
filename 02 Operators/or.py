food = input('Choose any food you like from below option\n1.Briyani\n2.Shawarma\n3.Burger\n4.Pavv Bhaji\n5.Parotta\n6.Pizza\n',)
print (food)

if int(food) == 1 or int (food) == 5:
    print('You like South Indian')
elif int (food) == 2 or int (food) == 4:
    print('You like North Indian')
else:
    print('You like Western Foods')
