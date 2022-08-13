# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import os

path = os.path.join('PythonHW04', 'ex03', 'fileinput.txt')
with open(path, 'r') as f:
    text = f.readline()

# метод для конвертации в инт из строку


def convert_to_int(str):
    return [int(x) for x in str.split()]


int_list = convert_to_int(text)
print(int_list)


newArr = []
for el in int_list:
    if int_list.count(el) == 1:
        newArr.append(el)
print(f'неповторяющиеся элементы: {newArr}')

print("*" * 10, "использование lambda+filter (поиск неповторяющиеся элементы):", "*" * 10)
my_list=list(filter(lambda x:int_list.count(x)==1,int_list))
print(my_list)