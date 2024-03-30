"""Первый подходящий с упорядочиванием (FFD)"""

"""Факторы:
1. Размерность(число предметов)
2. Мат ожидание 
3. Вместимость контейнера
4. Длина интервалов"""

import random


N = [100, 200, 500, 1000, 10000] #кол-во предметов
capacities = [35, 55, 80, 100, 150]  #объем контейнеров
means = [25, 50, 75, 100, 150] #мат ожидания
intervals_length = [15,20, 25, 33, 40] #длина интервала

def first_sort_fit(capacity, weights):
    containers = [0] #список контейнеров. Один контейнер будет хранить сумму весов предметов, положенных в него

    for w in weights:
        for i in range(len(containers)): #проходимся по всем непустыи контейнерам
            if containers[i] + w <= capacity:
                containers[i] += w #нашли первый попавшийся контейнер
                break
        else:
            containers.append(w)#если среди непустых контейнеров не оказалось места, то кладем предмет в новый контейнер

    return containers



def calc(capacity, n, length , mean):
    std = (length / 2) ** 0.5#стандартное отклонение
    weights = [random.normalvariate(mean, std) for _ in range(n)]
    weights.sort(reverse=True)
    result = first_sort_fit(capacity, weights)

    return result


for n in N:
    for c in capacities:
        for length in intervals_length:
            for mean in means:
                result = calc(c, n, length, mean)
                str = (f"X1 Размерность (количество предметов): {n}\n"
                       f"X2 Мат. ожидание: {mean}\n"
                       f"X3 Вместимость контейнера: {c}\n"
                       f"X4 Длина интервала: {length}\n"
                       f"Итоговое количество контейнеров:{len(result)}\n")
                print(str)

