from random import randint

class Person:
    count = 0
    def __init__(self, c):
        self.id = Person.count # уникальный номер объекта
        Person.count += 1
        self.command = c

class Hero(Person):
    def __init__(self, c):
        Person.__init__(self, c)
        self.level = 1
    def upLevel(self):
        self.level += 1 # метод увеличения собственного уровня

class Soldier(Person):
    def __init__(self, c):
        Person.__init__(self, c)
        self.my_hero = None
    def follow(self, hero):# следовать  "иду за героем"
        self.my_hero = hero.id 

h1 = Hero(1)# по одному герою для каждой команды
h2 = Hero(2)

army1 = []
army2 = []

for i in range(20):# Использую функцию range для количества человек
    n = randint(1, 2)
    if n == 1:
        army1.append(Soldier(n))
    else:
        army2.append(Soldier(n))
#У солдат есть метод "иду за героем"
#который в качестве аргумента принимает объект типа "герой"
#У героев есть метод увеличения собственного уровня.
print(len(army1), len(army2))

if len(army1) > len(army2):
    h1.upLevel()
else:
    h2.upLevel()
#В основной ветке программы создается по одному герою для каждой команды.
#В цикле генерируются объекты-солдаты. 
#Их принадлежность команде определяется случайно
#Солдаты разных команд добавляются в разные списки
army1[0].follow(h1)
print(army1[0].id, h1.id)
#Чтобы задавать уникальный идентификационный 
#номер объекта, используется поле count, 
#принадлежащее классу Person. Часто словом "count"
#обозначают счетчик объектов. 
#так как значение этой переменной не будет уменьшаться
#при удалении объектов. Здесь count всегда только 
 #увеличивается, что позволяет задавать каждому новому
# объекту уникальный идентификатор.