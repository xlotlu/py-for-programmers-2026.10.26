# dat task-ul....
numbers = range(10)
# creați o listă cu pătratele numerelor impare
squares_odd_numbers = []
for n in numbers:
    if n % 2 == 1:
        squares_odd_numbers.append(n ** 2)

# implementare cu list comprehension:
[
    n ** 2
    for n in numbers
    if n % 2 == 1
]

# Exercițiu:
# având o listă de dicționare
people = [
  {'name': 'Jane', 'age': 25},
  {'name': 'John', 'age': 38},
  {'name': 'Andrew', 'age': 19},
  {'name': 'Georgia', 'age': 28},
  {'name': 'Lisa', 'age': 46},
  {'name': 'Carmen', 'age': 68},
  {'name': 'Thomas', 'age': 22},
  {'name': 'Bill', 'age': 31},
  {'name': 'Peter', 'age': 47},
  {'name': 'Stephen', 'age': 42},
]
# scrieți un one-liner ce calculează
# media de vârstă.
#
# luați în considerare că funcția sum rulează pe un iterabil

