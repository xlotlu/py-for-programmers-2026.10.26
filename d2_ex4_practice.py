# dat fiind dataset-ul
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]

# scrieți o funcție
def get_friend_by_name(lst, name):
    pass
# ce returnează prietenul cu acel nume

get_friend_by_name(friends, "Jane")

def get_friend_by_name(lst, name):
    for friend in lst:
        if friend[0] == name:
            return friend

# scrieți o funcție
def find_friends_by_hobby(lst, hobby):
    pass
# ce returnează o listă nouă cu prietenii
# cu acel hobby

def find_friends_by_hobby(lst, hobby):
    filtered = []
    for friend in lst:
        if hobby in friend[2]:
            filtered.append(friend)
    return filtered

find_friends_by_hobby(friends, "hiking")


# scrieți o funcție
def find_friends_by_age(lst, min_age=None, max_age=None):
    pass
# ce returnează o listă nouă cu prietenii
# cu vârstă între `min_age` respectiv `max_age`,
# dacă nu sunt None.

def find_friends_by_age(lst, min_age=None, max_age=None):
    filtered = []

    for friend in lst:
        age = friend[1]

        if (min_age is None or age >= min_age) and \
           (max_age is None or age <= max_age):
            filtered.append(friend)

    return filtered

# same thing as above,
# the if formatted differently
def find_friends_by_age(lst, min_age=None, max_age=None):
    filtered = []

    for friend in lst:
        age = friend[1]

        if (
            (min_age is None or age >= min_age)
            and
            (max_age is None or age <= max_age)
        ):
            filtered.append(friend)

    return filtered

# shortcircuit if min_age=None and max_age=None
def find_friends_by_age(lst, min_age=None, max_age=None):
    if min_age is None and max_age is None:
        # maybe don't do this,
        # because the rest of the code returns a new list,
        # and this would return a reference to the old
        #return lst

        # so then, return a copy
        return lst.copy()

    filtered = []

    for friend in lst:
        age = friend[1]

        if (
            (min_age is None or age >= min_age)
            and
            (max_age is None or age <= max_age)
        ):
            filtered.append(friend)

    return filtered

print("»» 1"); print(find_friends_by_age(friends))
print("»» 2"); print(find_friends_by_age(friends, 20, 40))
print("»» 3"); print(find_friends_by_age(friends, max_age=28))
print("»» 4"); print(find_friends_by_age(friends, 30))

# apoi:
# a) folosiți get_friend_by_name() pentru a o găsi pe Jane.
#    îmbătrâniți-o cu un an.
#

jane = get_friend_by_name(friends, "Jane")
jane[1] += 1


# b) folosiți find_friends_by_age() pentru a găsi
#    toți prietenii cu vârsta mai mare de 30 de ani.
#    adăugați-le într-o singură operațiune
#    hobby-urile ["sudoku", "bingo"].

for f in find_friends_by_age(friends, min_age=30):
    f[2].extend(["sudoku", "bingo"]) 

#
# c) adăugați-i lui Sam hobby-ul "hiking".
get_friend_by_name(friends, "Sam")[2].append("hiking")

#
# d) chain-uiți funcțiile `find_friends_by_hobby` și 
#    `find_friends_by_age` pentru a găsi toți prietenii
#    cu vârsta mai mare de 20 de ani interesați de
#   "hiking".


print(
    find_friends_by_hobby(
        find_friends_by_age(friends,  min_age=20),
        "hiking"
    )
)


# Dacă ați terminat cele de mai sus,
# Exercițiu:
# 
# modificați funcția get_friend_by_name()
# astfel încât să facă acces cache-uit.

cache = {}
def get_friend_by_name(lst, name):
    # să nu facă search în toată lista
    # dacă am mai accesat acest obiect deja
    if name in cache:
        return cache[name]

    for friend in lst:
        print("debug » [processing]", friend[0])
        if friend[0] == name:
            # don't forget to cache
            cache[name] = friend
            return friend
get_friend_by_name(friends, "Dan")

# a bit cleaner:

def get_friend_by_name(lst, name):
    cache = get_friend_by_name._cache

    if name in cache:
        return cache[name]

    for friend in lst:
        if friend[0] == name:
            cache[name] = friend
            return friend
get_friend_by_name._cache = {}