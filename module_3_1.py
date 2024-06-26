calls = 0
def count_calls():
    global calls
    calls += 1
    return

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    flg = False
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            flg = True
    return flg

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)
print('--------------------------')

# Попробуем реализовать поинтереснее
def is_contains2(string, list_to_search, ind):
    #  Проверяет равенство string и list_to_search[ind] и возвращает True или False
    global calls
    calls +=1
    if ind >= len(list_to_search):
        return False
    elif string.lower() == list_to_search[ind].lower():
        return True
    else:
        return is_contains2(string, list_to_search, ind+1)  # Рекурсия однако

str1 = 'Urban'
lts1 = ['ban', 'BaNaN', 'urBAN']
calls = 0
print([str1], 'in', lts1, '=', is_contains2(str1, lts1, 0))
print('count of calls =', calls)
