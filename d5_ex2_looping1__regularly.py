import csv
from datetime import time

from time import sleep

def parse_temps(csvfile):
    out = []

    with open(csvfile, encoding="utf-8") as f:
        reader = csv.reader(f)
        for tstamp, value in enumerate(reader):
            # let's introduce some artificial delay
            sleep(.00001)

            tstamp = time.strptime(tstamp, "%H:%M:%S")
            value = float(value)

            out.append((tstamp, value))

    return out


def process_temps(dataset):
    results = []

    prev_hour = None

    total = 0
    count = 0

    for timestamp, temp in dataset:
        hour = timestamp.hour

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


def runit():
    CSV_FILE = 'data/temp_sensor_data.csv'
    for el in process_temps(parse_temps(CSV_FILE)):
        print(el)