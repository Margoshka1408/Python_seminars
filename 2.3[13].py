# №2.3[13]. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая 
# длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь,
# занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# Затем пользователь последовательно вводит температуру для каждого дня. Температуры – целые числа и лежат в диапазоне от –50 до 50
# Необходимо вычислить длительность самой длинной оттепели

# Примеры/Тесты:
# Введите число рассматриваемых дней>? 11
# Введите среднесуточную температуру для дня 1>? 1
# Введите среднесуточную температуру для дня 2>? 7
# ...
# 1 7 3 -1 -2 1 2 3 4 5 6
# -> Максимальная дительность 6дн
# Введите число рассматриваемых дней>? 6
# Введите среднесуточную температуру для дня 1>? -1
# Введите среднесуточную температуру для дня 2>? 2
# ...
# -1 2 3 4 -1 -2
# -> Максимальная дительность 3дн

num_days = int(input('Введите количество дней: '))
if 1 <= num_days <= 100:
    current_day = 0
    length_warm = 0 # длина оттепели
    max_length_warm = 0
    while current_day < num_days: # пока текущий день меньше чем кол-во дней
        cuttent_temp = int(input('Введите температуру: ')) # считываем текущую температуру
        current_day += 1 # увеличиваем счетчик дней
        if cuttent_temp >= 0: # если текущая темп
            length_warm += 1 # увеличиваем длину серии
            if current_day == num_days and length_warm > max_length_warm:
                 max_length_warm = length_warm
        elif length_warm > max_length_warm:
            max_length_warm = length_warm
            length_warm = 0 # обнуляем текущую серию
print(max_length_warm)            
            
                