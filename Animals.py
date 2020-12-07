class Animals:
    weight=''
    size=''
    color=''
    feeds=''
    def __init__(self, w,s,c,f):
        self.weight=w
        self.size=s
        self.color=c
        self.feeds=f
 
class Birds(Animals):
    wings=''
    feathers=''
    def get_bird(self,wings,feathers):
        self.wings=wings
        self.feathers=feathers
    def show_bird(self):
        print(self.wings,self.feathers)

class Fishes(Animals):
    fins=''
    scales=''
    def get_fish(self,fins,scales):
        self.fins=fins
        self.scales=scales
    def show_fish(self):
        print(self.fins,self.scales,self.color)
 
Penguin=Birds('10 kg','королевский','белый','ананасы/люди')
Penguin.get_bird('несгибающиеся','как чещуя')
Penguin.show_bird()

Canary=Birds("300g", "Маленькая" ,"желтый", "семочки/Овес")
Canary.get_bird("Serinus", "Домашняя")
Canary.show_bird()

Plotva=Fishes("500g", "Средняя", "черно-желтая", "Черви")
Plotva.get_fish("семейства карповых", "Rutilus")
Plotva.show_fish()

Forel=Fishes("2kg", "Средняя", "Красная", "Опарыш")
Forel.get_fish("семейство лососевых", "Радужная")
Forel.show_fish()