'''
Создать не менее двух дескрипторов для атрибутов классов,
которые вы создали ранее в ДЗ
'''


class NoNegative:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Значение не может быть отрицательным")
        else:
            instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    _depth_sm = 5
    _weight_kg_sm = 25
    length = NoNegative()
    width = NoNegative()

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_weight(self):
        return (self.length * self.width * \
                self._depth_sm * self._weight_kg_sm) / 1000


road = Road(-10, 5000)
print(road.get_weight())
