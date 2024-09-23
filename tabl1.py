import math

# Варіянт 8
# Таблиця 1

a = 1.5
b = 3.5
h = 0.2

for i in range(int((b-a) / h)):
    
    # Вводимо параметр х для розрахунку
    x = i + a

    #Результат розрахунку
    f = 0

    if x < 2:
        # Косеканс
        f = math.sin(math.exp(x))**(-1) 

    elif x < 3:
        # Секанс
        f = math.cos(math.log(x))**(-1)

    else:
        f = math.sin(math.log(x))

    print("№", i+1, " = ", f)