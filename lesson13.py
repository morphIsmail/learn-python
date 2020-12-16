# Чтение / запись файла
# Чтение из файла по строкам
f = open('files/input.txt')
while True:
  line = f.readline()
  if len(line) == 0:
    break
  print(line, end='')
f.close()
# Запись в файл
f = open('files/output.txt', 'w')
f.write('New text')
f.close()