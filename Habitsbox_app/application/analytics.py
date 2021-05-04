import sqlite3
#import os
from datetime import datetime
from itertools import groupby
from functools import reduce
from collections import Counter
from operator import itemgetter

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
            
    def habits_table(self):
        """
        Return all the habits and all the fields
        available in the table habits in the DB
        example:
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Before breakfast', '2021-02-22')]
        """
        self.cursor.execute("SELECT * FROM habits")
        return self.cursor.fetchall()
    
    def trackings_table(self):
        self.cursor.execute("""SELECT HabitID, Date, Time
                            FROM trackings""")
        return self.cursor.fetchall()
    
    def habits_trackings(self):
        self.cursor.execute("""SELECT h.HabitID, h.Name, h.Periodicity,
                            h.Motivation, h.Description, t.Date, t.Time
                            FROM habits h
                            JOIN trackings t
                            USING(HabitID)""")
        return self.cursor.fetchall()
    
    def select_column(self, table, i):
        return map(lambda x: x[i], table)
    
    def select_columns(self, table, start=0, stop=1):
        return map(lambda x: x[start:stop], table)
    
    # def get_dates(self, trackings_table):
    #     return select_column(trackings_table, )
    
    def get_all_names(self):
        """
        Return the names of the habits in a list
        Example: ['Yoga', 'Run']
        """
        return list(self.select_column(self.habits_table(), 1))
    
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
    
    def display_unique_elements_of_column(self, table, column):
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
    
    def start_habit(self, trackings, column):
        if len(trackings) == 0:
            return []
        else:
            return min(
                self.format_to_date(
                    self.select_column(trackings, column
                                   )))
    
    def last_day(self, trackings, column):
        if len(trackings) == 0:
            return []
        else:
            return max(
                self.format_to_date(
                    self.select_column(
                        trackings, column
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
        Classification of hours in
        Morning, Afternoon, Evening and Overnight
        """
        return map(lambda x: 'Morning' 
                   if x >= 5 and x < 12 
                   else ('Afternoon'
                         if x >= 12 and x < 18
                         else ('Evening'
                               if x >= 18 and x < 24
                               else 'Overnight')), hours)

    def count_sorted_hours(self, sort_hours):
        """Create a dictionary of the form:
           {'Morning': 9, 'Afternoon': 5, 'Evening': 4, 'Overnight': 2}
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
    
    def list_habits_list(self,habits_trackings, unique_ids):
        """
        Give a list of the lists of habits grouped by id
        """
        return [self.select_rows(habits_trackings, 0, id_n) for id_n in unique_ids]
    
    def lists_periodicity(self, table, periodicity):
        """
        Give a list of the lists of habits grouped by id
        and with the same periodicity
        """
        return self.list_habits_list(table,
                                     self.unique_data(
                                         self.get_all_ids(
                                             self.select_rows(table, 2, periodicity))))
    
    def header_in_list(self, header):
        return [header]

    def add_header(self, header, table):
        return self.header_in_list(header)+table    
        
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
                        
            habits_info.append((self.display_unique_elements_of_column(l, 1),
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
    
    def max_streak(self, data, periodicity):
        return max(
            self.periodicity_info(
                self.lists_periodicity(data,
                                       periodicity),
                periodicity),
            key=itemgetter(-1))[-1]

    def lengths(self, data):
        """
        A list of lists with the lengths of each element
        Example: [[1, 4, 5, 16, 16, 10], [1, 3, 5, 10, 11, 10]]
        """
        return [[len(str(x)) for x in row] for row in data]

    def max_lengths(self, lengths, data):
        """
        Choose the list whith the maximum of the lengths
        Example: [1, 4, 5, 16, 16, 10]
        """
        return list(max(map(itemgetter(x), lengths)) for x in range(0, len(data[0])))
    
    def distance_format(self, max_lengths):
        """
        Use the list with maximum lenghts to create the following
        format: %-1s   %-4s   %-5s   %-16s   %-16s   %-10s   
        """
        return ''.join(map(lambda x: '%%-%ss    ' % x, max_lengths))
    
    def list_including_distances(self, format_distance, data):
        """
        anteriormente display_table
        A list of strings with the appropriate distances
        Example: ['1    Yoga    daily    Be more flexible    Before breakfast    2021-02-22    ', 
                  '2    Run     daily    Be healthy          At weekends         2021-02-22    ']
        """
        return map(lambda x: format_distance % x, data)
    
    def line(self, max_lengths):
        """
        Creates a line with the length of the maximum lengths
        """
        return '_' * (sum(max_lengths) + len(max_lengths) * 3 + 3)
    
    def display_table(self, data, title):
        """
        Display a table and 
        """
        print(self.line(self.max_lengths(
            self.lengths(data), data)))
        print("{}".format(title))
        print(self.line(self.max_lengths(
            self.lengths(data), data)))
        print(self.display_list_elements(
            self.list_including_distances(
                self.distance_format(self.max_lengths(
                    self.lengths(
                        data), 
                    data)), 
                data)))
        print(self.line(self.max_lengths(
            self.lengths(data), data)))
        
    def table_header(self, header, data, title):
        """
        Display a table with header
        """
        return self.display_table(
            self.add_header(header,data), 
            title)
   
    def table_registered_habits(self):
        """
        Display table with header of registered habits,
        it includes the id and the name of the habit
        """        
        self.table_header(
            ('ID', 'HABIT'), 
            list(self.select_columns(
                self.habits_table(), 
                stop=2)), 'REGISTERED HABITS')
   
    def remove_habit(self, name):
        with self.connection:
            self.cursor.execute("SELECT HabitID FROM habits WHERE Name=:name", 
                       {'name': name})
            id_habit = self.cursor.fetchone()[0]
            self.cursor.execute("DELETE from trackings WHERE HAbitID = :habitID",
                             {'habitID': id_habit})
            self.cursor.execute("DELETE from habits WHERE HAbitID = :habitID",
                             {'habitID': id_habit})
            
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
        print('\n' * 200)
    
    
    def __del__(self):
        self.connection.close()

