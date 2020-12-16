# Модули
# Импорт модуля math
import math
# Функции вызываются через имя модуля
print(math.sqrt(16))
# Импорт модуля sys
import sys
print(sys.copyright)
# Импорт всех функций модуля math
from math import *
# Функции вызываются просто по названию
print(sqrt(16))
# Импорт некоторых функций модуля math
from math import cos, log
# Функции вызываются просто по названию но доступны только импортированные
print(cos(30))