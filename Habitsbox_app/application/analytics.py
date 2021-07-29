import sqlite3
#import os
from datetime import datetime
from itertools import groupby
from functools import reduce
from collections import Counter
from operator import itemgetter

#from .habit import Habit
from .habit import Habit
#from . import Habit

class Analytics:
    """Initialize and manipulate SQLite3 database"""
    
    def __init__(self):
        """
        Connect to the database
        or create it if does not exist
        """
        try:
            # Connect to database
            self.connection = sqlite3.connect('DB_Habitsbox_app.db')
            # Create a cursor
            self.cursor = self.connection.cursor()
            # Create table habits with six columns if does not exist
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS habits(
                             HabitID INTEGER PRIMARY KEY, 
                             Name TEXT UNIQUE,
                             Periodicity TEXT,
                             Motivation TEXT,
                             Description TEXT,
                             Creation_date TEXT      
                          )""")
            # Create table trackings with four columns if does not exist
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS trackings(
                             TrackingID INTEGER PRIMARY KEY,
                             Date TEXT,
                             Time TEXT,
                             HabitID INTEGER NOT NULL,
                             FOREIGN KEY (HabitID) REFERENCES habits (HabitID)
                          )""")
        # print error if any error occurs  
        except sqlite3.Error as error:
            print('Error while connectiong to SQLite', error)
        
    def insert_habit(self, name, periodicity, motivation, description):
        """
        Initialize the Habit class in the habit module and 
        insert a habit to the DB
        """
        self.habit = Habit(name, periodicity, motivation, description)

        with self.connection:
            self.cursor.execute("""INSERT INTO habits (Name, Periodicity, Motivation, Description, Creation_date)
                            VALUES (:name, :periodicity, :motivation, :description, :creation_date)""", 
                            {'name': self.habit.name, 
                            'periodicity':self.habit.periodicity, 
                            'motivation':self.habit.motivation,
                            'description':self.habit.description,
                            'creation_date':self.habit.creation_date})
            
    def habits_table(self):
        """
        Return all the habits and all the fields
        available in the table habits in the DB.
        Example:
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Before lunch', '2021-04-26'), 
         (2, 'Run', 'weekly', 'Being healthier', 'At weekends', '2021-04-26')]
        """
        self.cursor.execute("SELECT * FROM habits")
        return self.cursor.fetchall()
    
    def trackings_table(self):
        """
        Returns the date and time when the trackings were
        registered, as well as to which habit-id they correspond.
        Example:        
        [(1, '2021-02-01', '19:52'), (2, '2021-02-03', '02:42')]
        """
        self.cursor.execute("""SELECT HabitID, Date, Time
                            FROM trackings""")
        return self.cursor.fetchall()
    
    def habits_trackings_table(self):
        """
        Join the habits table and the trackings table using the
        id of the habit.
        Example:
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-06-21', '09:06'), 
         (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-06-21', '15:26'), 
         (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-06-22', '16:00')]
        """
        self.cursor.execute("""SELECT h.HabitID, h.Name, h.Periodicity,
                            h.Motivation, h.Description, t.Date, t.Time
                            FROM habits h
                            JOIN trackings t
                            USING(HabitID)""")
        return self.cursor.fetchall()
    
    def select_column(self, table, i):
        """Select column i of the indicated table"""
        return list(map(lambda x: x[i], table))
    
    def select_columns(self, table, start=0, stop=1):
        """Select several columns of the indicated table"""
        return list(map(lambda x: x[start:stop], table))
    
    # def get_dates(self, trackings_table):
    #     return select_column(trackings_table, )
    
    # def get_all_names(self):
    #     """
    #     Return a list of habit names registered in the DB
    #     Example: ['Yoga', 'Run']
    #     """
    #     return list(self.select_column(self.habits_table(), 1))
        # ['Yoga']
        #return list(self.select_columns(self.habits_table(), 1, 2))
        # [('Yoga',)]
    
    def get_all_ids(self, table):
        """
        Return the first column of a table in a list
        """
        return list(self.select_column(table, 0))

    # def one_habit_info_by_id(self, table, id_n):
    #     """
    #     Select all rows with the corresponding id
    #     """
    #     return list(filter(lambda x: x[0]==id_n, table))
    
    # def habits_same_periodicity(self, table, periodicity):
    #     """
    #     Select all rows with the same periodicity
    #     """
    #     return list(filter(lambda x: x[2]==periodicity, table))
    
    def select_rows(self, table, number_column, feature):
        """
        Select all rows with the same feature
        """
        return list(filter(lambda x: x[number_column]==feature, table))
            
    def display_list_elements(self, my_list):
        return '\n'.join(map(str, my_list))
    
    def display_elements(self, my_list):
        return ', '.join(map(str, my_list))
    
    def unique_elements(self, table, column):
        return self.display_elements(
                self.unique_data(
                    self.select_column(
                        table, 
                        column)))

    def format_to_date(self, column):
        return map(lambda x: datetime.strptime(x, "%Y-%m-%d").date(), column)
    
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
        Same numbers are grouped and designed to a key.
        A new group is formed each time the number(key) changes.
        For example [1, 1, 1, 2, 1, 1, 2, 2] is grouped into
        [[1, [1, 1, 1]], [2, [2]], [1, [1, 1]], [2, [2, 2]]]
        """
        return groupby(differences)

    def streaks(self, grouping_differences):
        """
        Count the number of items contained in the group
        if the key is the number one
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
    
    def longest_streak_periodicity(self, trackings, periodicity, column):
        if len(trackings) == 0:
            return []
        else:
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
                                                    trackings,
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
                                                        trackings,
                                                        column))))))))))
    
    def start_habit(self, trackings, col_date):
        """
        Returns the earliest date from a column of dates
        """
        if len(trackings) == 0:
            return []
        else:
            return min(
                self.format_to_date(
                    self.select_column(trackings, col_date
                                   )))
    
    def last_day(self, trackings, col_date):
        if len(trackings) == 0:
            return []
        else:
            return max(
                self.format_to_date(
                    self.select_column(
                        trackings, col_date
                        )))
    
    def activity(self, periodicity, trackings, col_date):
        date_column = self.format_to_date(
            self.select_column(
                trackings, col_date))
        if periodicity == 'daily':
            return len(self.unique_data(date_column))
        elif periodicity == 'weekly':
            return len(self.unique_data(self.to_calender_week(date_column))) 
        
    def only_hours(self, time):
        """Get hours without minutes"""
        return map(lambda x: x.hour, time)

    def sort_hours(self, hours):
        """
        Each hour is renamed according to the part of the 
        day it corresponds to.
        Example: [3, 18, 19, 2] is 
        ['Overnight', 'Evening', 'Evening', 'Overnight']
        """
        return map(lambda x: 'Morning' 
                   if x >= 5 and x < 12 
                   else ('Afternoon'
                         if x >= 12 and x < 18
                         else ('Evening'
                               if x >= 18 and x < 24
                               else 'Overnight')), hours)

    def count_sorted_hours(self, sort_hours):
        """
        Count the number of times the words of the parts
        of the day appear.
        Example: ['Overnight', 'Evening', 'Evening', 'Overnight']
        is {'Evening': 2, 'Overnight': 2}
        """
        return Counter(sort_hours)

    def max_value(self, active_time_dict):
        """Get the maximum value of a dictionary"""
        if len(active_time_dict) == 0:
            return {}
        else:
            return max(active_time_dict.values())

    def most_active_time(self, active_time_dict, max_value):
        """
        Get the keys with the maximum value for example:
        ['Morning']
        """
        if len(active_time_dict) == 0:
            return {}
        else:
            return [k for k, v in active_time_dict.items() if v == max_value]
    
    def active_time_dict(self, trackings, col_time):
        return self.count_sorted_hours(
            self.sort_hours(
                self.only_hours(
                    self.format_to_time(
                        self.select_column(
                            trackings, col_time)))))
    
    def unique_ids_periodicity(self, table, col_periodicity, periodicity):
        """
        Gets the ids of the habits with the same periodicity
        """
        return self.unique_data(
            self.get_all_ids(
                self.select_rows(table, col_periodicity, periodicity)))
    
    def list_habits_list(self,habits_trackings, unique_ids):
        """
        Give a list of the lists of habits grouped by id
        """
        return [self.select_rows(habits_trackings, 0, id_n) for id_n in unique_ids]
    
    def lists_periodicity(self, table, col_periodicity, periodicity):
        """
        Give a list of the lists of habits grouped by id
        with the same periodicity
        """
        return self.list_habits_list(table, 
                                     self.unique_ids_periodicity(table, 
                                                                 col_periodicity, 
                                                                 periodicity))
    
    # def colnames_in_list(self, colnames):
    #     return [colnames]
    
    # def add_colnames(self, colnames, table):
    #     """Add the name of the columns"""
    #     return self.colnames_in_list(colnames)+table  
    

       
    def periodicity_info(self, lists_periodicity, periodicity, col_date=5):
        """
        A list containing information for each habit according 
        to its periodicity. Name of the habit, first and last tracking,
        most active time, activity days or weeks, and longest streak
        Example: [('Yoga', '2021-03-18', '2021-04-17', 'Evening', 5, 2),
                  ('Reading', '2021-03-19', '2021-04-25', 'Afternoon', 8, 2)]
        """
        habits_info = []
        
        for l in lists_periodicity:
            
            active_time_dictionary = self.active_time_dict(
                                l, 
                                6)  
            max_value_active_time = self.max_value(
                                active_time_dictionary)
            most_active_time = self.most_active_time(
                                active_time_dictionary, 
                                max_value_active_time)
                        
            habits_info.append((self.unique_elements(l, 1),
                  ''.join(min(self.select_column(l, col_date))),
                  ''.join(max(self.select_column(l, col_date))),
                  self.display_elements(most_active_time), 
                  self.activity(
                      periodicity, 
                      l, 
                      col_date),
                  self.longest_streak_periodicity(
                      l, 
                      periodicity, 
                      col_date)))
            
        return habits_info
    
    # def max_streak(self, data, periodicity):
    #     return max(
    #         self.periodicity_info(
    #             self.lists_periodicity(data,
    #                                    periodicity),
    #             periodicity),
    #         key=itemgetter(-1))[-1]

    def lengths(self, data):
        """
        A list of lists with the lengths of each element
        Example: [[1, 4, 5, 16, 16, 10], [1, 3, 5, 10, 11, 10]]
        """
        return [[len(str(x)) for x in row] for row in data]

    def max_lengths(self, lengths, data):
        """
        Lists are compared and the largest number from index i
        is picked.
        Example: From these three lists
        [[1, 4, 5, 16, 25, 10], [1, 4, 5, 20, 10, 10], [1, 3, 6, 9, 11, 10]]
        the following list is formed [1, 4, 6, 20, 25, 10] which contains
        the largest numbers in each index.
        """
        return list(max(map(itemgetter(x), lengths)) for x in range(0, len(data[0])))
    
    def distance_format(self, max_lengths):
        """
        Use the list with maximum lenghts to create a string formating.
        Example: 
        if max_lengths = [1, 4, 6, 20, 25, 10]
        "%-1s    %-4s    %-6s    %-20s    %-25s    %-10s    "   
        """
        return ''.join(map(lambda x: '%%-%ss    ' % x, max_lengths))
    
    def aligned_columns(self, format_distance, data):
        """
        Table data are aligned using the maximum length per column.
        Example: 
        ['1    Yoga    daily    Be more flexible    Before breakfast    2021-02-22    ', 
         '2    Run     daily    Be healthy          At weekends         2021-02-22    ']
        """
        return map(lambda x: format_distance % x, data)
    
    def line(self, max_lengths):
        """
        Creates a line with the length of the maximum lengths
        """
        return '_' * (sum(max_lengths) + len(max_lengths) * 4 - 3)
    
    def add_colnames(self, colnames, table):
        """
        Receives the column names in a tuple and
        adds them to the data
        """
        return [colnames]+table
    
    def display_table(self, data, title):
        """
        Display the data in a table
        """
        print(self.line(self.max_lengths(
            self.lengths(data), data)))
        print("{}".format(title))
        print(self.line(self.max_lengths(
            self.lengths(data), data)))
        print(self.display_list_elements(
            self.aligned_columns(
                self.distance_format(self.max_lengths(
                    self.lengths(
                        data), 
                    data)), 
                data)))
        print(self.line(self.max_lengths(
            self.lengths(data), data)))
         
    def table_header(self, colnames, data, header):
        """
        Displays a table with header and column names
        """
        return self.display_table(
            self.add_colnames(colnames,data), 
            header)
   
    def table_registered_habits(self):
        """
        Displays the names and ids of the registered habits
        in table format. The table has a title and the name
        of the columns.
        """        
        self.table_header(
            ('ID', 'HABIT'), 
            list(self.select_columns(
                self.habits_table(), 
                stop=2)), 'YOUR HABIT(S)')
   
    def remove_habit(self, name):
        """
        The habit is removed from the DB in the habit table along
        with all trackings related to its id.
        """
        with self.connection:
            self.cursor.execute("SELECT HabitID FROM habits WHERE Name=:name", 
                       {'name': name})
            id_habit = self.cursor.fetchone()[0]
            self.cursor.execute("DELETE from trackings WHERE HabitID = :habitID",
                             {'habitID': id_habit})
            self.cursor.execute("DELETE from habits WHERE HabitID = :habitID",
                             {'habitID': id_habit})
            
    def insert_day(self, id_habit):
        """
        Registers in the trackings table the day and time
        when the user checks a habit off, i.e. chooses
        the id of the habit.
        """
        
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M")

        with self.connection:
            self.cursor.execute("""INSERT INTO trackings (Date, Time, HabitID)
                                VALUES (:date, :time, :habitID)""", 
                            {'date': date, 'time': time, 'habitID': id_habit})

###No  in use__________________________________
#     def update_motivation(self, habit, new_mot):
#         with self.connection:
#             self.cursor.execute("""UPDATE habits SET motivation = :new_mot
#                            WHERE name = :name AND periodicity = :periodicity""",
#                            {'name': habit.name, 
#                             'periodicity': habit.periodicity, 
#                             'new_mot': new_mot})

# ###No  in use__________________________________
#     def get_trackings_by_id(self, id_habit):
#         self.cursor.execute("SELECT * FROM trackings WHERE id_habit=:id_habit",
#                         {'id_habit': id_habit})
#         return self.cursor.fetchall()
# ###No  in use__________________________________
 
#     def remove_day(self, day):
#         with self.connection:
#             self.cursor.execute("""DELETE from trackings 
#                             WHERE id_habit = :id_habit AND date_time = :date_time""",
#                   {'id_habit': day.id_habit, 'date_time': day.date_time})
# ###____________________________________________
    
    # def clear_console(self):
    #     return lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    
    # def clear_console(self):
    #     command = 'clear'
    #     if os.name in ('nt', 'dos'):
    #         print('hola')
    #         command = 'cls'
    #     os.system(command)
    #     print(command)
       
    
    def clear_console(self):
        """
        Print several new lines to clean up the console
        """
        print('\n' * 200)
    
    
    def close(self):
        """Close sqlite3 connection"""
        self.connection.close()
