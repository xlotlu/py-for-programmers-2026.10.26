# scrieți o funcție
# ce filtrează un iterabil după prima litera
# și returnează o listă.
# Pattern de acumulare!
def filter_by_first_letter(iterable, letter):
    # 1. instanțiem obiectul în care acumulăm
    out = []

    # 2. iterăm în sursă
    for elem in iterable:
        # 3. filtrăm
        if elem[0] == letter:
            # 4. acumulăm
            out.append(elem)

    # x. returnăm
    return out


# 1. implementare LIFO
#    (last-in first-out)

lst = []
lst.append("elem 1")
lst.append("elem 2")
lst.append("elem 3")

lst.pop()
lst.pop()
lst.pop()

# 2. implementare FIFO
#    (first-in first-out)
lst = []
lst.append("elem 1")
lst.append("elem 2")
lst.append("elem 3")

lst.pop(0) # re-indexează tot
lst.pop(0)
lst.pop(0)

# 3. FIFO cu insert
lst = []
lst.insert(0, "elem 1") # re-indexează tot
lst.insert(0, "elem 2")
lst.insert(0, "elem 3")

lst.pop()
lst.pop()
lst.pop()


iterable = range(5)

lst.extend(iterable)
# este echivalent cu:
for elem in iterable:
    lst.append(elem)

tup = ["ala", "bala", "ala", "bala", "ala", "trosc"]
try:
    zala_idx = tup.index("zala")
except ValueError:
    print("there is no zala!")

# implementați o funcție
def remove(lst, elem):
    pass
# ce face același lucru cu `lst.remove()`
# șterge prima apariție a elementului `elem`
# din lista `lst`.
# 
# dacă elem nu există în listă,
# raise ValueError()

def remove(lst, elem):
    #idx = 0
    #while idx < len(lst):
    #    idx += 1

    for idx in range(len(lst)):
        value = lst[idx]
        if value == elem:
            del lst[idx]
            return

    # elem was not found
    raise ValueError("not found")
