#creating the card type checker
card_number = ''
while True:
    card_number = input('Enter the card number like follows "1234 5678 9870 5432" : \n')
    #checking card number and card type
    if len(card_number) != 19:
        print('Ooops there is an error. Please try to enter the card number one more time')
    else:
        card_number = card_number.split(' ') #splits the number into list of values
        card_number1 = []
        for i in card_number: #checks the length of each card number element
            if len(i) != 4:
                print('Ooops there is an error. Please try to enter the card number one more time')
        try:
            for i in card_number: #integers card number into the new list
                card_number1.append(int(i))  # checks if the card number is entered in the defined format
            first = int(card_number1.pop(0))  # takes first 4 numbers
            if first == 5167: #checks the card type
                print('You use PrivatBank credit card')
            elif first == 5375:
                print('You use MonoBank credit card')
            else:
                print('You use credit card from the unknown bank')
            break
        except ValueError or AttributeError: #the above checks failed
            print('Ooops there is an error. Please try to enter the card number one more time')
#checking expiry
expiry = ''
while True:
    expiry = input('Enter the expiry date in the format mm/yy: \n')
    expiry1 = expiry.split('/')
    try:
        month = int(expiry1.pop(0))
        year = int(expiry1.pop(0))
        if month in range(1,13) and year > 18:
            break
        else:
            print('Use a valid card please')
    except TypeError or ValueError:
        print('Enter the numbers please in the correct format')
#checking cvv
cvv = ''
while True:
    cvv = input('Enter the CVV code: \n')
    if len(cvv) == 3:
        try:
            cvv = int(cvv)
            break
        except ValueError:
            print('Enter 3 numbers please')
    else:
        print('Enter 3 numbers please')
#try2





