from abc import abstractmethod

class Figure:

    def __init__(self, name, x, y, z, isFlipped, color, mode):
        self.__name = name
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)
        self.__isFlipped = isFlipped

        self.__color = color

        self.__visual_mode = mode

        self.__vertices = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        self.__z = value

    @property
    def isFlipped(self):
        return self.__isFlipped

    @isFlipped.setter
    def isFlipped(self, value):
        self.__isFlipped = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def visual_mode(self):
        return self.__visual_mode

    @visual_mode.setter
    def visual_mode(self, value):
        self.__visual_mode = value

    # Функция в дальнейшем используется для получения точек
    @staticmethod
    def custom_map(n, start1, stop1, start2, stop2):
        return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2

    @abstractmethod
    def draw(self):
        pass

    def __str__(self):
        return self.name