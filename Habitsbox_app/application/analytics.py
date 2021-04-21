import sqlite3
from datetime import datetime
from itertools import groupby
from functools import reduce
from collections import Counter

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
        self.cursor.execute("""SELECT t.HabitID, t.Date, t.Time 
                            FROM habits h 
                            INNER JOIN trackings t 
                            USING(HabitID)""")
        return self.cursor.fetchall()
    
    def format_to_date_time(self, trackings):
        """
        Convert strings into datetime format
        """
        return map(lambda x: (datetime.strptime(x[0], "%Y-%m-%d"), 
               datetime.strptime(x[1], "%H:%M").time()),
               trackings)


    def select_column(self, list_date_time, i):
        return map(lambda x: x[i], list_date_time)
    
    def format_to_date(self, column):
        return map(lambda x: datetime.strptime(x, "%Y-%m-%d"), column)
    
    def format_to_time(self, column):
        return map(lambda x: datetime.strptime(x, "%H:%M").time(), column)
           
    def to_calender_week(self, dates):
        return map(lambda x: x.isocalendar()[1], dates)
    
    def unique_data(self, myobject):
        return reduce(lambda x, y: x + [y] if y not in x else x, myobject, [])
    
    def zipping_unique_data(self, unique):
        """
        Create a sequence of pairs from a list of dates that are unique
        """
        return zip(unique[1:], unique[:-1])

    def differences(self, pairs):
        """
        Difference of days between trackings 
        """
        return map(lambda x: (x[0]-x[1]), pairs) 
    
    def difference_in_days(self, differences):
        return map(lambda x: x.days, differences)

    def cw_5152_to_1(self, differences):
        return map(lambda x: 1 
                   if (x == -51) or (x == -52) 
                   else x, differences)

    def grouping_differences(self, differences):
        """
        Group by nummer (key) and members. Example: nummer: [item1, item2]
        [(2, 2), (1, 2), (2, 1), (1, 3), (7, 1), (1, 2), (2, 1), (1, 2)]
        """
        return groupby(differences)

    def streaks(self, grouping_differences):
        """
        Count the number of items if the key is the number one
        """
        return [sum(group) for key, group in grouping_differences if key == 1]

    def longest_streak(self, streaks):
        """
        Select the longest streak if the list given is not empty,
        if the list is empty gives a default value of 1
        """
        if len(streaks) != 0:
            return max(streaks) + 1
        else:
            return 1
    
    def longest_streak_periodicity(self, periodicity, column):
        if periodicity == 'daily':
            return self.longest_streak(
                self.streaks(
                    self.grouping_differences(
                        self.difference_in_days(
                            self.differences(
                                self.zipping_unique_data(
                                    self.unique_data(
                                        self.format_to_date(
                                            self.select_column(
                                                self.joint_habits_trackings(), 
                                                column)))))))))
        elif periodicity == 'weekly':
            return self.longest_streak(
                self.streaks(
                    self.grouping_differences(
                        self.cw_5152_to_1(
                            self.differences(
                                self.zipping_unique_data(
                                    self.unique_data(
                                        self.to_calender_week(
                                            self.format_to_date(
                                                self.select_column(
                                                    self.joint_habits_trackings(),
                                                    column))))))))))
    
    def start_habit(self, column=1):
        return min(
            self.format_to_date(
                self.select_column(self.joint_habits_trackings(), column
                                   )))
    
    def last_day(self, column):
        return max(
            self.format_to_date(
                self.select_column(
                    self.joint_habits_trackings(), column
                    )))
    
    def activity(self, unique_data):
        return len(unique_data)
        
    def info_one_habit(self):
        """Return the information of one habit"""
        all_habits_trackings = self.joint_habits_trackings()
        all_habits = self.get_all_habits()
        habit = all_habits[0][1]
        periodicity = all_habits[0][2]
        motivation = all_habits[0][3]
        registration_habit = all_habits[0][-1]
        start = self.start_habit()
        last = self.last_day(1)
        streak_daily = self.longest_streak_periodicity('daily', 1)
        streak_weekly = self.longest_streak_periodicity('weekly', 1)
        activity_daily = self.activity(
            self.unique_data(
                self.format_to_date(
                    self.select_column(
                        self.joint_habits_trackings(), 1))))
        activity_weekly = self.activity(
            self.unique_data(
                self.to_calender_week(
                    self.format_to_date(
                        self.select_column(
                            self.joint_habits_trackings(), 1))))) 


        if len(all_habits_trackings) == 0:
            #self.see_all_habits()
            #all_habits = self.get_all_habits()
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
            """.format(habit, registration_habit, motivation)
            )
        else:
            print(
                        """
                        ___________________________________
                                      - {} -
                        ___________________________________
                        Motivation:   {}
                        Periodicity:  {}
                        -----------------------------------
                        
                        Started on:             {}
                        Last day of activity:   {}
                        """.format(habit, motivation, 
                        periodicity, start, last)
                        )
            
            if len(all_habits_trackings) > 1:
                
                if periodicity == 'daily':
                    
                    print(
                        """
                        Longest streak: {}
                        Days of activity: {}
                        """.format(streak_daily, activity_daily)
                        )
                elif all_habits[0][2] == 'weekly':
                    print(
                        """
                        Longest streak: {}
                        Weeks of activity: {}
                        """.format(streak_weekly, activity_weekly)
                        )
            
                
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

