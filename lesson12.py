# Классы
# Все поля public а методы virtual
class People:
  def say(self):
    print('Hello')
People().say()
# Конструктор
class Man:
  __age = 25 # privat поле
  def __init__(self, name):
    self.name = name
  def sayName(self):
    print("Меня зовут: {0}, Возраст: {1}".format(self.name, self.__age))
Man("Ivan").sayName()