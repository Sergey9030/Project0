def calculate_structure_sum(*data_):
    rslt = 0
    for i in data_:
        if isinstance(i, int):
            rslt += i
        elif isinstance(i, float):
            rslt += i
        elif isinstance(i, str):
            rslt += len(i)
        elif isinstance(i, dict):
            rslt += calculate_structure_sum(*i)  #  Сумма ключей
            for j in i:
                rslt += calculate_structure_sum(i[j])  # Сумма значений
        else:
            rslt += calculate_structure_sum(*i)
    return rslt

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))
