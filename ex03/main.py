# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

import os
path1 = os.path.join('PythonHW05', 'ex04', 'input1.txt')
with open(path1, 'r') as my_file:
    data1 = my_file.readline()
data1 = data1.split()
# print(data1)
res = ' '.join(data1)
print(f'прочитано из файла:\n{res}')

myListValue = []
myListCount = []
count = 1
for i in range(len(res)):
    # print(i)
    if i < len(res)-1:
        if res[i] == res[i+1]:
            count += 1
        else:
            # print(count, res[i])
            myListValue.append(count)
            myListCount.append(res[i])
            count = 1

            
myListValue.append(count)
myListCount.append(res[i])

# print(myListValue)
# print(myListCount)
print(f'полученный массив с парами элементов:')
print("*" * 10, "использование zip (формирую кортеж для дальнейшей расшифроки):", "*" * 10)
my_list = list(zip(myListValue, myListCount))
print(my_list)
print("*" * 10, "расшифровка:", "*" * 10)


result = ''
for item in my_list:
    result += item[0] * item[1]
print(result)


print("*" * 10, "использование map (применяю ко всему кортежу):", "*" * 10)
def f(x):return(x[0]*x[1])

res = tuple(map(f, my_list))
res = ''.join(res)
print(res)



repack = []
j = 0
for i in myListValue:
    if i > 0:
        repack.append(myListCount[j]*i)
        i -= 1
        j += 1



# print(repack)

repack = ''.join(repack)

print(repack)
