while condition:
    statements

    # loop control se face cu
    break    # ies din loop
    # și
    continue # repet bucla
    # 
    # (valabile și în for)

# scrieți o funcție
def get_int_input(prompt=""):
    pass
# ce promptează în mod repetat
# utilizatorul cu promptul `prompt`
# până când acest introduce un număr întreg.
# apoi returnează acest număr întreg
# drept int.


# v.1.: very explicit, while True
def get_int_input(prompt=""):
    while True:
        num = input(prompt)

        if num.isdecimal():
            break
        
        print("Invalid number, try again!")

    return int(num)

# v.2. scurtată:
def get_int_input(prompt=""):
    while True:
        num = input(prompt)

        if num.isdecimal():
            return int(num)

        print("Invalid number, try again!")

# v.3. condițional pe ce ne interesează:
def get_int_input(prompt=""):
    num = input(prompt)

    while not num.isdecimal():
        # deci avem o eroare
        print("Invalid number, try again!")

        num = input(prompt)

    # am ieșit din while deci totul este în regulă
    return int(num)

def get_int_input(prompt=""):
    num = input(prompt)

    while not num.isdecimal():
        # deci avem o eroare
        print("Invalid number, try again!")

        num = input(prompt)

    # am ieșit din while deci totul este în regulă
    return int(num)

# don't do this:
def get_int_input(prompt=""):
    # using the walrus operator
    while not (num := input(prompt)).isdecimal():
        # deci avem o eroare
        print("Invalid number, try again!")

    # am ieșit din while deci totul este în regulă
    return int(num)

# v.x.: with exception handling:
def get_int_input(prompt=""):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number, try again!")
        