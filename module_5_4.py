class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor+1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if (isinstance(other, int)):
            return self.number_of_floors == other
        else:
            return self.number_of_floors == other.number_of_floors

    def __sub__(self, other):
        if (isinstance(other, int)):
            return self.number_of_floors - other
        else:
            return self.number_of_floors - other.number_of_floors

    def __mul__(self, other):
        if (isinstance(other, int)):
            return self.number_of_floors * other
        else:
            return self.number_of_floors * other.number_of_floors

    def __truediv__(self, other):
        if (isinstance(other, int)):
            return self.number_of_floors / other
        else:
            return self.number_of_floors / other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        if (isinstance(other, int)):
            self.number_of_floors = self.number_of_floors + other
        else:
             self.number_of_floors = self.number_of_floors + other.value
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __del__(self):
        print(f'Дом в {self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
# print(House.houses_history)
del h3
print(House.houses_history)