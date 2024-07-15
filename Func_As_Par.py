from time import time_ns

'''
Задача: написать функцию, которая в качестве параметра получает другую функцию,
запускает ее и вычисляет время ее работы.

При передаче функции без параметров все работает.
При передаче функции с параметрами возникает ошибка: "Объект не может быть вызван".
'''


def tfr(fnctn):
    st = time_ns()
    fnctn()                 # Если убрать скобки, то ошибок не возникает, но fnctn не работает. return = 0.
    return time_ns() - st

#  =================================


def f1():
    for _ in range(1000):
        for _ in range(1000):
            pass


def f5(a, b):
    for _ in range(a):
        for _ in range(b):
            pass

print(f'время работы f1: {tfr(f1)} наносекунд')  # Так все работает
#print(f'время работы f5: {tfr(f5(100, 100))} наносекунд')  # Если так, то пишет, что объект не может быть вызван. В 14 строке.
