# scrieți o funcție
def count_words(txt):
    pass
# ce numără aparițiile fiecărui cuvânt
# în `txt`. și returnează un datatype potrivit
# pentru acest scop

# și testați-o cu string-ul
s = """
It was the best of times, it was the worst of times,
it was the age of wisdom, it was the age of foolishness,
it was the epoch of belief, it was the epoch of incredulity!
it was the season of Light, it was the season of Darkness?
it was the spring of hope, it was the winter of despair,
we had everything before us, we had nothing before us:
we were all going direct to Heaven,
we were all going direct the other way--in short,
the period was so far like the present period,
that some of its noisiest authorities insisted on its being received,
for good or for evil, in the superlative degree of comparison only.
"""

# v1.
import string

def get_words(txt: str) -> list:
    """
    returns a list containing the words in `txt`,
    as they appear in the text
    """
    # ^^ "docstring"
    # este alocat atributului .__doc__

    for c in string.punctuation:
        txt = txt.replace(c, " ")

    return txt.split()


# v2.
_TRANSLATION_TABLE = str.maketrans(
    string.punctuation,
    ' ' * len(string.punctuation)
)
def get_words(txt: str) -> list:
    return txt.translate(_TRANSLATION_TABLE).split()

# v3.
import re

def get_words(txt: str) -> list:
    #r"\w+" # raw string; \w means in regexp, word character
    return re.findall(r"\w+")




def count_words(txt):
    # part one:
    # o listă cu toate cuvintele
    # încercăm să killărim spațiile și .. chestiile
    #
    # să lăsăm doar cuvinte

    # part two:
    # scriem un dicționar: cheia cuvântul, valoarea count.

