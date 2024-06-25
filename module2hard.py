#  Подбор двух чисел, сумме которых кратно введенное число.

str_n = input('Введите целое число >= 3: ')
if str_n.isdigit() and (int(str_n) >= 3):
    n = int(str_n)
    print('Число: ', n)

#  Не понял определение уникальности поэтому
#  сначала выводим пары, сумме которых кратно чило n

    result = []
    for i in range(1, n):
        for j in range(i, n):
            if n % (i + j) == 0:
                result.append([i, j])
    print('Пары: ', *result)

# Теперь пароль. (Отсутствуют пары i == j).

    result = []
    for i in range(1, n):
        for j in range(i+1, n):
            if (n % (i + j) == 0): #and (i != j):
                result.append(i)
                result.append(j)
    print('Пароль: ', *result, sep='')
else:
    print('Неверный ввод. Попробуйте в еще раз.')
