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


# scrieți o funcție
def find_friends_by_hobby(lst, hobby):
    pass
# ce returnează o listă nouă cu prietenii
# cu acel hobby


# scrieți o funcție
def find_friends_by_age(lst, min_age=None, max_age=None):
    pass
# ce returnează o listă nouă cu prietenii
# cu vârstă între `min_age` respectiv `max_age`,
# dacă nu sunt None.


# apoi:
# a) folosiți get_friend_by_name() pentru a o găsi pe Jane.
#    îmbătrâniți-o cu un an.
#
# b) folosiți find_friends_by_age() pentru a găsi
#    toți prietenii cu vârsta mai mare de 30 de ani.
#    adăugați-le într-o singură operațiune
#    hobby-urile ["sudoku", "bingo"].
#
# c) adăugați-i lui Sam hobby-ul "hiking".
#
# d) chain-uiți funcțiile `find_friends_by_hobby` și 
#    `find_friends_by_age` pentru a găsi toți prietenii
#    cu vârsta mai mare de 20 de ani interesați de
#   "hiking".


# Dacă ați terminat cele de mai sus,
# Exercițiu:
# 
# modificați funcția get_friend_by_name()
# astfel încât să facă acces cache-uit. 