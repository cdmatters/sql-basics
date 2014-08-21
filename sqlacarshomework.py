import sqlite3

connected_data = sqlite3.connect("cars.db")

cursor = connected_data.cursor()

cursor.execute("""CREATE TABLE cars 
                (make TEXT, model TEXT, quantity INT)
                """)

connected_data.close()