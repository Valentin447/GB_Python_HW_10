'''
Создать метакласс для паттерна Синглтон
'''

from time import sleep


class MySing(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class TrafficLight(metaclass=MySing):
    __color = (('red', 7), ('yellow', 2), ('green', 10))

    def running(self):
        inc = 1
        count = 0
        while True:
            print(self.__color[count][0])
            sleep(self.__color[count][1])
            count += inc
            if count == 2:
                inc = -1
            elif count == 0:
                inc = 1


light_1 = TrafficLight()
light_2 = TrafficLight()
print(light_1 is light_2)
