import sqlite3

connection = sqlite3.connect("crime.db", check_same_thread=False)

connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.cursor()



# Case Database
cursor.execute("""

CREATE TABLE IF NOT EXISTS cases(
id integer primary key autoincrement,
title TEXT NOT NULL,
victim_name TEXT NOT NULL,
crime_type TEXT NOT NULL)
""")

#Suspect Database
cursor.execute("""

CREATE TABLE IF NOT EXISTS suspects(
    id integer primary key autoincrement,
    case_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    motive TEXT NOT NULL,
    alibi TEXT NOT NULL, 
    FOREIGN KEY(case_id)REFERENCES cases(id)
    ON DELETE CASCADE)""")

#Witness Database
cursor.execute("""

CREATE TABLE IF NOT EXISTS witnesses(
    id integer primary key autoincrement,
    case_id INTEGER NOT NULL,
    name TEXT  NOT NULL,
    statement TEXT NOT NULL,
    FOREIGN KEY(case_id) REFERENCES cases(id)
    ON DELETE CASCADE)""")

#Evidence Database
cursor.execute("""
CREATE TABLE IF NOT EXISTS evidence(
id integer primary key autoincrement,
case_id INTEGER NOT NULL,
evidence TEXT NOT NULL,
evidence_status TEXT NOT NULL,
FOREIGN KEY(case_id) REFERENCES cases(id)
ON DELETE CASCADE)""")


connection.commit()