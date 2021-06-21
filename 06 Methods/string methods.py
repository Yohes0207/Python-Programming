# .strip()
text=input('Type Something: ')
print(text.strip())

# .len()
text=input('Input Password(answer in 8 letters):')
if len(text)>8:
    print('Retry with correct values')
elif len(text)<8:
    print('Retry with suitable values')
else:
    print(' ',text)

# .split()
text=input('Enter the Grocery items')
print(text.split(' '))
