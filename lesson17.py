# Импортируем из модуля lesson15.py функцию "Сортировка выбором"
from lesson15 import selectionSort
# Импорт всех функций из модуля lesson15.py
# from lesson15 import *
# Импорт некоторых функций из модуля lesson15.py
# from lesson15 import selectionSort, findSmallest
# Просто вызываем функции по названию, например selectionSort(arr)

# Импортируем весь модуль lesson16.py (функция "Быстрая сортировка")
import lesson16
# Вызываем функцию так: lesson16.quickSort(arr)

# Бинарный поиск
def binary_search(my_list, item):
  step = 0
  low = 0
  high = len(my_list)-1
  while low <= high:
    mid = (low + high)
    quess = my_list[mid]
    if quess == item:
      print("На поиск ушло шагов: {0}".format(step))
      return mid
    if quess > item:
      high = mid-1
    else:
      low = mid+1
    step+=1
  return None
# Массив должен быть отсортирован
my_list = [2, 4, 1, 3, 7, 8, 6, 5]
print("Изначальный массив:", my_list)
# Сортировка выбором
#sortList = selectionSort(my_list)
# Быстрая сортировка
sortList = lesson16.quickSort(my_list)
print("Отсортированный массив:", sortList)

# Ищем нужный элемент
print("Индекс элемента, который мы искали:", binary_search(sortList, 5))

# Для массива из n элементов потребуется log2n шагов
# Если массив и 100 чисел то мы найдем нужное число максимум за 7 шагов
# # 100 шагов, 2**7=128, 7 шагов
# Если массив и 240 000 чисел то мы найдем нужное число максимум за 18 шагов