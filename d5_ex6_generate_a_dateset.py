# Task:
# Creați un fișier "test-dataset.csv"

# cu coloanele
# ID, Nume, Adresă, Telefon, E-mail

# populați acest fișier cu 1000 de row-uri
# folosind library-ul faker

# folosiți faker.Faker(locale="ro")
# folosiți csv.writer()

import csv
import faker

fake = faker.Faker(locale="ro")
with open("test-dataset.csv", 'w', encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow((
        'ID', 'Nume', 'Adresă', 'Telefon', 'E-mail'
    ))

    for id in range(1000):
        writer.writerow((
            id,
            fake.name(),
            fake.address(),
            fake.phone_number(),
            fake.email(),
        ))



