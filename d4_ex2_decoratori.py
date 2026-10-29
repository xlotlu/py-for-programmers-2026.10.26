# un decorator este o funcție
# ce primește ca argument o funcție
# și returnează o funcție

# (de fapt, mai precis
# un decorator este un callable
# ce primește ca argument un callable
# și returnează un callable)

from functools import cache # este decorator
from random import randint

def myrand(a, b):
    return randint(a, b)

#my_decorated_rand = cache(myrand)
myrand = cache(myrand)

# ^^ acesta este pattern-ul de decorare
#    în Python

# căruia i s-a inventat
# syntactic sugar:
@cache
def myrand(a, b):
    return randint(a, b)


# să scriem un decorator

def deco(func):
    print("» sunt decoratorul, decorez pe", func)

    def _inner(*args, **kwargs): # arg. packing
        print("-- sunt funcția decorată, rulez originalul")
        retval = func(*args, **kwargs) # arg. unpacking
        print("-- sunt funcția decorată, final")

        return retval

    return _inner

@deco
def myfunc(x, y):
    print("! sunt funcția originală")
    return x * y


# Exercițiu: 
# scrieți un decorator
def timeit(func):
    pass
# ce face print cu durata de execuție
#
# hint 1: în modulul `datetime`, clasa `datetime`
# are metoda `.now()`
# hint 2: obiectele de tip `datetime` suportă diferență


# Opțional:
# îmbunătățiți print-ul lui timeit
# cu numele funcției
# și argumentele primite

from datetime import datetime

def timeit(func):
    LOG_LINE = "{module}.{func}({args}) -> {retval} :: {duration}ms"

    def _inner(*args, **kwargs):
        start_time = datetime.now()
        out = func(*args, **kwargs)
        end_time = datetime.now()

        delta = (end_time - start_time).total_seconds()

        print(LOG_LINE.format(
            module=__name__,
            func=func.__qualname__,
            args=args + tuple(kwargs.items()),
            retval=out,
            duration=delta*1000,
        ))

        return out

    return _inner

from time import sleep

@timeit
def sleepy(x):
    sleep(x / 10)

    return 42 * x 


# next-level decorator:
from functools import lru_cache


@lru_cache(maxsize=3)
def myfunc(x, y):
    return randint(x, y)

# deci blueprint-ul în loc să fie
def deco(func):
    def _inner(*args, **kwargs): # arg. packing
        retval = func(*args, **kwargs) # arg. unpacking
        return retval

    return _inner

# ... este:

def wrapper(args):
    # execută cod ce generează o funcție decorator custom
    def deco(func):
        def _inner(*args, **kwargs): # arg. packing
            retval = func(*args, **kwargs) # arg. unpacking
            return retval

        return _inner
    return deco

# TODO, pentru voi, când vreți să vă prindeți urechile
#       și să.... really, really get it.
# scrieți un decorator care se comportă ca lru_cache
# care poate fi folosit și așa
@lru_cache
def myfunc(x, y):
    return randint(x, y)

# și așa
@lru_cache(maxsize=3)
def myfunc(x, y):
    return randint(x, y)

# și așa
@lru_cache(3)
def myfunc(x, y):
    return randint(x, y)

# considerați ce se întâmplă în spate:
# lru_cache(myfunc) --> returnează myfunc decorat
# lru_cache(15)(myfunc)  --> returnează myfunc decorat


# Also:
# pentru cazuri complexe, merită
# să scriem un decorator pe baza de clasă

class MyThing:
    def __init__(self, arg):
        self.arg = arg

    def __call__(self, x, y):
        print('eu sunt "o funcție", hahaha')
        print("am acces la state-ul obiectului:", self.arg)
        return x * y * self.arg

class ClassBasedDeco:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("înainte de funcția vanilla")
        retval = self.func(*args, **kwargs)
        print("după funcția vanilla")
        return retval





