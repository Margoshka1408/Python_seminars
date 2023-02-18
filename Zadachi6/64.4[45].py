# №64.4[45] Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, — их сумма равна 284.
# 284: 1, 2, 4, 71 и 142, — их сумма равна 220.
# Первые пары дружественных чисел:
# 220, 284; 1184, 1210; 2620, 2924; 5020, 5564; 6232, 6368
# Для заданного числа number выведите все пары дружественных чисел, каждое из которых не превосходит number.
# Напишите функцию:
# Аргументы: целое число
# Печатает все пары дружественных чисел, не превосходящих аргумент.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Примечание:
# 1. Выделите значимые куски алгоритма и оформите их в виде функций
# 2. Задокументируйте созданные функции
# 3. Используйте type hinting
# Примеры/Тесты:
# <function_name>(300)
# 220 284
# <function_name>(10000)
# 220 284
# 1184 1210
# 2620 2924
# 5020 5564
# 6232 6368

def sum_divisor(a: int) -> int:
    """
    """
    sum_a = 0
    for i in range(1, a):
        if a % i == 0:
            sum_a += i
    return sum_a

def para_numbers(n: int) -> None:
    
    for i in range(1, n):
        sum_1 = sum_divisor(i)
        sum_2 = sum_divisor(sum_1)
        
        if i == sum_2 and i < sum_1:
            print(i, sum_1)

para_numbers(10000)

# вариант решения 2
# def no_remain_divisor(number: int, islistcontent: bool = False):
#     """
#     Return sum of no_remain_divisor for number and optionally list of such divisor
#     :param number: number for that require divisors
#     :param islistcontent: flag for return full list of divisors
#     :return: sum of divisors and optionally list of them
#     """
#     lst_div = []
#     for divisor in range((number - 1) // 2 + 1, 0, -1):
#         if number % divisor == 0:
#             lst_div.append(divisor)
#     if islistcontent: return lst_div, sum(lst_div)
#     return sum(lst_div)


# def friends_number(max_num: int)-> None:
#     set_friends = set()
#     for n in range(1, max_num):
#         divisor1 = no_remain_divisor(n)
#         divisor2 = no_remain_divisor(divisor1)
#         if divisor1 <= max_num and divisor2 <= max_num and n == divisor2 and n != divisor1 and n not in set_friends:
#             set_friends.add(n)
#             set_friends.add(divisor1)
#             print(n, divisor1)


# friends_number(10000)
