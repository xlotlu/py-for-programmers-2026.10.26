def func(arg1, arg2, *args):
    print("» arg1:", arg1)
    print("» arg2:", arg2)
    print("» args:", args)

func("unu", "doi")
func("unu", "doi", "trei")
func("unu", "doi", "trei", "patru")


def func(arg1, arg2, arg3=50):
    print("» arg1:", arg1)
    print("» arg2:", arg2)
    print("» arg3:", arg3)

func("unu", "doi")
func("unu", "doi", "trei")
func("unu", "doi", "trei", "patru")


def func(arg1, arg2, *args, kwarg1="default"):
    print("» arg1:", arg1)
    print("» arg2:", arg2)
    print("» args:", args)
    print("» kwarg1:", kwarg1)

func("unu", "doi", "trei", kwarg1="valoare nouă")

def func(arg1, arg2, *args,
         kwarg1="default", kwarg2="ok", **kwargs):
    print("» arg1:", arg1)
    print("» arg2:", arg2)
    print("» args:", args)
    print("» kwarg1:", kwarg1)
    print("» kwarg2:", kwarg2)
    print("» kwargs:", kwargs)

func("unu", "doi", "trei",
     kwarg1="valoare nouă",
     ceva_nespecificat="123",
     povești="wow!",
     kwarg2="ceva")


#    * și ** în semnătura funcției fac argument packing

# există argument unpacking când este chemată funcția
lst = ["ala", "bala", "porto"]
print(*lst, sep=" | ")

opts = {
    "sep": " | ",
    "end": " «««\n"
}

print("o", "poveste", **opts)


# utilizare de packing / unpacking în OOP:

class Parent:
    def method(self, complicated, signature="ok"):
        pass

class Child(Parent):
    def method(self, *args, **kwargs):
        return super().method(*args, **kwargs)

class AnotherChild(Parent):
    # am un kwarg care mă interesează numai pe mine:
    def method(self, *args, my_kwarg="something", **kwargs):
        # do_something_with(my_kwarg)
        return super().method(*args, **kwargs)

class YetAnotherChild(Parent):
    # tot cu un kwarg care mă interesează numai pe mine:
    def method(self, *args, **kwargs):
        my_kwarg = kwargs.pop("my_kwarg", "valoare default")
        # do_something_with(my_kwarg)
        return super().method(*args, **kwargs)

def func(arg, kwarg=None):
    pass
def func(arg, *, kwarg=None):
    pass
def func1(arg, kwarg=None):
    pass
def func2(arg, *, kwarg=None):
    pass
func1(1, 2)
func1(arg=1, kwarg=2)
func2(1, 2)
func2(1, kwarg=2)
def func2(arg, *, kwarg=None):
    pass
func1(arg=1, kwarg=2)
def func3(arg, /, kwarg=None):
    pass
func3(1, 2)
func3(arg=1, kwarg=2)
func3(1, kwarg=2)
def func4(arg, *, /, kwarg=None):
    pass
def func4(arg, /, *, kwarg=None):
    pass
func4(1, kwarg=2)
func4(arg=1, kwarg=2)
func4(1, 2)
