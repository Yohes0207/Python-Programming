print('Check you Loan Eligibility')
age = input('Enter your age,')
bank = input('Do you have a bank account,')
work = input('Are you working,')
cibil = input('Enter your CIBIL Score,')
if int(age) <= 18 and bank == 'no' or work == 'no' and int(cibil) <= 700:
    print('You are not Eligibile')
else:
    print('You are Eligibile')
    
