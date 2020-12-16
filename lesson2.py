# Строки
# Это комментарий, он не отображается при запуске
# Комментарии в VS Code можно добавить с помощью ctrl+/
a = "Строка в двойных кавычках"
print(a)

b = 'Такая же строка, но в одичночных кавычках'
print(b)

str = "Чтобы писать в несокльких \
строках используется \\, но результат выводится в одной строке"
print(str)

c = '''В тройных кавычках можно писать
на нескольких
разных строках.'''
print(c)

d = """Тоже самое но в двойных кавычках,
которых по три штуки."""
print(d)

e = "Если надо вывести 'что-то в одиночных кавычках'"
print(e)

f = 'Если надо вывести "что-то в двойных кавычках"'
print(f)

g = "Или просто \"экранировать двойные кавычки\""
print(g)

h = 'Или просто \'экранировать одиночные кавычки\''
print(h)

i = 'Строка\nс переносом'
print(i)

j = r'Строка в которой не работает \n или \\'
print(j)

print('Форматный вывод: {0} - {1}'.format("ITD", "Уроки"))

# в конце строки ; не нужна
# но если писать в одной строке то нужна
# у переменных тип данных не указывается так как в python испольуется динамическая типизация
i=5; print(i)

# блоки кода отделяются табуляциями