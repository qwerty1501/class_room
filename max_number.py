number = input("Введите число: ")
b = 0
for i in number:
    if int(b) < int(i):
        b = i
print(b)