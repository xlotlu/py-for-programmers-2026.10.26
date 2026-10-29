# continuăm exercițiul de ieri

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

    def get_distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# învățăm inheritance
class ThreeDPoint(Point):
    def __init__(self, x, y, z):
        # vrem să executăm logica părintelui, întotdeauna
        Point.__init__(self, x, y)

        self.z = z





# considerați tree-ul de inheritance:
class Ancestor:
    def method(self):
        print("Ancestor running")

class P1(Ancestor):
    def method(self):
        Ancestor.method(self)

        print("P1 running")

class P2(Ancestor):
    def method(self):
        Ancestor.method(self)

        print("P2 running")

class Descendant(P1, P2):
    def method(self):
        P1.method(self)
        P2.method(self)

        print("Descendant running")


# pentru a rezolva problema "diamond inheritance"
# (și pentru că simplifică lucrurile)
# folosim `super()`

class Ancestor:
    def method(self):
        print("Ancestor running")

    def override_me(self):
        print("not yet overriden")

class P1(Ancestor):
    def method(self):
        super().method()

        print("P1 running")

    def override_me(self):
        print("P1's overriden")

class P2(Ancestor):
    def method(self):
        super().method()

        print("P2 running")

    def override_me(self):
        print("P2's overriden")

class Descendant(P1, P2):
    def method(self):
        super().method()

        print("Descendant running")



class ThreeDPoint(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    #TODO
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"
    # TODO
    def __str__(self):
        return f"({self.x}, {self.y})"

    def translate(self, dx, dy, dz):
        super().translate(dx, dy)
        self.z += dz

    def __eq__(self, other):
        return super().__eq__(other) and self.z == other.z

# să rezolvăm și __repr__ și __str__:
class Point(Point):
    def as_tuple(self):
        return (self.x, self.y)

    def __repr__(self):
        return f"{self.__class__.__name__}{self.as_tuple()}"

    def __str__(self):
        return str(self.as_tuple())

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        
        return self.as_tuple() == other.as_tuple()

class ThreeDPoint(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def as_tuple(self):
        return super().as_tuple() + (self.z,)
    
    def translate(self, dx, dy, dz):
        super().translate(dx, dy)
        self.z += dz


# loc de parcat cursorul
#