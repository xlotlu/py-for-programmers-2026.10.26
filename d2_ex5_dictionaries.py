d = {
    "k1": "v1",
    "k2": "v2",
}

# vine din clasa
dict()

# assignment
d["k1"] = "valoare"

# același lucru cu creație de cheie nouă
d["k3"] = "valoare"

# Exercițiu
# dată fiind lista
cities = [
    ['Cluj-Napoca', 450],
    ['Timișoara', 550],
    ['Iași', 390],
    ['Constanța', 225],
    ['Brașov', 180],
    ['Craiova', 230],
    ['Galați', 250],
    ['Ploiești', 60],
    ['Oradea', 610],
    ['Sibiu', 275],
    ['Arad', 560],
    ['Bacău', 300],
    ['Brăila', 200],
    ['Buzău', 110],
    ['Suceava', 450],
    ['Pitești', 120],
    ['Târgu Mureș', 330],
    ['Baia Mare', 600],
]

# creați un dicționar dcities
# cu cheia nume orașului
# și valoarea distanța

dcities = {}
for elem in cities:
    name = elem[0]
    distance = elem[1]

    dcities[name] = distance

for elem in cities: dcities[elem[0]] = elem[1]

for elem in cities:
    name, distance = elem
    dcities[name] = distance

for name, distance in cities:
    dcities[name] = distance


# celelalte modalități de a inițializa
# un dicționar.
dict(key1="value 1", key2="value 2")

# dată fiind o structură
bidimensional =  [  ("k1", "v1"), ("k2", "v2"), ]
dict(bidimensional)


# iterarea dicționarelor
for key in dcities.keys():
    print(key)

for values in dcities.values():
    print(values)

for item in dcities.items():
    print(item)


