import sqlite3
from sqlite3 import Error


def make_db():
    try:
        conn = sqlite3.connect("api/water.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS watersupply (liters INTEGER PRIMARY KEY);")
        conn.commit()
        cursor.execute("INSERT INTO watersupply(liters) VALUES(1)")
        conn.commit()
        cursor.execute("SELECT * FROM watersupply")
        p = cursor.fetchone()
        print(p[0])
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


make_db()