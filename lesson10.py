# Функции
def helloWorld():
  print("Hello, World!")
helloWorld()
helloWorld()

# Функция с параметрами
def printMax(a,b):
  if a>b:
    print(a, 'больше', b)
  elif a==b:
    print(a, 'равно', b)
  else:
    print(a, 'меньше', b)
printMax(7,9)
printMax(7,5)
printMax(7,7)

# Функция с параметрами по умолчанию
# def sayHello(name="Ivan", age) так не правильно
def people(age, name="Ivan"):
  print("Имя: {1}, Возраст: {0}".format(age, name))
people(25, "Evgen")
people(18)

# Возврат значения из функции и передача нескольких параметров в виде массива
def total(*numbers):
  total = numbers[0]
  for n in numbers:
    if n > total:
      total = n
  return total
print("Максимальный из аргументов:", total(5,4,1,0,9,17,3,2,15,4,2))

# Возврат нескольких значений в виде кортежа
def get_two_param():
  return (2, "Text Param")
print(get_two_param())

# exec и eval
exec('print("Выполняется код из строки")')
print('Вычисляется выражение из строки (2+5)*2: ', eval('(2+5)*2'))