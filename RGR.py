"""Первый подходящий с упорядочиванием (FFD)"""

"""Факторы:
1. Размерность(число предметов)
2. Доля средних
3. Вместимость контейнера
4. Длина интервала"""

import random


N = [100, 200, 500, 1000, 10000] #кол-во предметов
capacities = [100, 200, 300, 500, 1000]  #объем контейнеров
means = [25, 50, 75, 100, 150] #мат ожидания
vars = [15,20, 25, 33, 40] #дисперсии

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



def calc(capacity, n, var, mean):
    std = int(var ** 0.5)
    weights = [random.normalvariate(mean, std) for _ in range(n)]
    weights.sort(reverse=True)
    result = first_sort_fit(capacity, weights)

    return result



count = 1
for n in N:
    for c in capacities:
        for var in vars:
            for mean in means:
                print(f"\nЭксперимент №{count}")
                result = calc(c, n, var, mean)
                str = (f"X1 Количество предметов: {n}\n"
                       f"X2 Средний вес предмета: {mean}\n"
                       f"X3 Дисперсия: {var}\n"
                       f"X4 Объем контейнера: {c}\n"
                       f"Итоговое количество контейнеров:{len(result)}\n")
                print(str)
                count+=1

