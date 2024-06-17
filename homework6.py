# Словари
my_dict={'serg':1980, 'masha':1983, 'den':1999}
print('Словарь:', my_dict, type(my_dict))
print('Существующее значение "serg":', my_dict['serg'], type(my_dict['serg']))
print('Существующее значение "masha":', my_dict.get('masha'))
print('Не существующее значение "klim:"', my_dict.get('klim', 'Отсутствует в словаре'))
my_dict['klim'] = 2000
my_dict.update({'tom': 2022})
print('Удаляемое значение "den:"', my_dict.pop('den'))
print('Измененный словарь:', my_dict)
print()

# Множества
my_set = {1, 1, 'Str', 'Str', 1.2, 1.2, (1, 2), (1,2)}
print('Множество:', my_set, type(my_set))
my_set.update({5, 'len', 3.4})
print('Измененное множество:', my_set)