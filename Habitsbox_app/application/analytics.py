"""
This module contains methods that analyse the data
of the habits and trackings that the user has saved.
It also contains methods that have a connection to
the database.
"""
import sqlite3
from datetime import datetime
from itertools import groupby
from functools import reduce
from collections import Counter
from operator import itemgetter

from .habit import Habit

class Analytics:
    """Initialize and manipulate SQLite3 database"""

    def __init__(self):
        """
        Connect to the database
        or create it if does not exist.
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
        insert a habit to the DB.

        Parameters
        ----------
        name : str
            Name of the habit
        periodicity : str
            Periodicity of the habit, daily or weekly
        motivation :
            Motivation of the user to perform the habit
        description :
            Description of the habit
        """
        self.habit = Habit(name, periodicity, motivation, description)

        with self.connection:
            self.cursor.execute("""
                            INSERT INTO habits (Name,
                                                Periodicity,
                                                Motivation,
                                                Description,
                                                Creation_date)
                            VALUES (:name,
                                    :periodicity,
                                    :motivation,
                                    :description,
                                    :creation_date)""",
                            {'name': self.habit.name,
                            'periodicity':self.habit.periodicity,
                            'motivation':self.habit.motivation,
                            'description':self.habit.description,
                            'creation_date':self.habit.creation_date})

    def habits_table(self):
        """
        Return all the habits with its information contained in
        the table habits in the DB. ID and name of the habit,
        periodicity, motivation, description, and the day it was recorded.

        Example
        -------
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Before lunch', '2021-04-26'),
         (2, 'Run', 'weekly', 'Being healthier', 'At weekends', '2021-04-26')]
        """
        self.cursor.execute("SELECT * FROM habits")
        return self.cursor.fetchall()

    def trackings_table(self):
        """
        Return the date and time when the trackings were
        registered, as well as to which habit-id they correspond.

        Example
        -------
        [(1, '2021-02-01', '19:52'), (2, '2021-02-03', '02:42')]
        """
        self.cursor.execute("""SELECT HabitID, Date, Time
                            FROM trackings""")
        return self.cursor.fetchall()

    def habits_trackings_table(self):
        """
        Join the habits table and the trackings table using the
        id of the habit.

        Example
        -------
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-06-21', '09:06'),
         (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-06-21', '15:26')]
        """
        self.cursor.execute("""SELECT h.HabitID, h.Name, h.Periodicity,
                            h.Motivation, h.Description, t.Date, t.Time
                            FROM habits h
                            JOIN trackings t
                            USING(HabitID)""")
        return self.cursor.fetchall()

    def select_column(self, table, number_column):
        """
        Select a column of the indicated table.

        Parameters
        ----------
        table : list of tuples
            Name of the table
        num_col : int
            Index number, i.e. column

        Returns
        -------
        list
            a list with the selected column
        """
        return list(map(lambda x: x[number_column], table))

    def select_columns(self, table, start=0, stop=1):
        """
        Select several columns of the indicated table.

        Parameters
        ----------
        table : list of tuples
            Name of the table
        start : int, optinal
            Number of the first index (inclusive), i.e. column
            (default is 0)
        stop : int, optional
            Number of the last index (exclusive), i.e. column
            (default is 1)

        Returns
        -------
        list
            a list of tuples with selected columns
        """
        return list(map(lambda x: x[start:stop], table))

    def get_all_ids(self, table):
        """
        First column of a table in a list.

        Parameters
        ----------
        table : list of tuples
            Name of the table

        Returns
        -------
        list
            a list of numbers representing habit ids
        """
        return list(self.select_column(table, 0))

    def select_rows(self, table, number_column, feature):
        """
        Select all rows with the same feature.

        Parameters
        ----------
        table : list of tuples
            Name of the table
        number_column : int
            Index number, column where the criterion
            will be searched
        feature : int, str
            the criteria used for selection

        Returns
        -------
        list
            a list of tuples with all rows that
            satisfy the condition
        """
        return list(filter(lambda x: x[number_column]==feature, table))

    def display_elements(self, my_list, separator='\n'):
        """
        Each item in the list is separated by a separator.

        Parameters
        ----------
        my_list : list
            List of elements to be separated
        separator : str, optional
            (default is '\n')

        Returns
        -------
        str
            a string with elements separated by the separator
        """
        return separator.join(map(str, my_list))

    def unique_data(self, my_list):
        """
        Give unique values from a list of data.

        Parameters
        ----------
        my_list : list
            A list tha contains duplicate elements

        Returns
        -------
        list
            a list of unique elements
        """
        return reduce(lambda x, y: x + [y] if y not in x else x, my_list, [])

    def display_unique_elements(self, table, column):
        """
        Unique elements of a column are
        separated by commas in a string.

        Parameters
        ----------
        table : list of tuples
            Name of the table
        column : int
            Index number, i.e. column

        Returns
        -------
        str
            Elements separated by comma
        """
        return self.display_elements(
                self.unique_data(
                    self.select_column(
                        table,
                        column)), ', ')

    def format_to_date(self, column):
        """
        Items are converted to datetime.date.

        Parameters
        ----------
        column : list of tuples
            a list of strings containing the dates to
            be converted

        Returns
        -------
        iterator
            dates in datetime.date
        """
        return map(lambda x: datetime.strptime(x, "%Y-%m-%d").date(), column)

    def format_to_time(self, column):
        """
        Items are converted to datetime.time.

        Parameters
        ----------
        column : list of tuples
            a list of strings containing the times to
            be converted

        Returns
        -------
        iterator
            times in datetime.time
        """
        return map(lambda x: datetime.strptime(x, "%H:%M").time(), column)

    def to_calender_week(self, dates):
        """
        Give the calendar week number for each date.

        Parameters
        ----------
        dates : list
            a list of dates

        Returns
        -------
        iterator
            calendar week numbers
        """
        return map(lambda x: x.isocalendar()[1], dates)

    def zipping_unique_data(self, data):
        """
        A list is sliced into one list without the first element
        and into another list without the last element.
        The first elements of each list are matched in a tuple,
        then the second and so on.

        Parameters
        ----------
        data : list
            a list of dates or numbers

        Returns
        -------
        iterator
            pairs of numbers or dates

        Example
        -------
        [52, 1, 2, 3, 5] has the following result

        [(1, 52), (2, 1), (3, 2), (5, 3)]
        """
        return zip(data[1:], data[:-1])

    def differences(self, pairs):
        """
        Differences between numbers or dates.

        Parameters
        ----------
        pairs : list of tuples
            pairs of numbers or dates

        Returns
        -------
        iterator
            difference between the first element and the second

        Example
        -------
        [(1, 52), (2, 1), (5, 3)]

        results in [-51, 1, 2]
        """
        return map(lambda x: (x[0]-x[1]), pairs)

    def difference_in_days(self, differences):
        """
        Number of days from a datetime.timedelta object.

        Parameters
        ----------
        differences : list
            a list of datetime.timedelta elements

        Returns
        -------
        iterator
            number of days

        Example
        -------
        [timedelta(days=2), timedelta(days=1)]

        results in [2, 1]
        """
        return map(lambda x: x.days, differences)

    def cw_5152_to_1(self, differences):
        """
        Change the number to 1 if the number in the list
        is -51 o -52.

        Parameters
        ----------
        differences : list
            a list of numbers

        Returns
        -------
        iterator
            numbers representing calender week numbers
        """
        return map(lambda x: 1
                   if x in (-51, -52)
                   else x, differences)

    def grouping_differences(self, differences):
        """
        Same numbers are grouped and designed to a key.
        A new group is formed each time the number(key)
        changes.

        Parameters
        ----------
        differences : list
            a list of numbers

        Returns
        -------
        sub-iterators
            keys and groups from the list

        Example
        -------
        [1, 1, 1, 2, 1, 1, 2, 2] is grouped into

        [[1, [1, 1, 1]], [2, [2]], [1, [1, 1]], [2, [2, 2]]]
        """
        return groupby(differences)

    def streaks(self, grouping_differences):
        """
        Count the number of items contained in the group
        if the key is the number one.

        Parameters
        ----------
        grouping_differences : list
            a list of keys and groups

        Returns
        -------
        list
            a list of numbers

        Example
        -------
        [[1, [1, 1, 1]], [2, [2]], [1, [1, 1]], [2, [2, 2]]]

        results in [3, 2]
        """
        return [sum(group) for key, group in grouping_differences if key == 1]

    def longest_streak(self, streaks):
        """
        Give the maximum number in a list of numbers.
        If the list is empty, returns the number one.

        Parameters
        ----------
        streaks : list
            a list of numbers

        Returns
        -------
        int
            a number representing the longest streak
        """
        if len(streaks) != 0:
            return max(streaks) + 1
        return 1

    def longest_streak_periodicity(self, habits_trackings_table, periodicity, col_date=5):
        """
        The longest streak of a habit depending on
        the habit's periodicity.

        Parameters
        ----------
        habits_trackings_table : list of tuples
            a list with the information of the habits and
            its trackings
        periodicity : str
            periodicity of the habit, 'weekly' or 'daily'
        col_date : int
            index number i.e. column containing the dates
            (default is number 5)

        Returns
        -------
        int
            a number representing the longest streak of a
            habit
        """
        if len(habits_trackings_table) == 0:
            return []
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
                                                habits_trackings_table,
                                                col_date
                                                )))))))))
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
                                                habits_trackings_table,
                                                col_date
                                                ))))))))))

    def start_habit(self, habits_trackings_table, col_date = 5):
        """
        The earliest date from a column of dates.

        Parameters
        ----------
        habits_trackings_table : list of tuples
            a list with the information of the habits and
            its trackings
        col_date : int
            index number i.e. column containing the dates
            (default is number 5)

        Returns
        -------
        datetime.date
            The earliest date
        """
        if len(habits_trackings_table) == 0:
            return []
        return min(
            self.format_to_date(
                self.select_column(
                    habits_trackings_table,
                    col_date
                    )))

    def last_day(self, habits_trackings_table, col_date = 5):
        """
        The most recent date in a column of dates.

        Parameters
        ----------
        habits_trackings_table : list of tuples
            a list with the information of the habits and
            its trackings
        col_date : int
            index number i.e. column containing the dates
            ((default is number 5))

        Returns
        -------
        datetime.date
            The most recent date
        """
        if len(habits_trackings_table) == 0:
            return []
        return max(
            self.format_to_date(
                self.select_column(
                    habits_trackings_table,
                    col_date
                    )))

    def activity(self, periodicity, trackings, col_date=5):
        """
        Return the number of days or weeks in which the habit
        has been checked off, depending on whether the habit
        is weekly or daily.

        Parameters
        ----------
        periodicity : str
            periodicity of the habit, 'weekly' or 'daily'
        trackings : list of tuples
            a list with the information of the trackings
            registered for a certain habit
        col_date : int
            index number i.e. column containing the dates
            (default is number 5)

        Returns
        -------
        int
            number of days or weeks in which the habit
            has been checked off
        """
        date_column = self.format_to_date(
            self.select_column(
                trackings, col_date
                )
            )

        if periodicity == 'daily':
            return len(self.unique_data(date_column))
        return len(self.unique_data(self.to_calender_week(date_column)))

    def only_hours(self, time):
        """
        Get hours without minutes

        Parameters
        ----------
        time : list
            a list of times

        Returns
        -------
        iterator
            numbers representing the hours
        """
        return map(lambda x: x.hour, time)

    def sort_hours(self, hours):
        """
        Each hour is renamed according to the part of the
        day it corresponds to (Morning, Afternoon, Evening
        or Overnight).

        Parameters
        ----------
        hours : list
            a list of numbers representing the hours

        Returns
        -------
        iterator
            parts of the day in strings

        Example
        -------
        [3, 18, 19, 2] results in

        ['Overnight', 'Evening', 'Evening', 'Overnight']
        """
        return map(lambda x: 'Morning'
                   if 5 <= x < 12
                   else ('Afternoon'
                         if 12 <= x < 18
                         else ('Evening'
                               if 18 <= x < 24
                               else 'Overnight')), hours)

    def count_sorted_hours(self, sort_hours):
        """
        Count the number of times the words of the parts
        of the day appear.

        Parameters
        ----------
        sort_hours : list
            a list of strings representing different parts
            of the day

        Returns
        -------
        counter
             a dictionary whose keys are the parts of the day and
             values are the frequencies with which they appear in
             the list

        Example
        -------
        ['Overnight', 'Evening', 'Evening', 'Overnight', 'Evening']

        results in {'Evening': 3, 'Overnight': 2}
        """
        return Counter(sort_hours)

    def active_time_dict(self, trackings, col_time=6):
        """
        A dictionary whose keys are the parts of the day
        (Morning, Afternoon, Evening and Overnight) in which a
        habit was checked and whose values indicate how often
        the activity is performed in these parts of the day.

        Parameters
        ----------
        trackings : list of tuples
            a list with the information of the trackings
            registered for a certain habit
        col_time : int
            index number i.e. column containing the times
            (default is number 6)

        Returns
        -------
        counter
            a dictionary whose keys are the parts of the day and
            values are the frequencies with which the habit is
            performed
        """
        return self.count_sorted_hours(
            self.sort_hours(
                self.only_hours(
                    self.format_to_time(
                        self.select_column(
                            trackings, col_time)))))

    def max_value(self, active_time_dict):
        """
        The highest value from a dictionary.

        Parameters
        ----------
        active_time_dict : dict
            a dictionary whose keys are the parts of the day
            and values are the frequencies with which the
            habit is performed

        Returns
        -------
        int
            a number which is the highest value
        """
        if len(active_time_dict) == 0:
            return {}
        return max(active_time_dict.values())

    def most_active_time(self, active_time_dict, max_value):
        """
        Get the dictionary key(s) with the maximum value.

        Parameters
        ----------
        active_time_dict : dict
            a dictionary whose keys are the parts of the day
            and values are the frequencies with which the
            habit is performed
        max_value : int
            a number which is the highest value of the
            dictionary

        Returns
        -------
        list
            a list of string(s) representing the part(s) of
            the day when a habit is most frequently checked off

        Example
        -------
        {'Morning':4, 'Evening': 3, 'Overnight': 2}

        results in ['Morning']
        """
        if len(active_time_dict) == 0:
            return {}
        return [k for k, v in active_time_dict.items() if v == max_value]

    def unique_ids_periodicity(self, table, col_periodicity, periodicity):
        """
        Get the ids of the habits with the same periodicity.

        Parameters
        ----------
        table : list of tuples
            name of the table
        col_periodicity : int
            index number i.e. column containing the periodicity
        periodicity : str
            periodicity of the habit, 'weekly' or 'daily'

        Returns
        -------
        list
            a list of numbers representing ids
        """
        return self.unique_data(
            self.get_all_ids(
                self.select_rows(table, col_periodicity, periodicity)
                )
            )

    def list_habits_list(self,habits_trackings_table, unique_ids):
        """
        Give a list of lists of habits grouped by id.

        Parameters
        ----------
        habits_trackings_table : list of tuples
            a list with the information of the habits and
            its trackings
        unique_ids : list
            a list of numbers representing ids

        Returns
        -------
        list
            Habits are grouped by id
        """
        return [self.select_rows(habits_trackings_table, 0, id_n) for id_n in unique_ids]

    def lists_periodicity(self, table, col_periodicity, periodicity):
        """
        A list of habits with the same periodicity. Information and
        trackings for each habit are grouped together in a list.

        Parameters
        ----------
        table : list of tuples
            name of the table
        col_periodicity : int
            index number i.e. column containing the periodicity
        periodicity : str
            periodicity of the habit, 'weekly' or 'daily'

        Returns
        -------
        list
            a list of lists. Each list has information and
            trackings for each habit with the same periodicity

        Example
        -------
        For the daily periodicity in the join of the habits and trackings
        table gives the following
        [[(1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-07-31', '16:41'),
          (1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-08-02', '18:44'),
          (1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-08-03', '13:43')],
         [(3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-08-03', '15:44')]]
        """
        return self.list_habits_list(table,
                                     self.unique_ids_periodicity(table,
                                                                 col_periodicity,
                                                                 periodicity))

    def periodicity_info(self, lists_periodicity, periodicity, col_date=5):
        """
        A list containing information on each habit according
        to its periodicity. ID and name of the habit, date of
        the first and last tracking, part of the day when the
        user is most active to perform this habit, days or weeks
        of activity, and the longest streak.

        Parameters
        ----------
        lists_periodicity : list
            a list of lists of habits with the same periodicity.
            Each list has information of the habit and its trackings
        periodicity : str
            periodicity of the habit, 'weekly' or 'daily'
        col_date : int
            index number i.e. column containing dates
            (default is number 5)

        Returns
        -------
        list
            a list of tuples containing information on each habit

        Example
        -------
        [(1, 'Yoga', '2021-03-18', '2021-04-17', 'Evening', 5, 2),
         (2, 'Reading', '2021-03-19', '2021-04-25', 'Afternoon', 8, 2)]
        """
        habits_info = []

        for habit_info in lists_periodicity:

            active_time_dictionary = self.active_time_dict(
                                habit_info,
                                6)
            max_value_active_time = self.max_value(
                                active_time_dictionary)
            most_active_time = self.most_active_time(
                                active_time_dictionary,
                                max_value_active_time)

            habits_info.append(
                (
                    self.display_unique_elements(habit_info, 0),
                    self.display_unique_elements(habit_info, 1),
                    ''.join(min(self.select_column(habit_info, col_date))),
                    ''.join(max(self.select_column(habit_info, col_date))),
                    self.display_elements(most_active_time, ', '),
                    self.activity(
                        periodicity,
                        habit_info,
                        col_date),
                    self.longest_streak_periodicity(
                        habit_info,
                        periodicity,
                        col_date))
                )

        return habits_info

    def lists_both_periodicities(self, habits_trackings_table):
        """
        Information and trackings for each habit are grouped together
        in a list. In addition, habits with the same periodicity are
        grouped together.

        Parameters
        ----------
        habits_trackings_table : list of tuples
            a list with the information of the habits and
            its trackings

        Returns
        -------
        list
            list of lists. Information and trackings for each habit
            are grouped together, and habits with the same periodicity
            are grouped together as well.

        Example
        -------
        [[[(1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-07-31', '16:41'),
           (1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-08-02', '18:44')],
          [(3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-08-03', '15:44')]],
         [[(2, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-31', '16:46'),
           (2, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-08-03', '14:36')]]]
        """
        return list(map(self.lists_periodicity, *zip((habits_trackings_table, 2, 'daily'),
                                             (habits_trackings_table, 2, 'weekly'))))

    def both_periodicities_info(self, lists_both_periodicities):
        """
        Habits separated by periodicity with general information
        about each habit. ID and Name of the habit, date of the
        first and last tracking, part of the day when the user
        is most active to perform this habit, days or weeks of
        activity, and the longest streak.

        Parameters
        ----------
        lists_both_periodicities : list
            Information and trackings for each habit grouped
            together. Habits with the same periodicity
            grouped together as well.

        Returns
        -------
        list
            list of lists with general information about each habit

        Example
        -------
        [[('1', 'Yoga', '2021-07-31', '2021-08-03', 'Afternoon', 3, 2),
          ('3', 'Read', '2021-08-03', '2021-08-03', 'Afternoon', 1, 1)],
         [('2', 'Run', '2021-07-31', '2021-08-03', 'Afternoon', 2, 2)]]
        """
        return list(map(self.periodicity_info, *zip((lists_both_periodicities[0], 'daily'),
                                              (lists_both_periodicities[1], 'weekly'))))

    def info_all_habits(self, both_periodicities_info):
        """
        Information on the habits is merged into a single list.

        Parameters
        ----------
        both_periodicities_info : list
            list of lists with general information about each habit

        Returns
        -------
        list
            a list with general information about each habit

        Example
        -------
        [('1', 'Yoga', '2021-07-31', '2021-08-03', 'Afternoon', 3, 2),
         ('3', 'Read', '2021-08-03', '2021-08-03', 'Afternoon', 1, 1)]
        """
        return [habit for l in both_periodicities_info for habit in l]

    def habit_info_longest_streak(self, habits_trackings_table):
        """
        Information of the habit(s) that has(have) the
        maximum streak.

        Parameters
        ----------
        habits_trackings_table : list of tuples
            a list with the information of the habits and
            its trackings

        Returns
        -------
        list
            a list with general information of the habit(s)
            that has(have) the maximum streak.

        Example
        -------
        [('1', 'Yoga', '2021-06-26', '2021-07-23', 'Morning', 17, 9)]
        """
        all_periodicity_habits = self.info_all_habits(
            self.both_periodicities_info(
                self.lists_both_periodicities(
                    habits_trackings_table)))

        if len(all_periodicity_habits) > 1:
            # get the number of the maximum streak
            max_n = max(all_periodicity_habits, key=itemgetter(-1))[-1]
            # get all habits which have the same number of the maximum streak
            return self.select_rows(all_periodicity_habits, -1, max_n)
        return all_periodicity_habits

    def name_habit_longest_streak(self, habit_info_longest_streak):
        """
        Give the name(s) of the habit(s) with the longest streak
        and the streak.

        Parameters
        ----------
        habit_info_longest_streak : list
             a list with general information of the habit(s)
             that has(have) the maximum streak.

        Returns
        -------
        list
            a list with the name and longest streak of
            habit(s) with the longest streak

        Example
        -------
        [('Yoga', 2), ('Read', 2), ('Run', 2)]
        """
        return list(zip(self.select_column(habit_info_longest_streak, 1),
                        self.select_column(habit_info_longest_streak, -1)))

    def lengths(self, habits_info):
        """
        Length of each element

        Parameters
        ----------
        habits_info : list
             a list of tuples with general information
             about each habit

        Returns
        -------
        list
            a list of lists of numbers representing lenghts

        Example
        -------
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-20'),
         (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21')]

        Results in
        [[1, 4, 5, 16, 25, 10],
         [1, 4, 5, 20, 10, 10]]
        """
        return [[len(str(x)) for x in row] for row in habits_info]

    def max_lengths(self, lengths, table):
        """
        The longest lengths

        Parameters
        ----------
        lengths : list
             a list of lists of numbers representing lenghts
        table : list of tuples
             name of the table

        Returns
        -------
        list
            a list with the longest lengths

        Example
        -------
        [[1, 4, 5, 16, 25, 10],
         [1, 4, 5, 20, 10, 10],
         [1, 3, 6, 9, 11, 10]]

        Results in [1, 4, 6, 20, 25, 10].
        """
        return list(max(map(itemgetter(x), lengths)) for x in range(0, len(table[0])))

    def distance_format(self, max_lengths):
        """
        Create a string formating that represents
        the distance to be maintained between each
        element.

        Parameters
        ----------
        max_lengths : list
             a list with the longest lengths

        Returns
        -------
        str
            a string formating

        Example
        -------
        if max_lengths = [1, 4, 6, 20, 25, 10]

        "%-1s    %-4s    %-6s    %-20s    %-25s    %-10s    "
        """
        return ''.join(map(lambda x: '%%-%ss    ' % x, max_lengths))

    def aligned_columns(self, format_distance, table):
        """
        Elements of the db table are separated and
        aligned.

        Parameters
        ----------
        format_distance : str
             a string formating that represents the distance
             to be maintained between each element
        table : list of tuples
             name of the table

        Returns
        -------
        list
            a list of strings whose elements are aligned with
            the given distance
        """
        return map(lambda x: format_distance % x, table)

    def line(self, max_lengths):
        """
        Create a line by adding the elements of a list
        of numbers (maximum lengths) and the spaces between
        the elements.

        Parameters
        ----------
        max_lengths : list
             a list with the longest lengths

        Returns
        -------
        str:
            a line with the given length
        """
        return '_' * (sum(max_lengths) + len(max_lengths) * 4)

    def add_colnames(self, col_names, table):
        """
        Add the names of each column.

        Parameters
        ----------
        col_names : str
            contains the names of each column
        table : list of tuples
             name of the table

        Returns
        -------
        list
            a list of tuples
        """
        return [col_names]+table

    def table_line(self, table):
        """
        Adjust the length of the line in relation to
        the data in the table.

        Parameters
        ----------
        table : list of tuples
             name of the table

        Returns
        -------
        str
            a line with the right length
        """
        return self.line(
            self.max_lengths(
                self.lengths(table), table))

    def display_table(self, col_names, table, header):
        """
        Display the data in a table.

        Parameters
        ----------
        col_names : str
            contains the names of each column
        table : list of tuples
            name of the table
        header : list of tuples
            title of the table
        """
        data_colnames = self.add_colnames(col_names, table)

        print(self.table_line(data_colnames))
        print("{}".format(header))
        print(self.table_line(data_colnames))
        print(self.display_elements(
            self.aligned_columns(
                self.distance_format(
                    self.max_lengths(
                        self.lengths(data_colnames),
                        data_colnames)),
                data_colnames)))
        print(self.table_line(data_colnames))

    def table_registered_habits(self):
        """
        Display the names and ids of the registered habits
        in table format. The table has a title and the name
        of the columns.
        """
        self.display_table(
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
        Register in the trackings table the day and time
        when the user checks a habit off, i.e. chooses
        the id of the habit.
        """
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M")

        with self.connection:
            self.cursor.execute("""INSERT INTO trackings (Date, Time, HabitID)
                                VALUES (:date, :time, :habitID)""",
                            {'date': date, 'time': time, 'habitID': id_habit})

    def close(self):
        """
        Close SQLite3 connection
        """
        self.connection.close()
