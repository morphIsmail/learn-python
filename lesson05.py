# Цикл while
i=0
while i <= 20:
  print(i)
  i+=2
else:
  print("Цикл завершился")
print("Этот код уже за пределами цикла")

# Цикл for
for i in range(1,5):
  print(i)
# else не обязателен в циклах
else:
  print("Конец цикла for")
print("За пределами цикла for")
# Можно указать шаг для цикла for
for i in range(0,10,2):
  # Шаг цикла = 2
  print(i)

# break и continue
for i in range(0,10):
  if i==4:
    continue
  if i>=7:
    break
  print(i)
