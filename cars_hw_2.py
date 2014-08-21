# importing database entries then updating them. Homework on pg71.

import sqlite3

with sqlite3.connect("cars.db") as connection:

    c = connection.cursor()

    car_data = [
                ('Honda', 'Einstein', 1000),
                ('Ford', 'Lavoisier', 50),
                ('Honda', 'Eddington', 890),
                ('Ford', 'Mendeleev', 400),
                ('Ford', 'Gibbs', 120)
                ]

    # TO AVOID REENTRIES AFTER FIRST TIME
    #  c.executemany("INSERT INTO cars VALUES(?, ?, ?)", car_data)

    c.execute("UPDATE cars SET quantity = 900 WHERE model = 'Einstein'")
    c.execute("UPDATE cars SET quantity = 500 WHERE model = 'Lavoisier'")

    for r in c.execute("SELECT * FROM cars"):
        print r[0], r[1], r[2]

    c.execute("SELECT model, quantity FROM cars WHERE make = 'Ford'")
    found_Ford = c.fetchall()

    for r in found_Ford:
        print r[0], r[1]
