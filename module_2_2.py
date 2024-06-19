print('Введите три целых числа.')
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
print(first, second, third)
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
print()

if len({first, second, third}) == 1:
    print(3)
elif len({first, second, third}) == 2:
    print(2)
else:
    print(0)
