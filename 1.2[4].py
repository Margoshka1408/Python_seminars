# 1.2[4]. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?
# Примеры/Тесты:
# 6 >>>  1  4  1
# 24 >>> 4  16  4
# 60 >>> 10  40  10

s = int(input('Введите количество журавликов: '))
a = s // 6 
c = a 
b = (a + c) * 2
print(f'Петя сделал {a} журавликов, Катя сделала {b} журавликов, Сережа сделал {c} журавликов')