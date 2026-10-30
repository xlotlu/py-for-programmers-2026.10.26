# Concepts

reprezentare

acțiunea operatorilor asupra unui data-type
este hotărâte de data-type


Python este whitespace-sensitive!


în Python totul(!) este un obiect
în Python totul este o referință

în Python, totul poate fi evaluat în context boolean

"Python comes with batteries included"

Python is self-documenting, because docstrings.



iterable: something that can be.... iterated
          (funcționează într-un for)

iterator: un iterabil suspendat în execuție.
          suportă next().
 
# De citit

(măcar o dată în viața de programator Python)

PEP-8: the styleguide
https://peps.python.org/pep-0008/

String formatting:
https://docs.python.org/3/library/string.html#format-examples

Date and time formatting
https://docs.python.org/3/library/datetime.html#format-codes


```python
import this
```


# Data types

## basic data types:

str
int
float
bool

tuple   # immutable
list    # mutable

## "sequences":

- sunt iterabile (cu for)
- sunt colecții ordonate
- sunt accesibile după index
- au metodele .count() și index()
- suportă operatorul `in`
- au o lungime dată
  (și suportă funcția `len()`)


# Debugging essentials:

print()
help()
type()


# Operators

new operators:

//
%
**


# boolean

and
or
not

is
is not

in
not in


# Important Exceptions

NameError:   simbolul respectiv (variabila) nu este definit

TypeError:   apare când s-au făcut operațiuni
             nesuportate de acel data-type.
             apare când o funcție primește
             număr invalid de parmetri.
ValueError:  apare când valoarea este nepotrivită.
             (ce înseamnă asta este context-dependent.)
IndexError:  nu există indexul
KeyError:    nu există cheia

AttributeError:    nu există atributul


UnboundLocalError: la fel ca NameError, doar că simbolul
                   este definit mai jos în cod

# VSCode utils
Ctrl+F5       run without debugging
Ctrl+/        comment
Shift+Enter   execute selection 



# păreri, și diverse

readability avoids bugs

There are 10 types of people, those who can read binary and those who can't.


There are 2 most difficult problems in computing:
- naming things
- cache invalidation
- off-by-one errors
