import sqlite3 as sq

with sq.connect("database.db") as con:
    cur=con.cursor()

    cur.execute("DROP TABLE IF EXISTS group1")
    cur.execute("""CREATE TABLE IF NOT EXISTS groups_uni (
    group_id INTEGER PRIMARY KEY,
    groups_uni CHAR
    )
    """)

    cur.execute("DROP TABLE IF EXISTS days")
    cur.execute("""CREATE TABLE IF NOT EXISTS days (
    day_id INTEGER PRIMARY KEY,
    day CHAR
    )
    """)
    
    cur.execute("DROP TABLE IF EXISTS week")
    cur.execute("""CREATE TABLE IF NOT EXISTS week (
    week_id INTEGER PRIMARY KEY,
    week CHAR
    )
    """)

    cur.execute("DROP TABLE IF EXISTS object")
    cur.execute("""CREATE TABLE IF NOT EXISTS object (
    group_id INTEGER,
    week_id INTEGER,
    day_id INTEGER,
    para_id TEXT,
    time_id TEXT,
    object TEXT,
    people TEXT,
    kabinet CHAR
    )
    """)

