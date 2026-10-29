# generatorul este un caz special de iterator

def myfunc():
    print("am intrat în funcție")
    yield 23
    print("după primul yield")
    yield 34
    print("după al doilea yield")
    yield 45
    print("ies din funcție")

# iterat:
genobj = myfunc()
for elem in genobj:
    print(elem)

# item by item
genobj = myfunc()
next(genobj)
next(genobj)
next(genobj)
try:
    next(genobj)
except StopIteration:
    print("succes, am consumat tot!")

# concretizat
list( myfunc() )


# Exercițiu:
# dat fiind fișierul data/temp_sensor_data.csv
#
# calculați media orară a temperaturilor.
#
# inițial scrieți o funcție ce returnează o listă
# cu mediile.






