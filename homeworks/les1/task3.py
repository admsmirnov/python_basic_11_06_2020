
# Ввод данных пользователя и их проверка
digit = input('Введите любое число\n')
if digit.isdigit():
    digit = int(digit)
    result = f'{digit} + {digit}{digit} + {digit}{digit}{digit}'
    print(result)
else:
    print('Неверный ввод! Вводите только число!')


