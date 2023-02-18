# №6.2[41] Дан список, целых чисел.
# Напишите функцию, которая определит те элементы списка, у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Функция
# Аргументы: список целых чисел
# Возвращает: список элементов (смотри условие)
# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 5]) -> [5]
# <function_name>([1, 5, 1, 6, 1]) -> [5,6]
# <function_name>([7, 5, 1, 6, 8]) -> [8]
# <function_name>([8, 1, 5, 4, 5]) -> [8,5]

def check_neigh(lst):
    rez = []
    for idx, el in enumerate(lst):
        prev_id = idx - 1
        next_id = idx + 1 if idx != len(lst) - 1 else 0
        if el > lst[prev_id] and el > lst[next_id]:
            rez.append(el)
    return rez


print(check_neigh([1, 3, 3, 3, 5]))
print(check_neigh([1, 5, 1, 6, 1]))
print(check_neigh([7, 5, 1, 6, 8]))
print(check_neigh([8, 1, 5, 4, 5]))