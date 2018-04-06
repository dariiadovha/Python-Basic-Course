low_digit_limit=1
upper_digit_limit=100
correct=34
answers=[]
a=''
while a!=correct:
    a = input('Enter the answer: \n')
    try:
        a = int(a)
        if a<1:
            print(f'Your input value {a}is less than 1')
        elif a>100:
            print(f'Your input value {a} is more than 100')
        answers.append(a)
    except ValueError:
        answers.append(a)
print(answers)
new_list=[i for i in answers if type(i)==str]
print(new_list)