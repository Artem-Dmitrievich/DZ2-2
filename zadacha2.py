# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

n = int(input('input N: '))
factorial = 1
for i in range(1, n+1):
     factorial *= i # *= умножение и присвание https://pythonru.com/osnovy/operatory-python
     print(factorial, end=' ')