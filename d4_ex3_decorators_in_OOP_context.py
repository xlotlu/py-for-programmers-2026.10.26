# decorators in OOP context

# @property
#
# @classmethod
# @staticmethod

# @property oferă posibilitatea
# de a implementa getter / setter 

class MyCls:
    def __init__(self):
        self._hidden_value = 55

    @property
    def value(self):
        # now I execute code
        # but pretend I'm an attribute...
        print("getter: mă execut")
        return self._hidden_value

    @value.setter
    def value(self, v):
        # i execute code once again
        print("setter: mă execut")
        if v < 0:
            raise ValueError("no negativ numbers pls")
        self._hidden_value = v


# ce este mai sus este ce veți folosi
# (probabil) întotdeauna

# dacă vrem să facem și deleter,
# are sens ceva de genul...

class MyCls:
    def __init__(self):
        self._hidden_value = 55

    @property
    def value(self):
        # now I execute code
        # but pretend I'm an attribute...
        print("getter: mă execut")

        try:
            self._hidden_value
        except AttributeError:
            raise AttributeError("cu mesajul meu") from None

        return self._hidden_value

    @value.setter
    def value(self, v):
        # i execute code once again
        print("setter: mă execut")
        if v < 0:
            raise ValueError("no negativ numbers pls")
        self._hidden_value = v

    @value.deleter
    def value(self):
        print("deleter: mă execut")
        del self._hidden_value

####

# loc unde are sens să fie folosit:
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)


#######

# @classmethod face ca primul argument implicit
# transmis metodei să nu fie instanța de obiect
# ci să fie clasa în sine.

class MyCls:
    def __init__(self):
        pass

    @classmethod
    def method(cls):
        print(cls)

# se comportă consecvent atât via instanță
# cât și via clasă:
MyCls().method()
MyCls.method()

# ce classmethods am întâlnit până acum?
import datetime as dt
dt.datetime.now()
dt.date.today()
dict.fromkeys("abc")

# folosit pentru metode gen custom constructor

#######

# @staticmethod

class MyCls:
    def __init__(self):
        pass

    @staticmethod
    def method():
        print("eu sunt o.. metodă, sau ce?")

# utility?
# helper function that makes sense
# to be stored in the class namespace

class Vector:
    def __init__(self, length, angle):
        self.length = length
        self.angle = angle

    def __repr__(self):
        return f"Vector({self.length}, {self.angle})"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def distance_from_origin(self):
        return self.get_length_between(self, Point(0, 0))

    def __sub__(self, other):
        angle = 4.2 # chosen by fair computation
        distance = self.get_length_between(other, self)

        return Vector(distance, angle)

    @staticmethod
    def get_length_between(p1, p2):
        return math.sqrt(
            (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2
        )

