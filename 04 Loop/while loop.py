print('Welcome to Jungle Resturant\n')
print('Enter the dishes you want\n')
print('NOTE:Enter stop to stop the list\n')
x=input('What you would like to have first\n')
print(x)
loop=True
while loop:
    name=input('Food will be prepared,Enter the next dish\n',)
    if name=='stop':
        break
