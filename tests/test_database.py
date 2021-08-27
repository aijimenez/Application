"""
Database related methods in the analytics module are tested.
Results of menu options such as see one habit, see habits with
the same periodicity and the longest streak of all habits are
tested using the five predetermined habits in the database.
"""
from datetime import date
from Habitsbox_app.application.analytics import Analytics

analytics = Analytics()


def insert_habit():
    """
    Insert the habit play piano and its corresponding
    information in the database.
    """
    analytics.insert_habit('Play Piano', 'daily', 'Learn more songs', 'Minimum one hour')

def delete_habit():
    """
    Delete the habit play piano and its corresponding
    information in the database.
    """
    analytics.remove_habit('Play Piano')

def test_get_habits_table_piano():
    """
    Get the habits registered in the habits table
    of the database.
    Verify that the habit play piano was inserted.
    """
    insert_habit()
    habits_table_with_piano = analytics.habits_table()
    assert habits_table_with_piano ==  [
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-06-25'),
        (2, 'Run', 'weekly', 'Improved fitness', 'Jogging and sprinting', '2021-06-25'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-06-25'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-06-29'),
        (5, 'Learn French', 'weekly', 'Fluent in french', 'Practice the 4 skills', '2021-06-29'),
        (6, 'Play Piano', 'daily', 'Learn more songs', 'Minimum one hour', str(date.today()))
        ]
    delete_habit()

def test_get_trackings_table():
    """
    Get the trackings recorded in the trackings table
    of the database.
    """
    trackings_table = analytics.trackings_table()
    assert trackings_table == [(2, '2021-06-25', '18:26'), (3, '2021-06-25', '19:52'),
                               (1, '2021-06-26', '20:09'), (3, '2021-06-26', '04:40'),
                               (1, '2021-06-27', '10:44'), (3, '2021-06-27', '20:49'),
                               (3, '2021-06-28', '01:18'), (3, '2021-06-29', '19:42'),
                               (1, '2021-06-29', '08:25'), (4, '2021-06-29', '08:57'),
                               (2, '2021-06-29', '02:07'), (5, '2021-06-29', '04:46'),
                               (1, '2021-06-30', '05:54'), (4, '2021-06-30', '12:04'),
                               (4, '2021-07-01', '05:37'), (1, '2021-07-01', '07:17'),
                               (3, '2021-07-01', '12:16'), (3, '2021-07-02', '22:04'),
                               (4, '2021-07-02', '23:02'), (3, '2021-07-03', '07:12'),
                               (3, '2021-07-04', '08:11'), (3, '2021-07-05', '10:58'),
                               (2, '2021-07-05', '14:38'), (3, '2021-07-06', '00:14'),
                               (4, '2021-07-06', '12:28'), (3, '2021-07-07', '17:07'),
                               (4, '2021-07-07', '02:44'), (5, '2021-07-07', '16:09'),
                               (4, '2021-07-08', '18:19'), (1, '2021-07-08', '22:35'),
                               (5, '2021-07-09', '10:01'), (1, '2021-07-09', '10:14'),
                               (1, '2021-07-10', '17:12'), (1, '2021-07-11', '19:54'),
                               (1, '2021-07-12', '00:06'), (2, '2021-07-12', '16:12'),
                               (3, '2021-07-12', '18:43'), (1, '2021-07-13', '08:02'),
                               (1, '2021-07-14', '21:32'), (1, '2021-07-15', '08:37'),
                               (1, '2021-07-16', '08:32'), (3, '2021-07-16', '11:59'),
                               (5, '2021-07-16', '21:14'), (4, '2021-07-18', '03:03'),
                               (1, '2021-07-18', '06:59'), (4, '2021-07-19', '22:50'),
                               (3, '2021-07-19', '13:05'), (4, '2021-07-20', '04:59'),
                               (3, '2021-07-20', '05:52'), (5, '2021-07-20', '09:00'),
                               (3, '2021-07-21', '18:44'), (4, '2021-07-21', '03:55'),
                               (3, '2021-07-22', '06:52'), (1, '2021-07-22', '18:27'),
                               (4, '2021-07-23', '01:28'), (1, '2021-07-23', '12:17'),
                               (4, '2021-07-24', '19:10'), (4, '2021-07-25', '02:18'),
                               (4, '2021-07-26', '09:53'), (5, '2021-07-26', '16:59')]

def test_get_habits_trackings_table():
    """
    Get the join of the habits and trackings tables
    in the database.
    """
    habits_trackings_table = analytics.habits_trackings_table()
    assert habits_trackings_table ==  [
        (2, 'Run',  'weekly', 'Improved fitness', 'Jogging and sprinting', '2021-06-25', '18:26'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-06-25', '19:52'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-06-26', '20:09'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-06-26', '04:40'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-06-27', '10:44'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-06-27', '20:49'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-06-28', '01:18'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-06-29', '19:42'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-06-29', '08:25'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-06-29', '08:57'),
        (2, 'Run', 'weekly', 'Improved fitness', 'Jogging and sprinting', '2021-06-29', '02:07'),
        (5, 'Learn French', 'weekly', 'Fluent in french',
         'Practice the 4 skills', '2021-06-29', '04:46'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-06-30', '05:54'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-06-30', '12:04'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-01', '05:37'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-01', '07:17'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-01', '12:16'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-02', '22:04'),
        (4,  'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-02', '23:02'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-03', '07:12'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-04', '08:11'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-05', '10:58'),
        (2, 'Run', 'weekly', 'Improved fitness', 'Jogging and sprinting', '2021-07-05', '14:38'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-06', '00:14'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-06', '12:28'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-07', '17:07'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-07', '02:44'),
        (5, 'Learn French', 'weekly', 'Fluent in french',
         'Practice the 4 skills', '2021-07-07', '16:09'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-08', '18:19'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-08', '22:35'),
        (5, 'Learn French', 'weekly', 'Fluent in french',
         'Practice the 4 skills', '2021-07-09', '10:01'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-09', '10:14'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-10', '17:12'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-11', '19:54'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-12', '00:06'),
        (2, 'Run', 'weekly', 'Improved fitness', 'Jogging and sprinting', '2021-07-12', '16:12'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-12', '18:43'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-13', '08:02'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-14', '21:32'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-15', '08:37'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-16', '08:32'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-16', '11:59'),
        (5, 'Learn French', 'weekly', 'Fluent in french',
         'Practice the 4 skills', '2021-07-16', '21:14'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-18', '03:03'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-18', '06:59'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-19', '22:50'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-19', '13:05'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-20', '04:59'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-20', '05:52'),
        (5, 'Learn French', 'weekly', 'Fluent in french',
         'Practice the 4 skills', '2021-07-20', '09:00'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-21', '18:44'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-21', '03:55'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-22', '06:52'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-22', '18:27'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-23', '01:28'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-23', '12:17'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-24', '19:10'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-25', '02:18'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-26', '09:53'),
        (5, 'Learn French', 'weekly', 'Fluent in french',
         'Practice the 4 skills', '2021-07-26', '16:59')
        ]

def insert_day():
    """
    Date and current time corresponding to the habit
    with id number 6 are inserted in the trackings table
    of the database.
    """
    analytics.insert_day(6)

def test_get_last_tracking_insertation_():
    """
    Get the id number and date of the tracking 61 in
    the trackings table of the database.
    """
    insert_habit()
    insert_day()
    trackings_table = analytics.trackings_table()
    assert trackings_table[60][:-1] == (6, str(date.today()))
    delete_habit()

def yoga_habits_trackings():
    """
    Select the rows corresponding to the yoga habit
    in the join of the habits and trackings tables
    of the database.
    """
    return analytics.select_rows(
        analytics.habits_trackings_table(),
        0,
        1)

def run_habits_trackings():
    """
    Select the rows corresponding to the run habit
    in the join of the habits and trackings tables
    of the database.
    """
    return analytics.select_rows(
        analytics.habits_trackings_table(),
        0,
        2)

def read_habits_trackings():
    """
    Select the rows corresponding to the read habit
    in the join of the habits and trackings tables
    of the database.
    """
    return analytics.select_rows(
        analytics.habits_trackings_table(),
        0,
        3)

def meditation_habits_trackings():
    """
    Select the rows corresponding to the meditation habit
    in the join of the habits and trackings tables
    of the database.
    """
    return analytics.select_rows(
        analytics.habits_trackings_table(),
        0,
        4)

def french_habits_trackings():
    """
    Select the rows corresponding to the french habit
    in the join of the habits and trackings tables
    of the database.
    """
    return analytics.select_rows(
        analytics.habits_trackings_table(),
        0,
        5)

def test_first_tracking():
    """
    Gives the date of the first tracking.
    """
    yoga_start_date = analytics.start_habit(yoga_habits_trackings(), 5)
    run_start_date = analytics.start_habit(run_habits_trackings(), 5)
    read_start_date = analytics.start_habit(read_habits_trackings())
    meditation_start_date = analytics.start_habit(meditation_habits_trackings())
    french_start_date = analytics.start_habit(french_habits_trackings())

    assert yoga_start_date == date(2021, 6, 26)
    assert run_start_date == date(2021, 6, 25)
    assert read_start_date == date(2021, 6, 25)
    assert meditation_start_date == date(2021, 6, 29)
    assert french_start_date == date(2021, 6, 29)

def test_last_tracking():
    """
    Gives the date of the last tracking.
    """
    yoga_last_day = analytics.last_day(yoga_habits_trackings())
    run_last_day = analytics.last_day(run_habits_trackings())
    read_last_day = analytics.last_day(read_habits_trackings())
    meditation_last_day = analytics.last_day(meditation_habits_trackings())
    french_last_day = analytics.last_day(french_habits_trackings(), 5)

    assert yoga_last_day == date(2021, 7, 23)
    assert run_last_day == date(2021, 7, 12)
    assert read_last_day == date(2021, 7, 22)
    assert meditation_last_day == date(2021, 7, 26)
    assert french_last_day == date(2021, 7, 26)

def yoga_trackings():
    """
    Select the rows corresponding to the yoga
    habit in the trackings table of the db.
    """
    return analytics.select_rows(
        analytics.trackings_table(),
        0,
        1)

def run_trackings():
    """
    Select the rows corresponding to the run
    habit in the trackings table of the db.
    """
    return analytics.select_rows(
        analytics.trackings_table(),
        0,
        2)

def read_trackings():
    """
    Select the rows corresponding to the read
    habit in the trackings table of the db.
    """
    return analytics.select_rows(
        analytics.trackings_table(),
        0,
        3)

def meditation_trackings():
    """
    Select the rows corresponding to the meditation
    habit in the trackings table of the db.
    """
    return analytics.select_rows(
        analytics.trackings_table(),
        0,
        4)

def french_trackings():
    """
    Select the rows corresponding to the learning
    french habit in the trackings table of the db.
    """
    return analytics.select_rows(
        analytics.trackings_table(),
        0,
        5)

def test_most_active_time():
    """
    Part(s) of the day (Morning, Afternoon, Evening and Overnight)
    with the most trackings for a given habit, which means that the
    activity is most often performed in that part of the day.
    """
    yoga_active_time = analytics.active_time_dict(yoga_trackings(), 2)
    run_active_time = analytics.active_time_dict(run_trackings(), 2)
    read_active_time = analytics.active_time_dict(read_trackings(), 2)
    meditation_active_time = analytics.active_time_dict(meditation_trackings(), 2)
    french_active_time = analytics.active_time_dict(french_trackings(), 2)

    yoga_max_active_time = analytics.max_value(yoga_active_time)
    run_max_active_time = analytics.max_value(run_active_time)
    read_max_active_time = analytics.max_value(read_active_time)
    meditation_max_active_time = analytics.max_value(meditation_active_time)
    french_max_active_time = analytics.max_value(french_active_time)

    assert analytics.most_active_time(yoga_active_time,
                                      yoga_max_active_time) == ['Morning']
    assert analytics.most_active_time(run_active_time,
                                      run_max_active_time) == ['Afternoon']
    assert analytics.most_active_time(read_active_time,
                                      read_max_active_time) == ['Evening', 'Morning']
    assert analytics.most_active_time(meditation_active_time,
                                      meditation_max_active_time) == ['Overnight']
    assert analytics.most_active_time(french_active_time,
                                      french_max_active_time) == ['Afternoon', 'Morning']

def test_longest_streak():
    """
    Give the longest streak for a given habit.
    """
    yoga_longest_streak = analytics.longest_streak_periodicity(yoga_trackings(), 'daily', 1)
    run_longest_streak = analytics.longest_streak_periodicity(run_trackings(), 'weekly', 1)
    read_longest_streak = analytics.longest_streak_periodicity(read_trackings(), 'daily', 1)
    meditation_longest_streak = analytics.longest_streak_periodicity(meditation_trackings(),
                                                                     'daily',
                                                                     1)
    french_longest_streak = analytics.longest_streak_periodicity(french_trackings(), 'weekly', 1)

    assert yoga_longest_streak == 9
    assert run_longest_streak == 4
    assert read_longest_streak == 7
    assert meditation_longest_streak == 4
    assert french_longest_streak == 5

def test_days_weeks_activity():
    """
    Total number of trackings. Days or weeks of activity
    depending on the periodicity of each habit.
    """
    assert analytics.activity('daily', yoga_trackings(), 1) == 17
    assert analytics.activity('weekly', run_trackings(), 1) == 4
    assert analytics.activity('daily', read_trackings(), 1) == 18
    assert analytics.activity('daily', meditation_trackings(), 1) == 15
    assert analytics.activity('weekly', french_trackings(), 1) == 5

def test_all_habits_registered():
    """
    Give the information contained in the habits table.
    ID and name of each habit, periodicity, motivation, description
    of the habit, and date when the habit was created.
    """
    habits_table = analytics.habits_table()
    assert habits_table ==  [
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-06-25'),
        (2, 'Run', 'weekly', 'Improved fitness', 'Jogging and sprinting', '2021-06-25'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-06-25'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-06-29'),
        (5, 'Learn French', 'weekly', 'Fluent in french', 'Practice the 4 skills', '2021-06-29')
        ]

def test_tracked_habits():
    pass

def test_habits_info_same_periodicity():
    """
    Give information for each habit with the same periodicity.
    ID and name of each habit, date of the first and last tracking,
    most active time, days or weeks of activity according to
    periodicity and its longest streak.
    """
    habits_trackings_table = analytics.habits_trackings_table()
    list_daily = analytics.lists_periodicity(habits_trackings_table, 2, 'daily')
    list_weekly = analytics.lists_periodicity(habits_trackings_table, 2, 'weekly')
    assert analytics.periodicity_info(list_daily, 'daily') == [
        ('3', 'Read', '2021-06-25', '2021-07-22', 'Evening, Morning', 18, 7),
        ('1', 'Yoga', '2021-06-26', '2021-07-23', 'Morning', 17, 9),
        ('4', 'Meditation', '2021-06-29', '2021-07-26', 'Overnight', 15, 4)
        ]
    assert analytics.periodicity_info(list_weekly, 'weekly') == [
        ('2', 'Run', '2021-06-25', '2021-07-12', 'Afternoon', 4, 4),
        ('5', 'Learn French', '2021-06-29', '2021-07-26', 'Afternoon, Morning', 5, 5)
        ]

def test_longest_streak_all_habits():
    """
    Give the longest streak of all habits.
    """
    habits_trackings_table = analytics.habits_trackings_table()
    habit_info_longest_streak = analytics.habit_info_longest_streak(habits_trackings_table)
    assert analytics.name_habit_longest_streak(habit_info_longest_streak) == [('Yoga', 9)]
