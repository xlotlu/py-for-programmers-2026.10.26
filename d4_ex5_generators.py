# generatorul este un caz special de iterator

def myfunc():
    print("am intrat în funcție")
    yield 23
    print("după primul yield")
    yield 34
    print("după al doilea yield")
    yield 45
    print("ies din funcție")

# iterat:
genobj = myfunc()
for elem in genobj:
    print(elem)

# item by item
genobj = myfunc()
next(genobj)
next(genobj)
next(genobj)
try:
    next(genobj)
except StopIteration:
    print("succes, am consumat tot!")

# concretizat
list( myfunc() )


# Exercițiu:
# dat fiind fișierul data/temp_sensor_data.csv
#
# calculați media orară a temperaturilor.
#
# inițial scrieți o funcție ce returnează o listă
# cu mediile, lista să fie de forma (hour, average):
[
    (7, 20),
    (8, 22),
    (9, 24)
]

CSVFILE = "data/temp_sensor_data.csv"

def process_temps(csvfile):
    pass

    # strategie:
    # 1. iterăm line by line
    # 2. extragem ora și temperatura
    # 3. dacă se schimbă ora trebuie să
    #    calculăm media celor din listă


    # dicționar:
    # cheie ora, valoare = lista de temperaturi

    # {
    #    7: [19.0, 20.0, 21.0],
    #    8: [...]
    # }

from collections import defaultdict

def process_temps(csvfile):
    with open(csvfile) as f:
        temps = defaultdict(list)

        for line in f:
            tstamp, value = line.removesuffix("\n").split(',')
            hour, minute, second = tstamp.split(':')

            hour = int(hour)
            value = float(value)

            temps[hour].append(value)

    return [
        (hour, sum(values) / len(values))
        for hour, values in temps.items()
    ]

print(process_temps(CSVFILE))


def process_temps(csvfile):
    results = []

    prev_hour = None

    total = 0
    count = 0

    with open(csvfile, encoding="utf-8") as f:
        for line in f:
            timestamp, temp = line.split(",")
            hour = int(timestamp[:2])
            temp = float(temp)

            if prev_hour is None:
                prev_hour = hour

            if hour == prev_hour:
                total += temp
                count += 1
                continue

            # if we got here, this is the next hour.
            # we will append previous hour's average

            results.append(
                (prev_hour, total / count)
            )
            # and reset the counter and total

            total = temp
            count = 1

            prev_hour = hour

    # don't forget to process the final hour
    if count:
        results.append(
            (prev_hour, total / count)
        )

    return results
