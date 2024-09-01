class Animal:
    alive = True              # alive - живой
    fed = False               # fed - сытый

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:                      # если еда съедобная
            print(f'{self.name} съел {food.name}')
            self.fed = True                  # животное накормленное
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False               # животное погибнет


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant:

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    edible = False            # съедобный - ложь


class Fruit(Plant):
    edible = True              # съедобный - правда


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик-семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
