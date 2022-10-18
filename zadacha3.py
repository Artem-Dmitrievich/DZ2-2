# Реализуйте случайное перемешивание списка.
# Пример:
# Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True ']
# Результат -> [250, 3.14, 'True ', 'Веселый пианист']
import random


list = ['Веселый пианист', 250, 3.14, 'True ']
print(list)
random.shuffle(list) #shuffle функция перемешивания модуля рандом
# https://docs-python.ru/standart-library/modul-random-python/funktsija-random-shuffle/
print('->', list)