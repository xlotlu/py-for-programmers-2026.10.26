# what is an iterable?

for elem in ["bla", "bli", "blu"]:
    print(elem)

for elem in range(10):
    print(elem)

# dat fiind
range(20)
# faceți print pătratelor numerelor impare

for x in range(20):
    if x % 2 == 1:
        print(x ** 2)

# sau
for x in range(20):
    if x % 2:
        print(x ** 2)

# dată fiind lista de orașe
cities = [
 'Cluj-Napoca',
 'Timișoara',
 'Iași',
 'Constanța',
 'Craiova',
 'Brașov',
 'Galați',
 'Ploiești',
 'Oradea',
 'Brăila',
 'Arad',
 'Sibiu',
 'Bacău',
 'Târgu Mureș',
 'Baia Mare',
 'Buzău',
 'Satu Mare',
 'Suceava',
]
# și dat fiind că accesul după index
# se face cu sintaxa
# elem[index]
# printați orașele care încep cu litera "B"

for city in cities:
    if city[0] == "B":
        print(city)

# extra:
# scrieți o funcție
def filter_by_first_letter(lst, letter):
    pass
# ce printează, la fel ca mai sus

def filter_by_first_letter(lst, letter):
    for elem in lst:
        if elem[0] == letter:
            print(elem)

# cu ce știm până acum,
# putem să modificăm funcția
# să returneze o listă cu elementele filtrate?

# Pattern de acumulare!
def filter_by_first_letter(lst, letter):
    # 1. instanțiem obiectul în care acumulăm
    out = []

    # 2. iterăm în sursă
    for elem in lst:
        # 3. filtrăm
        if elem[0] == letter:
            # 4. acumulăm
            out += [elem]
            # or, un-ugly:
            #out.append(elem)

    # x. returnăm
    return out
