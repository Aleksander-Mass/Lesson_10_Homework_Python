'''
#    Погружение в Python (семинары)
##   Урок 10. ООП. Начало

###  Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.

###  Задание №6
*Доработайте задачу 5*.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.

'''

__all__ = [
    'Animal',
]

from enum import Enum


class AnimalType(Enum):
    FISH = 0,
    BIRD = 1,
    CAT = 2


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Fish(Animal):
    def __init__(self, color, *args):
        self.color = color
        super().__init__(*args)

    def get_color(self):
        return self.color

    def __str__(self):
        return f'Рыба.\nИмя {self.name}\nВозраст {self.age} лет/год\nЦвет: {self.color}'


class Bird(Animal):
    def __init__(self, is_flies, *args):
        self.is_flies = is_flies
        super().__init__(*args)

    def is_flies(self):
        return self.is_flies

    def __str__(self):
        type = 'летает' if self.is_flies else 'ходит'
        return f'Птица.\nИмя {self.name}\nВозраст {self.age} лет/год\n{type}'


class Cat(Animal):
    def __init__(self, hair_length, *args):
        self.hair_length = hair_length
        super().__init__(*args)

    def get_height(self):
        if self.hair_length < 0.01:
            return 'Лысый'
        if self.hair_length < 1:
            return 'Короткошерстный'
        return 'Пушистый'

    def __str__(self):
        return f'Кот.\nИмя {self.name}\nВозраст {self.age} лет/год\n{self.get_height()}'


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: AnimalType, *args):
        factory_dict = {
            AnimalType.FISH: Fish,
            AnimalType.BIRD: Bird,
            AnimalType.CAT: Cat
        }
        return factory_dict[animal_type](*args)


if __name__ == '__main__':
    cat = AnimalFactory.create_animal(AnimalType.CAT, 50, 'Пушок', 1)
    print(cat)

    bird = AnimalFactory.create_animal(AnimalType.BIRD, True, 'Каркуша', 3)
    print(bird)
    print(bird.is_flies)