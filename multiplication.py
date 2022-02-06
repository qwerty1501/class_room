import random
s = 0
for i in range(10):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    c = input(f"Введите сколько будет {a} * {b} = ")
    d = a * b
    if d == int(c):
        s += 1
print(f"Ваш результат {s*10}%.")
