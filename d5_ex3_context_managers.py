# așa făceam lucrurile pe vremuri

def mywriter():
    fp = open("test.txt", 'w')

    try:
        fp.write("something")
        # do_stuff()
        1 / 0
    finally:
        print("o să închid fp-ul")
        fp.close()


# s-a inventat context manager-ul.
# un context manager oferă garanția
# faptului că se rulează anumite operațiuni
# la intrarea în context, adică __enter__
# și că se rulează anumite operațiuni
# la ieșirea din context, adică __exit__
# chiar dacă a existat o excepție


with open("f.txt", 'w') as f:
    f.write("chestii")
# garantează că f își rulează singur f.close()
