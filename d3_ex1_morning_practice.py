# două modalități de a utiliza dicționare.
# 1. stil id - valoare (sau set de valori)
d = {
  'id1': 'value(s)',
  'id2': 'value(s)',
}

# 2. stil listă de obiect chei-valori
lst = [
  {
    'name': 'Jane',
    'age': 20,
    'hobbies': [],
  },
  {
    'name': 'Sam',
    # ...
  },
  {
    'name': 'George'
  },
]

# Exercițiu:
# dat fiind dataset-ul
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]
# transformați-l într-o listă de dicționare
# cu cheile 'name', 'age', 'hobbies'

d = {}
d['name'] = '...'
d['age'] = '...'

d = {
    'name': name,
    'age': age,
}

# assignment-ul multiplu
# se numește "iterable unpacking"

# deci suportă orice(!) iterabil
first_friend = friends[0]
name, age, hobbies = first_friend
a, b, c, *_ = range(10000)
friend_1, friend_2, *_ = map(lambda el: el[0], friends)

# rezolvare pt. mai sus
friends_as_dicts = []

for elem in friends:
    name, age, hobbies = elem

    d = {
        'name': name,
        'age': age,
        'hobbies': hobbies,
    }

    friends_as_dicts.append(d)

# și mai condensat.
for name, age, hobbies in friends:
    d = {
        'name': name,
        'age': age,
        'hobbies': hobbies,
    }

    friends_as_dicts.append(d)

# cum accesăm age-ul celui de-al 2lea prieten?
friends_as_dicts[2]['age']


# Exercițiu de gândire:
# dataset-ului nostru i se tot schimbă numărul de coloane.
# așa că ne-am enervat (constructiv!) și ne-am setat
# coloanele într-o variabilă.

columns = 'name', 'age', 'hobbies', 'address', 'phone', 'email'

friends_as_dicts = []
for elem in friends:
    d = {}

    for idx in range(len(columns)):
        colname = columns[idx]
        value = elem[idx]

        d[colname] = value

    friends_as_dicts.append(d)    

# mai condensat, folosind `enumerate()`
# ce face enumerate? iată:
for idx, elem in enumerate(lst):
    print(idx, elem, sep=" :: ")

columns = 'name', 'age', 'hobbies', 'address', 'phone', 'email'

friends_as_dicts = []
for elem in friends:
    d = {}

    for idx, colname in enumerate(columns):
        value = elem[idx]

        d[colname] = value

    friends_as_dicts.append(d)  

# ȘI mai condensat:
# enter zip:
lst = ["ala", "bala", "porto", "cala"]
otherlst = [11, 12, 13, 14, 15]
print(list(zip(lst, otherlst)))

# controlabil ce se întâmplă dacă
# iterabilele au lungimi diferite:
print(list(
    zip(lst, otherlst, strict=True)
))

friends_as_dicts = []
# zip aplicat:
for elem in friends:
    friends_as_dicts.append(
        dict(
            zip(columns, elem)
        )
    )


# Exercițiu:
# dat fiind dicționarul
occupations = {
    "Jane": "nurse",
    "Dan": "firefighter",
    "Mike": "dancer",
    "Sam": "boat captain",
    "Anna": "gardner",
}
# unde cheia este numele și valoarea este ocupația,
# augmentați dicționareele potrivite din `friends_as_dicts`
# astfel încât să setați cheia "occupation"
# cu valoarea potrivită.

