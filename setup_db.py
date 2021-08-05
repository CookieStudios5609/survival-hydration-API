import sqlite3
from sqlite3 import Error


def make_db():
    try:
        conn = sqlite3.connect("api/water.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS watersupply (liters INTEGER, weight INTEGER, days INTEGER);")
        conn.commit()
        cursor.execute("INSERT INTO watersupply(liters, weight, days) VALUES(1, 100, 0)")
        conn.commit()
        cursor.execute("SELECT * FROM watersupply")
        p = cursor.fetchone()
        print(f"{p[0]} liters, {p[1]} pounds, {p[2]} days")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


make_db()
