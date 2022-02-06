from itertools import count
from itertools import accumulate
from random import choice
counter = count()

class Unit:
    def __init__(self, name, team=None):
        self.id = next(counter)
        self.name = name
        self.team = team

class Hero(Unit):
    def __init__(self, name, team, level=1):
        Unit.__init__(self, name, team)
        self.level = level

    def get_level(self, team_count):
        level_list = list(accumulate(range(2, 10)))
        if team_count > level_list[0]:                          # Как этот ужос можно укоротить?
            self.level = 2
            if team_count > level_list[1]:
                self.level = 3
                if team_count > level_list[2]:
                    self.level = 4
                    if team_count > level_list[3]:
                        self.level = 5
                        if team_count > level_list[4]:
                            self.level = 6
                            if team_count > level_list[5]:
                                self.level = 7
                                if team_count > level_list[6]:
                                    self.level = 8

class Soldier(Unit):
    def follow_hero(self, name_hero, id_hero):
        print(f"Герой {name_hero}(ID: {id_hero}) взял в свои ряды бойца {self.name}(ID: {self.id})")

def main():
    # Создаем героев
    h_rad = Hero('Sinon_1501', 'Rayana_16')
    h_dire = Hero('Fatina', 'Adinai')

    # Создаем солдат и распределяем их по командам.
    teams = [1, 2]          # Рандомайзер команд для солдат.
    soldiers_name = ['Rayana', 'Fatima', 'Albina', 'Aidana', 'Kamila', 'Aiturgan', 'Baku',
                     'Aliya', 'Karina', 'Samira', 'Dareia', 'Ice', 'Ramina', 'Malika', 'Sinon']
    radiant = []       # Списки
    dire = []          # солдат
    max_soldiers = int(input("Введите сколько всего будет солдат: "))
    for i in range(max_soldiers):
        team_flag = choice(teams)
        if team_flag == 1:
            random_name = choice(soldiers_name)
            i = Soldier(random_name, 'Radiant')      # Создание солдат класса Soldier, присвоение имени и команды.
            radiant.append(i)
        elif team_flag == 2:
            random_name = choice(soldiers_name)
            i = Soldier(random_name, 'Dire')
            dire.append(i)
    h_rad.get_level(len(radiant))
    h_dire.get_level(len(dire))

    # Вывод состава команд и героев.
    print(f"\nСостав команды Radiant:\nГерой: {h_rad.name} ({h_rad.level} LVL). Количество солдат: {len(radiant)}.\n"
          f"Солдаты Radiant: {[p.name for p in radiant]}\n"
          f"\nСостав команды Dire:\nГерой: {h_dire.name} ({h_dire.level} LVL). Количество солдат: {len(dire)}.\n"
          f"Солдаты Dire: {[p.name for p in dire]}\n")

    # Выполняем условие следования рандомного солдата за героем.
    random_dire_soldier = choice(dire)
    random_dire_soldier.follow_hero(h_dire.name, h_dire.id)

main()