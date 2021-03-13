
import sqlite3

conn = sqlite3.connect('DB_Habitsbox_app.db')
#conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE habits(
            HabitID INTEGER PRIMARY KEY, 
            Name TEXT UNIQUE,
            Periodicity TEXT,
            Motivation TEXT,
            Description TEXT,
            Creation_date TEXT      
            )""")

c.execute("""CREATE TABLE trackings(
            TrackingID INTEGER PRIMARY KEY,
            Date TEXT,
            Time TEXT,
            HabitID INTEGER NOT NULL,
            FOREIGN KEY (HabitID) REFERENCES habits (HabitID)
            )""")

conn.close()