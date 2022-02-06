print("\x1b[4;34mВыполнил: Малову А.\x1b[0m")
base_salary = int(input("Введите Ваш оклад: "))
day_base = int(input("Введите количество рабочих дней: "))
day_worked = int(input("Введите количество отработанных дней: "))
bonus = int(input("Введите сумму всех премии и надбавок: "))
penalty = int(input("Введите сумму всех удержаний: "))
tax = float(0.13)
salary = (((base_salary / day_base) * day_worked + bonus)*((100 - tax) / 100) - penalty)
if salary <= 1000:
    print(f"\x1b[31mВаша заработная плата составляет: {salary}$. Денег нет, но вы держитесь...\x1b[0m")
else:
    print(f"\x1b[32mВаша заработная плата составляет {salary}$\x1b[0m")