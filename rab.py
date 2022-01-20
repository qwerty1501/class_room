#12
x = input('Пожалуйста, введите предложение: ')
y = input('Пожалуйста, введите номер: ')
y = int(y)
g = list(x)
j = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
limit = 25
for e in g:
    q = j.index(e)
    if (q+y) > 25:   
        oman = (q+y) % 26
        newg = j[oman]
        print(newg, end="")
    elif (q+y) <= 25:
        newg = j[q+y]
        print(newg, end="")



#13
def divide(array):
    positive = []
    negative = []
    for i in array:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
    return positive, negative
 
 
arr = [1, 2, 3, -1, -2, -3]
pos, neg = divide(arr)
print(pos)
print(neg)



#14
def season(num):
   if num == 12 or 1 <= num <= 2:
       print("Зима")
   elif  3 <= num <= 5:
       print("Весна")
   elif 6 <= num <= 8:
       print("Лето")
   elif 9 <= num <= 11:
       print("Осень")
   else:
       print("Неверно введён номер месяца!")
n = int(input("Введите номер месяца (1-12): "))
season(n)


#15
n = int(input())
m = int(input())
y = int(input())

def bank(n, m, y):
        nal = n
        year = y
        def money():
            if year >0:
                nal = n * 1.1 + m
                year = year -1
                return money()
            else:
                return nal

print(nal)



#16
a = 0
days = -1
summ = 0
while a > -300:
   summ += a
   days += 1
   a = float(input('Температуру воздуха '))
print(summ / days)


while True:
    symbol = int(input())
    if symbol == 0:
        break
    print(chr(symbol)) 