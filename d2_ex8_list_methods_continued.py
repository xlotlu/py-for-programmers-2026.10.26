# Mâine (adică azi):
# dată fiind structura de date
# bi-dimensională
# de forma [city, distance]
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
# sortați-o după distanță

def mysortingfunction(item):
    return item[1]
cities.sort(mysortingfunction)

# dată fiind lista
l = [
    "bla",
    "Blu",
    "bli",
    "Ble",
]
# sortați-o case insensitive
# psss: `str` are metoda .lower()

def insensitive(item):
    return item.lower()
l.sort(key=insensitive)


# extrageți numele orașelor din cities
# într-o listă nouă.
cnames = []
for c in cities:
    name = c[0]
    cnames.append(name)

# faceți același lucru folosind:
def extract_name(item):
    return item[0]

for elem in map(extract_name, cities):
    print(elem)

# Notă: există funcția
# sorted(iterable) ce suportă
# key și reverse la fel ca list.sort()
# dar funcționează pe orice iterabil.

# Știind acestea, obțineți o listă
# sortată din 
map(extract_name, cities)
# după ultima literă a numelui, case-insensitive
def funcție_dubioasă_de_sortare(item):
    # ultima literă a numelui, case-insensitive
    return item[-1].lower()

sorted(
    map(extract_name, cities),
    key=funcție_dubioasă_de_sortare
)

sorted(
    map(extract_name, cities),
    key=lambda item: item[-1].lower()
)

# având lista cities de mai sus,
# sortați-o in-place cuun lambda

# before:
def mysortingfunction(item):
    return item[1]
cities.sort(key=mysortingfunction)

# sintaxa de lambda:
# lambda args: return_value

# after:
def mysortingfunction(item):
    return item[1]

cities.sort(key=lambda item: item[1])
