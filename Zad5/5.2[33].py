# №5.2[33]. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите функцию, которая заменяет оценки, переданные в виде списка, но наоборот: все максимальные – на минимальные.
# Функция должна возвращать новый список оценок
# Примечание: Обратите внимание на side effects функции.
# Примеры/Тесты:
# <function_name>([1, 3, 3, 3, 4, 2, 5, 5, 2]) -> [1, 3, 3, 3, 4, 2, 1, 1, 2]
# [*] Усложненение: Если ни одна оценка не была заменена, функция должна вернуть None
# Примеры/Тесты:
# <function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None
# [**] Усложненение: Добавьте параметр в функцию, который определит как будут заменены оценки:
# Друзьям минимальные на максимальные, Врагам - наоборот.
# Примеры/Тесты:
# <function_name>(vasya_grades, "friend") -> [5, 3, 3, 3, 4, 2, 5, 5, 2]
# <function_name>(vasya_grades, "enemy") -> [1, 3, 3, 3, 4, 2, 1, 1, 2]

# def grade(lst1):
#     min_grade = min(lst1)
#     max_grade = max(lst1)
#     for i in range(len(lst1)):
#         if lst1[i] == max_grade:
#             lst1[i] = min_grade
#     return lst1       
# lst2 =  [1, 3, 3, 3, 4, 2, 5, 5, 2] 
# res = grade(lst2)
# print(res)

def grade(lst1):
    new_grades = lst1.copy()
    min_grade = min(new_grades)
    max_grade = max(new_grades)
    for i in range(len(new_grades)):
        if new_grades[i] == max_grade:
            new_grades[i] = min_grade
    return new_grades       
lst2 =  [1, 3, 3, 3, 4, 2, 5, 5, 2] 
print(lst2)
res = grade(lst2)
print(res)
print(lst2)

# [*] Усложненение: Если ни одна оценка не была заменена, функция должна вернуть None
# Примеры/Тесты:
# <function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None
def grade(lst1):
    new_grades = lst1.copy()
    min_grade = min(new_grades)
    max_grade = max(new_grades)
    if min_grade == max_grade:
            return None
    for i in range(len(new_grades)):
        if new_grades[i] == max_grade:
            new_grades[i] = min_grade
    return new_grades       
    
lst2 =  [3, 3, 3, 3, 3, 3, 3, 3, 3] 
print(lst2)
res = grade(lst2)
print(res)
print(lst2)