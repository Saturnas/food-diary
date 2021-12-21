import sqlite3

with sqlite3.connect("food.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Foods(
Data text PRIMARY KEY,
Breakfast text,
Dinner text,
Supper text,
Snacks text,
Calories real,
Weight real,
Exercises text,
Comment text);""")

db.close()