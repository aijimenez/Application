import sqlite3
from datetime import datetime

#from .habit import Habit
from habit import Habit

class Analytics:
    """Initialize and manipulate SQLite3 database"""
    
    def __init__(self):
        """Connect to the database"""
        self.connection = sqlite3.connect('DB_Habitsbox_app.db')
        self.cursor = self.connection.cursor()
        
    def insert_habit(self, name, periodicity, motivation, description):
        """Initialize the Habit class in the habit module"""
        self.habit = Habit(name, periodicity, motivation, description)
        """Insert a habit to the DB"""
        with self.connection:
            self.cursor.execute("""INSERT INTO habits (Name, Periodicity, Motivation, Description, Creation_date)
                            VALUES (:name, :periodicity, :motivation, :description, :creation_date)""", 
                            {'name': self.habit.name, 
                            'periodicity':self.habit.periodicity, 
                            'motivation':self.habit.motivation,
                            'description':self.habit.description,
                            'creation_date':self.habit.creation_date})
            
    def get_all_habits(self):
        """Return all the habits and all the fields
        available in the table habits in the DB"""
        self.cursor.execute("SELECT * FROM habits")
        return self.cursor.fetchall()
    
    def get_all_names(self):
        """Return the names of the habits in a list"""
        all_habits = self.get_all_habits()
        if len(all_habits) >= 1:
            return [habit[1] for habit in all_habits]
        else:
            return []

    def get_all_ids(self):
        """Return the ids of the habits in a list"""
        all_habits = self.get_all_habits()
        return [habit[0] for habit in all_habits]
                                     
    def see_all_habits(self):
        """Print a table with all habits and
        its fields"""
        all_habits = self.get_all_habits()
        if len(all_habits) >= 1:
            print('-' * 50)
            print('ID'.center(2) + 'HABIT'.center(15) + 'PERIODICITY'.center(15) + 'MOTIVATION'.center(15))
            print('-' * 50)
            for habit in all_habits:
                print(str(habit[0]).ljust(6) + str(habit[1]).ljust(15) + str(habit[2]).ljust(15)+ str(habit[3]))
                        
    def get_habit_by_id(self, id_n):
        self.cursor.execute("SELECT * FROM habits WHERE HabitID=:habitID", 
                       {'habitID': id_n})
        one_habit = self.cursor.fetchone()
        print('\n')
        print('-' * 50)
        print('HABIT'.ljust(16) + 'PERIODICITY'.ljust(18) + 'MOTIVATION')
        print('-' * 50)
        print(one_habit[1] + ' ✔'.ljust(12) + one_habit[2].ljust(18) + one_habit[3])
        
    
    def get_habits_by_name(self, name):
        self.cursor.execute("SELECT * FROM habits WHERE name=:name", 
                       {'name': name})
        one_habit = self.cursor.fetchone()
        print('-' * 45)
        print('HABIT'.ljust(30) + 'MOTIVATION')
        print('-' * 45)
        print(one_habit[1].ljust(30) + one_habit[3])
        print('\nStart:')
        print('Progress %')
        print('Days 12/30')
        print('Longest streak: 12 days')
        
    def join_tables(self, id_habit):
        self.cursor.execute("""SELECT * FROM habits h 
                                INNER JOIN trackings t 
                                ON h.id = t.id_habit
                                WHERE id_habit=:id_habit""",
                            {'id_habit': id_habit})
        return self.cursor.fetchall()
        # print('-' * 45)
        # print('HABIT'.ljust(30) + 'MOTIVATION')
        # print('-' * 45)
        # print(one_habit[2].ljust(30) + one_habit[4])
        # print('\nStart:')
        # print('Progress %')
        # print('Days 12/30')
        # print('Longest streak: 12 days')
        
    def joint_habits_trackings(self):
        self.cursor.execute("""SELECT t.Date FROM habits h 
                            INNER JOIN trackings t 
                            USING(HabitID)""")
        return self.cursor.fetchall()
        
    def info_one_habit(self):
        """Return the information of one habit"""
        all_habits_trackings = self.joint_habits_trackings()
        if len(all_habits_trackings) == 0:
            #self.see_all_habits()
            all_habits = self.get_all_habits()
            #print(all_habits)
            #[(1, 'Yoga', 'weekly', 'Be more flexible', 'Before breakfast', '2021-02-22')]
            print(
                """             
            ------------------------------------------------
                    ** Start now with {} **
                    and check it off as done
            ------------------------------------------------
                    
                    Registration date: {}
                    Motivation: {}
                    
            ------------------------------------------------
            """.format(all_habits[0][1], all_habits[0][-1], all_habits[0][3])
            )
        else:
        
           print(all_habits_trackings)
        #[(1, 'Yoga', 'weekly', 'Be more flexible', 'Before breakfast', '2021-02-22', 
        #1, '2021-02-24', '07:36 PM')]
        # if len(all_habits) == 1:
        #     for habit in all_habits:
        #         print(str(habit[0]).ljust(6) + str(habit[1]).ljust(15) + str(habit[2]).ljust(15)+ str(habit[3]))
        #     print('-' * 45)
        #     print('HABIT'.ljust(30) + 'MOTIVATION')
        #     print('-' * 45)
        #     print(all_habits[2].ljust(30) + all_habits[4])
        #     print('\nStart:')
        #     print('Progress %')
        #     print('Days 12/30')
        #     print('Longest streak: 12 days')
        
        



    # def joint_habits_trackings(self, name):
    #     self.cursor.execute("""SELECT * FROM habits h 
    #                         INNER JOIN trackings t 
    #                         ON h.HabitID = t.HabitID
    #                         WHERE Name=:name""",
    #                         {'name': name})
        
    #     print(self.cursor.fetchall())      
    
    def remove_habit(self, name):
        with self.connection:
            self.cursor.execute("SELECT HabitID FROM habits WHERE Name=:name", 
                       {'name': name})
            id_habit = self.cursor.fetchone()[0]
            self.cursor.execute("DELETE from trackings WHERE HAbitID = :habitID",
                             {'habitID': id_habit})
            self.cursor.execute("DELETE from habits WHERE HAbitID = :habitID",
                             {'habitID': id_habit})
            
            print('\nThe habit {} has been deleted.\n'.format(name))
            

         
    # def joint_habits_trackings(self, id_habit):
    #     self.cursor.execute("""SELECT * FROM habits h INNER JOIN trackings t ON h.HabitID = t.HabitID
    #                         WHERE habitID=:id_habit""",
    #                         {'habitID': id_habit})
        
    #     habits_trackings = self.cursor.fetchall()
    #     for habit in habits_trackings:
    #         print(str(habit[0]).ljust(6) + 
    #               habit[2].ljust(15) + habit[3].ljust(15) + habit[4])        
            
    
    # def get_habits_by_name(self, name):
    #     self.cursor.execute("SELECT * FROM habits WHERE name=:name", 
    #                    {'name': name})
    #     one_habit = self.cursor.fetchone()
    #     print('HABIT'.ljust(15) + 'PERIODICITY'.ljust(15) + 'MOTIVATION')
    #     print('-' * 45)
    #     print(one_habit[2].ljust(15) + one_habit[3].ljust(15) + one_habit[4])
        
    # def total_habits(self):
    #     self.cursor.execute("SELECT COUNT(*) FROM habits")
    #     return self.cursor.fetchone()[0]        
                      
    def update_motivation(self, habit, new_mot):
        with self.connection:
            self.cursor.execute("""UPDATE habits SET motivation = :new_mot
                           WHERE name = :name AND periodicity = :periodicity""",
                           {'name': habit.name, 
                            'periodicity': habit.periodicity, 
                            'new_mot': new_mot})
            
    def insert_day(self, id_habit):
        """Insert the day and time in the databank
        when a habit is checked-off"""
        
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M")

        with self.connection:
            self.cursor.execute("""INSERT INTO trackings (Date, Time, HabitID)
                                VALUES (:date, :time, :habitID)""", 
                            {'date': date, 'time': time, 'habitID': id_habit})
        

       


    def get_trackings_by_id(self, id_habit):
        self.cursor.execute("SELECT * FROM trackings WHERE id_habit=:id_habit",
                        {'id_habit': id_habit})
        return self.cursor.fetchall()
 
    def remove_day(self, day):
        with self.connection:
            self.cursor.execute("""DELETE from trackings 
                            WHERE id_habit = :id_habit AND date_time = :date_time""",
                  {'id_habit': day.id_habit, 'date_time': day.date_time})

    def __del__(self):
        self.connection.close()

