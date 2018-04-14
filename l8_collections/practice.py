import collections,csv,random
def gen_mail(firm_list, max_number):
    firm_list1 = list(firm_list)
    mails = []
    counter = 0
    while counter<50:
        for firm in firm_list1:
            random_firm =firm_list[random.randint(0,len(firm_list1)-1)]
            mails.append (str(random_firm)+str(random.randint(1, max_number+1))+'@'+str(random_firm)+'.com')
            counter+=1
    return mails

tp=('micro','tesla','acura')

last_year_list = gen_mail(tp,11)
current_year_list = gen_mail(tp,30)
print(last_year_list,current_year_list)

unique_last_year=set(last_year_list)
unique_current_year=set(current_year_list)
recurring_guests= unique_last_year.intersection(unique_current_year)
print(recurring_guests)


recurring_guests_dict = {}
for email in recurring_guests:
    value = (email.split('@'))[0]
    recurring_guests_dict[email] = value
print(recurring_guests_dict)

with open('emails.csv', 'w', newline='') as csvfile:
    header = ['e-mail', 'name']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for key,value in recurring_guests_dict.items():
        writer.writerow({'e-mail':key,'name':value})


