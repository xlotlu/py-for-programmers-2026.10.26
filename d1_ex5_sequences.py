# sequences:

# tuple:
tup = (1, 2, 3)

# list:
lst = ["ala", "bala", "porto"]

# str:
s = "abcdefg"

# iterabil:
#for elem in iterable:
#    print(elem)


# Q: Cum facem să iterăm prin 
# toate valorile din tup, lst și s?

# A: iterăm pe 2 niveluri
for iterable in tup, lst, s:
    for elem in iterable:
        print(elem)

# A alt: itertools.chain
from itertools import chain

for elem in chain(tup, lst, s):
    print(elem)



# introducem operatorul `in`
tup = (1, 2, 3)
lst = ["ala", "bala", "porto"]
s = "abcdefg"

"ala" in lst
3 in tup
"g" in s
"efg" in s
