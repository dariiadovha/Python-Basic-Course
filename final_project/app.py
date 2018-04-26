from final_project.utils import *

compiled_list = gen_dict()

with open('cardholders_no_errors.csv', 'w', newline='')as csvfile:
    header = ['Name', 'Phone', 'Exp_day', 'Card']
    writer = csv.DictWriter(csvfile, fieldnames = header)
    writer.writeheader()

with open('cardholders_errors.csv', 'w', newline='')as csvfile:
    header = ['Name', 'Phone', 'Exp_day', 'Card']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()


for el in compiled_list:
    if card_has_errors(el.get('Card')) or phone_has_errors(el.get('Phone')) is True:
        with open('cardholders_errors.csv')as csvfile:
            writer.writerow({'Name': el.get('Name'), 'Phone': el.get('Phone'), 'Exp_day': el.get('Exp_day'),'Card': el.get('Card')})
    else:
        with open('cardholders_no_errors.csv')as csvfile:
            writer.writerow({'Name': el.get('Name'), 'Phone': el.get('Phone'), 'Exp_day': el.get('Exp_day'),'Card': el.get('Card')})



