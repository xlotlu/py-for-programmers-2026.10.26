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

# ce preferați? list comprehension sau map?


ages = [  p['age'] for p in people  ]

print(sum(ages) / len(ages))


# dacă problema era să calculați și media, și minimul și maximul
# vârstelor?
print(min(ages), max(ages))


# dar dacă cerința era să faceți asta într-o singură iterație?
# (adică fără listă intermediară?)

# nu mai putem folosi list comprehension

# scriem o funcție
the_min = 0
the_max = 0
the_total = 0

for p in people:
    age = p['age']

    if age > the_max:
        the_max = age

    if age < the_min:
        the_min = age

    the_total += age

print(
    the_total / len(people),
    the_min,
    the_max
)