import sqlite3 as sql
qiymat1 = sql.connect("susy.db")
qiymat2 = qiymat1.cursor()
qiymat2.execute("""
    CREATE TABLE IF NOT EXISTS Malumots(
        ism TEXT
        yosh INTEGER
        vazn INTEGER
    )
""")