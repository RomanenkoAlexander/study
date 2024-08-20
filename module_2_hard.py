import random
first_number = random.randint(3, 20)
passwords = []
pass_ = []
for i in range(1, first_number):
    for j in range(i+1, first_number):
        #print('Первое число', first_number, 'i= ', i, 'j= ', j)
        if first_number % (i + j) == 0 and i != j:
            pass_ = ([i, j])
            passwords.append(pass_)
print('Число первого поля', first_number)
print('Пары чисел', passwords)