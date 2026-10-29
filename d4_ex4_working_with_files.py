# dat fiind string-ul

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

filename = "cities.txt"
content = s

# știind că modalitatea standard de scriere într-un fișier este:
with open(filename, 'w', encoding="utf-8") as f:
    f.write(content)

# scrieți conținutul lui `s` în fișierul "cities.txt"

# știind că modalitatea standard de citire linie cu linie
# dintr-un fișier este:
with open(filename, encoding="utf-8") as f:
    for line in f:
        print(line.removesuffix("\n"))

# vs. modalitatea de citire a întregului conținut:
with open(filename, encoding="utf-8") as f:
    print(
        f.read()
    )

# citiți pe "cities.txt" în cele două feluri.
# ce diferență observați?


# Exercițiu:
# scrieți o funcție
def grep(filename, match):
    pass
# ce printează fiecare linie din `filename`
# ce conține substring-ul `match`
def grep(filename, match):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if match in line:
                print(line.removesuffix("\n"))


# Îmbunătățiți funcția de mai sus
# astfel încât să facă și case-insensitive matching:
def grep(filename, match, insensitive=False):
    pass

def grep(filename, match, insensitive=False):
    with open(filename, encoding="utf-8") as f:
        if insensitive:
            match = match.casefold()

        for line in f:
            normalised = line.casefold() if insensitive else line

            if match in normalised:
                print(line.removesuffix("\n"))

