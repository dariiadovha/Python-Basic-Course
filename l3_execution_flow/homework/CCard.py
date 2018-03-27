#part2
card_number=input('Enter your card number: ')
if len(card_number)==16:
    pass
else:
    exit()
expiry=input('enter the expiry date in format mmyy: ')
try:
    expiry=int(expiry)
except ValueError:
    exit()
cvv = input('enter your CVV code: ')
if len(cvv)!=3:
    print('Incorrect CVV')
    exit()
else:
    print('Ha-ha-ha. Now I will use your credit card!')
#part 1
a = input ("enter some word here: ")
b = int (input('enter a number here: '))
c = float (input ('enter some float number here: '))
try:
    if b%2==0:
        print('b is even')
    else:
        print('b is uneven')
except TypeError:
    print('you should have entered a number for b')
my_list=[a, b, c]
for i in my_list:
    print(type(i))
name = input('Enter your name: ')
age = int(input('Enter your age: '))
if name and age is not None:
    print({name},{age})
else:
    print('Enter the name please')

