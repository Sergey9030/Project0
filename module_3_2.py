def if_address(find_in='university.help@gmail.com', *, find_=['.com', '.ru', '.net']):
    #  проверяет, являеся ли find_in адресом

    if not ('@' in find_in):
        return False
    for i in range(len(find_)):
        if find_in[-1*len(find_[i]):] == find_[i]:
            return True
    return False


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if not (if_address(recipient) and if_address((sender))):
        return 'Невозможно отправить письмо с адреса <' + sender + '> на адрес <'+  recipient + '>'
    elif recipient == sender:
        return 'Нельзя отправить письмо самому себе!'
    elif sender == 'university.help@gmail.com':
        return 'Письмо успешно отправлено с адреса <'+ sender + '> на адрес <' + recipient + '>.'
    else:
        return 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <' + sender + '> на адрес <' + recipient + '>.'

print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))