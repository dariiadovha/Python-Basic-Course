name = input('Enter your name: ')
age = input('Enter your age: ')
email = f'{name}.{age}@itea.ua'
try:
    name/'good'
    surname = 'Noob'
except TypeError:
    surname = 'Ivanov'
if surname == 'Noob':
    print('Ti dopustil oshibku')
else:
    print('Molodec')
print('\nDeveloping with Python...\n')
print(email)
