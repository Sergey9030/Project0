#  Поиск простых чисел

end_of_num = int(input('Введите последнее число последовательности: '))
print(end_of_num)
numbers = []
for i in range(end_of_num): #  Формируем список numbers
    numbers.append(i+1)
primes = []
not_primes = [1]  #  Единицу не считают простым числом
for i in range(1, len(numbers)):  #  Начинаем со второго числа
    is_prime=True
    for j in range(1, i):
        if numbers[i] % numbers[j] == 0:
            is_prime = False
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print('numbers=', numbers)
print('Primes:', primes)
print('Not Primes:', not_primes)
