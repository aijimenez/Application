import sqlite3

try:
    # Connect to database
    connection = sqlite3.connect('DB_Habitsbox_app.db')
    #conn = sqlite3.connect(':memory:')
    
    # Create a cursor
    c = connection.cursor()
    print('Connected to SQLite')

    # Create table habits with six columns if does not exist
    c.execute("""CREATE TABLE IF NOT EXISTS habits(
            HabitID INTEGER PRIMARY KEY, 
            Name TEXT UNIQUE,
            Periodicity TEXT,
            Motivation TEXT,
            Description TEXT,
            Creation_date TEXT      
        )""")
    
    # Create table trackings with four columns if does not exist
    c.execute("""CREATE TABLE IF NOT EXISTS trackings(
            TrackingID INTEGER PRIMARY KEY,
            Date TEXT,
            Time TEXT,
            HabitID INTEGER NOT NULL,
            FOREIGN KEY (HabitID) REFERENCES habits (HabitID)
        )""")
    
    print('tables habits and trackings are succesfully created')
        
    # close the cursor
    c.close()
    
# print error if any error occurs    
except sqlite3.Error as error:
    print('Error when using SQLite', error)
     
# close connection
finally:
    if (connection):
        connection.close()
        print('SQLite connection is closed')
