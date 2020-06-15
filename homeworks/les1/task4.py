
# Проверка, что число положительное и целое
while True:
    plz = input('Введите целое положительное число\n')
    if plz.isdigit():
        plz=int(plz)
        plz <= 0
        break
# Вычисление наибольшей цифры
prm = plz % 10
plz = plz // 10
while plz > 0:
    if plz % 10 > prm:
        prm = plz % 10
    plz = plz // 10
print(prm)


