import random, collections, csv, string, re

def gen_dict(): #generates random dict with name, surname, phone, card
    counter = 0
    names = ['John', 'Peter', 'Alfred', 'Kate', 'Lewis', 'Louise', 'Emma', 'Irvin', 'Claire', 'Roisin', 'Jenna', 'Craig', 'Liam', 'Tom', 'Thomas', 'Edwin', 'Anna', 'Natalie', 'Alina', 'Scarlett', 'Jane', 'Lewis', 'Helen', 'Barbara', 'Alfonso', 'Julia', 'Antoine', 'Johan', 'Christine', 'Francois', 'Gemma', 'Cara', 'Miranda', 'James', 'Jason', 'Ryan', 'Albert', 'Cedric', 'Harry', 'Hermione', 'Anastasia', 'Edward', 'Isabelle', 'Cherry', 'Claudia', 'Xavier']
    final_list = []
    while counter < 100:
        full_name = str(random.choice(names) +' ' + random.choice(names))
        chance = random.randint(1,50)
        symbols = ['-', ' ', '[', ']', random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase)]
        counter2 = 0
        counter3 = 0
        phone_number = ['+',]
        card_number = []
        if chance == 14:
            while counter2<11:
                phone_number.append(random.randint(0,9))
                counter2+=1
            phone_number.append(random.choice(symbols))
        else:
            while counter2<12:
                phone_number.append(random.randint(0,9))
                counter2+=1
        exp_day = str(random.randint(1,12)) + '/' + str(random.randint(1,9)) + str(random.randint(1,9))
        chance2 = random.randint (1,100)
        if chance2 == 45:
            while counter3<15:
                card_number.append(random.randint(0,9))
                counter3+=1
            card_number+=str(random.choice(symbols))
        else:
            while counter3<16:
                card_number.append(random.randint(0,9))
                counter3+=1
        counter += 1
        temp_dict ={'Name':full_name, 'Phone':phone_number, 'Exp_day':exp_day,'Card':card_number}
        final_list.append(temp_dict)
    return final_list

def card_has_errors(card_number):
    for el in card_number:
        try:
            el_int = int(el)
        except ValueError or AttributeError:
            return True
    return False

def phone_has_errors(phone):
    phone1 = phone.pop(0)
    for el in phone:
        try:
            el_int = int(el)
        except ValueError or AttributeError:
            return True
    return False