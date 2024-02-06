# Операторы сравнения
print("5 > 2 -", 5 > 2)
print("5 >= 2 -", 5 >= 2)
print("5 < 2 -", 5 < 2)
print("5 <= 5 -", 5 <= 5)
print("5 == 2 -", 5 == 2)
print("5 != 2 -", 5 != 2)
# True False на Python пишутся с заглавной буквы
# Логическое Отриациние
print("not True -", not True)
print("not False -", not False)
# Логическое И
print("True and True -", True and True)
print("True and False -", True and False)
print("False and True -", False and True)
print("False and False -", False and False)
# Логическое ИЛИ
print("True or True -", True or True)
print("True or False -", True or False)
print("False or True -", False or True)
print("False or False -", False or False)
# Условные конструкции
a=2
if a < 3:
  # Обязательно ставится табуляция
  print("a < 3")
elif a >= 5:
  print("a >= 5")
else:
  print("3 < a < 5")
# switch в Python отсутствует
# можно не ставить новую строку и таб если всего одна строка
if a < 10: print("a < 10")
