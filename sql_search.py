# this is a way of exploring the SELECT statement
#UPDATE this includes a n exploration of UPDATE and DELETE statements


import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # update data 
    c.execute("UPDATE population \
        SET population = 9000000 WHERE city = 'New York City'")

    #delete data
    c.execute("DELETE FROM population WHERE city = 'Boston'")

    print "\nNEW DATA:\n"

    c.execute("SELECT * FROM population")

    total_row = c.fetchall()

    for r in total_row:
        print r[0], r[1], r[2]


    # use for loop to iterate through the database printing results line by line
    for row in c.execute("SELECT city, state, population from population"):
        print row

    #  use SELECT to get the data, then fetchall() to retrieve records from query
    # fetchall() r all records from query and stored them as a tuple of tuples
    c.execute("SELECT city, population from population")
    some_data = c.fetchall()

    for r in some_data:
            print r[0], r[1]

