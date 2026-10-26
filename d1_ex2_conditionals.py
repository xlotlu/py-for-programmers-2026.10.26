'''
if condition:
    statement_1
    statement_2
else:
    other_statements

    if something:
        something_else
'''
# ^^ acesta este un multiline string.
#    abuzat deseori drept multi-line comment

# în Python toate statement-urile care au sub-bloc
# de logică se încheie cu ":"
#
# și au sub-blocul indentat


# Exercițiu:
# cereți vârsta utilizatorului cu input()
# și... age-discrimination:
# dacă are sub 18 ani printați-i mesajul
# "Ne pare rău, ești prea tânăr"
# altfel printați
# "Ești acceptat"

age = input("Vârsta ta? ")
age = int(age)

if age < 18:
    print("Ne pare rău, ești prea tânăr")
else:
    print("Ești acceptat")

# întrebare:
# cum tratăm cu input invalid?

# răspuns 1: exception handling
age = "bla"

try:
    age = int(age)
except ValueError:
    print("Număr invalid")

# răspuns 2: cunoscând metodele str-ului
age = "blu"

if age.isdecimal():
    age = int(age)
else:
    print("Număr invalid")


# Sintaxa completă de condițional:
"""
if conditie1: 
    statements
elif conditie2:
    statements
# ...
elif conditien:
    statements    
else:
    statements

if conditie1: 
    statements

if conditie1: 
    statements
elif conditie2:
    statements

if conditie1: 
    statements  
else:
    statements
"""

# Exercițiu
# scrieți un condițional care în funcție
# de variabila `hour` (care este de tip int)
# face print unuia din string-urile
#
# "Bună dimineața"  între 5 și 10
# "Bună ziua"       între 10 și 18
# "Bună seara"      între 18 și 22
# "Noapte bună"     între 22 și 5

hour = "3"
hour = int(hour)

if hour >= 0 and hour < 5:
    print('Noapte bună!')
elif hour >= 5 and hour < 10:
    print('Bună dimineața!')
elif hour >= 10 and hour < 18:
    print('Bună ziua!')
elif hour >= 18 and hour < 22:
    print('Bună seara!')
elif hour >= 22 and hour < 25: # 24 zicem ca e ora 0
    print('Noapte bună!')
else: # negativ sau peste ora 24
    print('Introdu o oră validă!')

if hour < 0 or hour > 23:
    print("Oră invalidă")

if hour >= 5 and hour < 10:
    print('Bună dimineața!')
elif hour >= 10 and hour < 18:
    print('Bună ziua!')
elif hour >= 18 and hour < 22:
    print('Bună seara!')
else:
    print("Noapte bună")


# operator chaining
if 5 <= hour < 10:
    print('Bună dimineața!')
# ...
