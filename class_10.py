# Несколько дней подряд метеоролог измеряет температуру воздуха в своём городе. 
# Ваша программа считывает измеренные им значения и выводит среднее значение температуры за время измерений. 
# Чтобы обозначить конец ввода данных, вводится значение, меньшее -300 (реальная температура не может быть ниже -273.15).
# При проведении вычислений с действительными числами ответ может незначительно отличаться от математически правильного из-за погрешностей округления;
#  это не повлияет на проверку решения.

a = 0
days = -1
summ = 0
while a > -300:
   summ += a
   days += 1
   a = float(input())
print(summ / days)