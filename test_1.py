# Чтение из файла.
# Создайте файл с текстом The Zen of Python.
# Напишите функцию, которая считайте его и возвратит список из слов, которые начинаются на букву “c” или “C”.
# Подсказка: используйте метод строчных значений, который проверяет, начинается ли слово на переданную букву.
a = []
with open("/Users/sinon_16/Desktop/tex.txt", 'r') as txt:
    text = txt.split()
    text = text.split('\n')
    for i in text:
        if i.title() == 'c' or i.title() == 'C':
            a.append(i)

print(a)