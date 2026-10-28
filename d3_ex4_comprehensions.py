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