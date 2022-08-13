#Задайте список из нескольких чисел. Напишите программу, которая найдёт
#сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# функция для создания и печати списка
def listZeroPlusN(resultArr=[]):
    n = int(input(
        'Введите положительное число N, для отображения всего промежутка 0 до N: '))
    # resultArr = []
    startValue = 0
    for i in range(0, n+1):
        resultArr.append(startValue)
        startValue += 1
        # print(sum)
    print(resultArr)
    return(resultArr)


Arr = []
listZeroPlusN(Arr)

print("*" * 10, "использование включения list comprehension (формирование массива из нечетных позиций входного массива):", "*" * 10)
my_list = [i for i in range(len(Arr)) if i%2!=0]
print(my_list)






# функция для суммы нечётных элементов списка

def listSumOddElements(inputArray=[]):
    answer = 0
    for i in range(len(inputArray)):
        if i%2!=0:
            answer = inputArray[i]+answer
            #print(answer)
    i+=1
   #print(answer)
    return(answer)
    #print(inputArray[i])
    
sum1=int(listSumOddElements(Arr))

print(f'сумма элементов с нечётных позиций: {sum1}')



