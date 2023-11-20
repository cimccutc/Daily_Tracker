def asking_for_expense(value):
    expense = int(input(f'What is your expense on {value} '))
    return expense

expense_list = ['Gas', 'Food', 'Penny Stuff', 'Others']
total = 0

for item in expense_list:
    total = total + asking_for_expense(item)

print('Look like your total price is', total, '$')


print('Your net value for the day is:',(int(input('How many hours did you work? '))*38) -  total, '$')