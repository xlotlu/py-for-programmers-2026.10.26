s = "Un StRiNg"

# relevante

s.split() # sparge după whitespace
          # (oricât de lung ar fi)
# vs.
s.split(' ') # creează elemente goale

s.join()


s.replace()


s.lower()
s.upper()

# utile, câteodată
s.endswith()
s.startswith()

s.strip()


s.splitlines()


s.format() # !!!



# poate relevante

s.removeprefix()
s.removesuffix()

# prietenii lui .strip() specializați
s.rstrip()
s.lstrip()


## utile în shell:
s.center()
s.rjust()
s.ljust()


## utile în alte contexte
s.casefold() # pt. case-insensitive normalisation

'/bla/bli/blu/blix.txt'.rsplit('/', maxsplit=1)


# ok...

s.capitalize()


# dat fiind acest header
header = '|    Name    |       Address       |   Phone  |'
# extrageți numele coloanelor
columns = list(
    map(str.strip,
        header.split('|')[1:-1])
)

# dat fiind `columns` de mai sus
# creați string-ul cap de tabel
# de forma
"### Column 1 ### Column 2 ### Column 3 ###"

# multiple variante:
# masăm lista
" ### ".join([''] + columns + [''])
# masăm string-ul de output
'### ' + " ### ".join(columns) + ' ###'
# old-school interpolation
'### %s ###' % " ### ".join(columns)
# interpolation with .format()
'### {} ###'.format(" ### ".join(columns))
# the same, but named placeholder
'### {columns} ###'.format(columns=" ### ".join(columns))
# pretty much the same, but f-string
columns_str = " ### ".join(columns)
f'### {columns_str} ###'


# Despre string formatting

"Numele meu este {} și am {} ani.".format("Gigel", 45)
"Numele meu este {0} și am {1} ani.".format("Gigel", 45)
"Numele meu este {1} și am {0} ani.".format("Gigel", 45)
"Numele meu este {name} și am {age} ani.".format(age=45, name="Gigel")
