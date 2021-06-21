print('Check your grocery list')
grocery=[' ','Rice','Flour','Eggs','Bread','Cheese','Butter']
print(grocery)
dec=input('Do you want to add any item?Y/N\n',)
if dec=='Y' or dec=='y':
    addd=input('Enter the item to be added to the list\n',)
    grocery.append(addd)
    ad=input('Do you want to change any item?Y/N\n')
    if ad=='Y' or ad=='y':
        add=input('Enter the S.No of the item\n',)
        item=input('Enter the Item to be changed\n',)
        grocery[int(add)]=item
        print('The item has been changed') 
    else:
        print('Thank You,The item has been added to the list')
else:
    print('The edited Grocery list is\n')
print(grocery)
    
    
