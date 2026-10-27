# item access means:
# obj[ item ]
# 
# adică sintaxa de acces cu paranteze drepte.
#
# care în cazul sequnces este
# (caz particular!) index access

lst = ["ala", "bala", "porto", "cala"]

lst[1]
# lst[5] # IndexError

dct = {
    "cheie": "valoare",
    0: "prima valoare",
    1: "ok... funny",
}
# dct[99] # KeyError


##### slice syntax ####
#lst[start:stop]
#lst[start:stop:step]
# fiecare din părți poate să fie lipsă
# și va primi valoare default ce are sens
# în context
lst[1:3]

# ultimele 2 elemente?
lst[-2:]

# toate elementele în afară de ultimul?
lst[:-1]

# exemplu cu numpy
import numpy
arr = numpy.array([
    [1, 2, 3, 4, 5],
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
])

# ultimele 3 coloane, ultimele 2 rânduri
arr[ -2:  , -3: ]

# să o decodăm ca slice și tuplă:
# de fapt echivalentă cu...
arr.__getitem__(
    (
        slice(-2, None),
        slice(-3, None)
    )
)