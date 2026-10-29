class AccessError(Exception):
    pass


class MyCls:
    def __init__(self, limits=5000):
        self.limits = limits # this is an attribute
        self.counter = 0

    def __repr__(self):
        return f"MyCls(limits={self.limits})"

    def __str__(self):
        return f'MyCls :: with limits {self.limits}'

    def check_status(self):
        return self.counter < self.limits

    def access(self):
        print("» being accessed")

        if not self.check_status():
            raise AccessError("Access denied, limits exceed.")

        self.counter += 1

#inst = MyCls()
#print("» inst. este", inst)



# task:
# implementați un
class Point:
    pass
# ce este inițializat cu argumentele `x` și `y`
# și:
# 1) definiți-i __repr__
# 2) faceți-l în context de string să arate ca un set de coordonate
#    "(x, y)"
# 3) creați o metodă
    def translate(self, dx, dy):
        pass
#    ce translatează coordonatele x respectiv y 
# 4) creați o metodă
    def get_distance_from_origin(self):
        pass
#   notă: există math.sqrt

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)