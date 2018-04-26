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
        phone_number = '+'
        card_number = ''
        while counter2<11:
                phone_number += str(random.randint(0,9))
                if chance == 14:
                    phone_number += str(random.choice(symbols))
                counter2+=1
        exp_day = str(random.randint(1,12)) + '/' + str(random.randint(1,9)) + str(random.randint(1,9))
        chance2 = random.randint (1,100)
        while counter3<15:
                card_number += str(random.randint(0,9))
                if chance2 == 45:
                    card_number+=str(random.choice(symbols))
                counter3+=1
        counter += 1
        temp_dict ={'Name':full_name, 'Phone':phone_number, 'Exp_day':exp_day,'Card':card_number}
        final_list.append(temp_dict)
    return final_list

def card_has_errors(card_number):
    card_valid = re.match(r'(^[0-9]{16}$)', card_number)
    if card_valid:
        return False
    else:
        return True

def phone_has_errors(phone):
    phone_valid = re.match(r'(^'+',[0-9]{11}$)', phone)
    if phone_valid:
        return False
    else:
        return True

