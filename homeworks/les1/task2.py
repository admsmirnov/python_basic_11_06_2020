
user_time = input('Введите время в секундах\n')
# Проверка, что введено число
if user_time.isdigit():
    user_time=int(user_time)
else:
    print('Разрешены только цифры')
# Вычисляем часы
hours = int(user_time/3600)
print(hours)
# Вычисляем минуты
minutes = int((user_time - hours * 3600)/60)
# Вычисляем секунды
seconds = user_time - hours * 3600 - minutes * 60
# Защита от
if hours > 99:
    print("Превышено максимальное значение")
else:
    f_time =f'{hours}:{minutes}:{seconds}'
    print(f_time)