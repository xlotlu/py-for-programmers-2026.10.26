### obiecte cu acces după item.

import random

class ItemAccessible:
    def __getitem__(self, key):
        return random.randint(1, 1000)

    def __setitem__(self, key, value):
        # teoretic setează ceva în spate...
        pass

### obiecte iterabile

class Iterable:
    def __init__(self):
        self._data = ["ala", "bala", "porto"]
        self._idx = 0

    def __iter__(self):
        # în situații mai complexe putem instanția un alt obiect,
        # a cărui clasă implementează pe __next__.
        #
        # (așa cum fac lista, tupla, str etc.)
        return self

    def __next__(self):
        idx = self._idx
        try:
            value = self._data[idx]
        except IndexError:
            raise StopIteration()
        
        self._idx += 1
        return value

    def rewind(self):
        self._idx = 0

    # dacă vreți să suporte len():
    def __len__(self):
        pass        


### custom attribute access

class CustomAttr:
    class_attr = "ceva pe clasă"

    def __init__(self):
        self._hidden_database = {
            'v1': "valoarea 1",
            'v2': "valoarea 2",
        }

        self.attr1 = "există"
        self.attr2 = "și el există"

    def __getattr__(self, name):
        # se rulează doar când atributul `name` nu există

        print("» accessing:", name)

        try:
            value = self._hidden_database[name]
        except KeyError:
            raise AttributeError() from None
        else:
            return value

        super().__ge

    def __setattr__(self, name, value):
        # acesta se rulează la orice attribute assignment.
        # trebuie să avem grijă să facem handling __doar__
        # la ce ne interesează
        if name in (
            '_hidden_database',
            'attr1',
            'attr2',
        ):
            super().__setattr__(name, value)
            return

        self._hidden_database[name] = value

    def __getattribute__(self, name):
        # acesta se rulează la orice attribute access.
        # atenție! a face overriding aici, înseamnă
        # a face override la the very basic attribute access
        print("» i spy:", name)
        return super().__getattribute__(name)

