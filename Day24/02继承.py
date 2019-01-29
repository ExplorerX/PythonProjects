class Animal:
    def __init__(self, name, aggr, hp, mp):
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.mp = mp

    def recovery(self):
        self.hp += 40


class Dog(Animal):
    def bite(self, person):
        person.hp -= self.aggr
        if person.hp <= 0:
            print('%s has been bited for %s' % (person.name, self.name))

    def recovery(self):
        Animal.recovery(self)
        self.teeth = 2


class Person(Animal):
    def __init__(self, name, aggr, hp, mp, weapon):
        super().__init__(name, aggr, hp, mp)  # super找父类，只在新式类中使用，python3中所有类都是新式类。。。
        self.weapon = weapon  # 派生属性

    def hit(self, dog):
        dog.hp -= self.aggr
        if dog.hp <= 0:
            print('%s has been pitted for %s' % (dog.name, self.name))


dog1 = Dog('Tiddy', 15, 100, 100)
print(dog1.name, dog1.aggr, dog1.hp, dog1.mp)

person1 = Person('Xiaomi', 10, 100, 100, 'sticks')
print(person1.name, person1.aggr, person1.hp, person1.mp, person1.weapon)

dog1.recovery()
print(dog1.name, dog1.aggr, dog1.hp, dog1.mp)
print(dog1.teeth)
