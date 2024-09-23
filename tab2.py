import math

# Варіянт 8
# Таблиця 2

a = -1
b = -0.9
h = 0.01
d = 0.001

for i in range(int((b - a) / h)):

    # Параметр розрахунку
    x = i + a

    k = 2
    S = 0 # Сума ряду
    n = ((-1)**k)*math.cos(k*x) / (k**2 - 1) # Черговий член ряду

    while abs(n) > d:

        n = ((-1)**k)*math.cos(k*x) / (k**2 - 1)
        S += n
        k += 1

    print(x*h,":", S)