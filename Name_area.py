# Отсутствие результата тоже результат.
def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()  # Не вызывается  потому, что не вызвана функция test_function().
inner_function()  # Вызывает ошибку  потому, что Name_area не видит inner_function().