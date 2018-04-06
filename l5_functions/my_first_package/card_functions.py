def card_has_errors(card_number):
    while True:
        card_number = input('Enter the card number like follows "1234 5678 9870 5432" : \n')
        # checking card number and card type
        try:
            if len(card_number) != 19:
                print('Ooops there is an error. Please try to enter the card number one more time')
                return True
            card_number = card_number.split(' ')  # splits the number into list of values
            card_number1 = []
            if len(card_number)==4:
                for i in card_number:  # checks the length of each card number element
                    if len(i) == 4:
                        card_number1.append(int(i))
                return card_number1 or False
        except ValueError or AttributeError: # the above checks failed
            print('Ooops there is an error. Please try to enter the card number one more time')
            return True
def print_bank(card_number_list):
    try:
        first = int(card_number_list.pop(0))  # takes first 4 numbers
        if first == 5167:  # checks the card type
            print('You use PrivatBank credit card')
        elif first == 5375:
           print('You use MonoBank credit card')
        else:
            print('You use credit card from the unknown bank')
    except ValueError or AttributeError:  # the above checks failed
        print('Ooops there is an error. Please try to enter the card number one more time')
        return True

def expiry_check(expiry):
    while True:
        expiry = input('Enter the expiry date in the format mm/yy: \n')
        expiry1 = expiry.split('/') #splits the expiry into 2 values
        try:
            month = int(expiry1.pop(0))
            year = int(expiry1.pop(0))
            if month in range(1, 13) and year > 18:
                return expiry1 or False
                break
            else:
                print('Use a valid card please')
                return True
        except TypeError or ValueError:
            print('Enter the numbers please in the correct format')
            return True
def cvv_check(cvv):
    while True:
        cvv = input('Enter the CVV code: \n')
        if len(cvv) == 3:
            try:
                cvv = int(cvv)
                return cvv or False
                break
            except ValueError:
                print('Enter 3 numbers please')
                return True
        else:
            print('Enter 3 numbers please')
            return True

def region_check(card_number_list):
    import os
    if len(card_number_list) != 3 and str(card_number_list)!=16:
        region = os.environ.get('CARD TYPE','Europe' )
    else:
        region = os.environ.get('CARD TYPE','China')
    print(region)
    return region

