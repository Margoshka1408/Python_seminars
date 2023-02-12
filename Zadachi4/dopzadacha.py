# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что ее нет
# Прммер:
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"] ищем "qwe" ответ: 3
# - список: [] ищем "123" ответ: -1   

list = []
find_str = "123"
count = 0
for idx, value in enumerate(list):
    if value == find_str:
        count +=1
    if count == 2:
        print(idx)
        break
if count != 2:
    print(-1)