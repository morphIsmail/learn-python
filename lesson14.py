# Квадратное уравнение
def quad(a,b,c):
  if a==0:
    return "Ошибка a = 0"
  D = b**2 - 4*a*c
  print("Дискриминант =", D)
  if D>0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    return "x1={0}, x2={1}".format(x1, x2)
  elif D == 0:
    x = -b / (2*a)
    return "x={0}".format(x)
  else:
    return "Нет корней"

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

print(quad(a,b,c))

# 1 -5 9 Корней нет
# 1 -4 4 Корень 2
# 1 3 -4 Корни -4 1