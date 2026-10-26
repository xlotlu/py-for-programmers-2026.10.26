print("Salut lume") 

name = "Ionuț"

print("Salut " + name)


#ret_str = input("Ce mai zici? ")
#print(ret_str)

# Exercițiu:
# Scrieți un program care cere numele utilizatorului
# și apoi face print cu string-ul
# "Salut <nume>, ce mai faci?"

#name = input("Numele tău? ")
#print("Salut " + name + ", ce mai faci?")

# "old-school" string interpolation
print("Salut %s, ce mai faci?" % name)

# string interpolation cu mai multe valori:

print("Acesta este un %s și are %f metri la o altitudine de %d" % ("bloc de piatră", 2, 3.8))

# new-school string interpolation
# "f-strings"

object = "bloc de piatră"
length = 2
altitude = 3

s = f"Acesta este un {object} și are {length:f} metri la altitudine {altitude:d}" 
print(s)