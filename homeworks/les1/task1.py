# Переменные и их вывод
age_a = 11
age_b = 22
age_c = 33
print(age_a)
print(age_b)
print(age_c)
# Вывод переменных в одну строку
print(age_a, age_b, age_c)
# Запрос и вывод чисел и строк
region_code = input('Введите код Вашего региона\n')

if region_code.isdigit():
    region_code=int(region_code)
    print('Ваш регион - ',region_code)
else:
    print('Код региона содержит только цфиры')

city = input('Введите название Вашего города\n')
print('Ваш город - ', city)

