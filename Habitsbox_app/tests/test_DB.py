from application.analytics import Analytics
from datetime import date

analytics = Analytics()


def insert_habit():
    analytics.insert_habit('Play Piano', 'daily', 'Learn more songs', 'Minimum one hour')
    
def delete_habit():
    analytics.remove_habit('Play Piano')
    
def test_get_habits_table_piano():
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

def test_get_habist_trackings_table():
    habits_trackings_table = analytics.habits_trackings_table()
    assert habits_trackings_table ==  [(2, 'Run',  'weekly', 'Improved fitness', 'Jogging and sprinting', '2021-06-25', '18:26'),
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
                                       (5, 'Learn French', 'weekly', 'Fluent in french', 'Practice the 4 skills', '2021-06-29', '04:46'),
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
                                       (5, 'Learn French', 'weekly', 'Fluent in french', 'Practice the 4 skills', '2021-07-07', '16:09'),
                                       (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-08', '18:19'),
                                       (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-08', '22:35'),
                                       (5, 'Learn French', 'weekly', 'Fluent in french', 'Practice the 4 skills', '2021-07-09', '10:01'),
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
                                       (5, 'Learn French', 'weekly', 'Fluent in french', 'Practice the 4 skills', '2021-07-16', '21:14'),
                                       (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-18', '03:03'),
                                       (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-18', '06:59'),
                                       (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-19', '22:50'),
                                       (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-19', '13:05'),
                                       (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-20', '04:59'),
                                       (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-20', '05:52'),
                                       (5, 'Learn French', 'weekly', 'Fluent in french', 'Practice the 4 skills', '2021-07-20', '09:00'),
                                       (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-21', '18:44'),
                                       (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-21', '03:55'),
                                       (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-07-22', '06:52'),
                                       (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-22', '18:27'),
                                       (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-23', '01:28'),
                                       (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-23', '12:17'),
                                       (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-24', '19:10'),
                                       (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-25', '02:18'),
                                       (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-07-26', '09:53'),
                                       (5, 'Learn French', 'weekly', 'Fluent in french', 'Practice the 4 skills', '2021-07-26', '16:59')]

def insert_day():
    analytics.insert_day(6)
        
def test_get_last_tracking_insertation_():
    insert_habit()
    insert_day()
    trackings_table = analytics.trackings_table()
    assert trackings_table[60][:-1] == (6, str(date.today()))
    delete_habit()
        
def test_first_tracking():
    habits_trackings_table = analytics.habits_trackings_table()
    
    Yoga = analytics.select_rows(habits_trackings_table, 0, 1)
    Run = analytics.select_rows(habits_trackings_table, 0, 2)
    Read = analytics.select_rows(habits_trackings_table, 0, 3)
    Meditation = analytics.select_rows(habits_trackings_table, 0, 4)
    French = analytics.select_rows(habits_trackings_table, 0, 5)
    
    Yoga_start_date = analytics.start_habit(Yoga, 5) 
    Run_start_date = analytics.start_habit(Run, 5) 
    Read_start_date = analytics.start_habit(Read, 5)
    Meditation_start_date = analytics.start_habit(Meditation, 5)
    French_start_date = analytics.start_habit(French, 5)
    
    assert Yoga_start_date == date(2021, 6, 26) 
    assert Run_start_date == date(2021, 6, 25)
    assert Read_start_date == date(2021, 6, 25)
    assert Meditation_start_date == date(2021, 6, 29)
    assert French_start_date == date(2021, 6, 29)
    
def test_last_tracking():
    habits_trackings_table = analytics.habits_trackings_table()
    
    Yoga = analytics.select_rows(habits_trackings_table, 0, 1)
    Run = analytics.select_rows(habits_trackings_table, 0, 2)
    Read = analytics.select_rows(habits_trackings_table, 0, 3)
    Meditation = analytics.select_rows(habits_trackings_table, 0, 4)
    French = analytics.select_rows(habits_trackings_table, 0, 5)
    

    Yoga_last_day = analytics.last_day(Yoga, 5)
    Run_last_day = analytics.last_day(Run, 5)
    Read_last_day = analytics.last_day(Read, 5)
    Meditation_last_day = analytics.last_day(Meditation, 5)
    French_last_day = analytics.last_day(French, 5)
    
    assert Yoga_last_day == date(2021, 7, 23) 
    assert Run_last_day == date(2021, 7, 12)
    assert Read_last_day == date(2021, 7, 22)
    assert Meditation_last_day == date(2021, 7, 26)
    assert French_last_day == date(2021, 7, 26)
    
def test_most_active_time():
    trackings_table = analytics.trackings_table()
    
    Yoga_trackings = analytics.select_rows(trackings_table, 0, 1)
    Run_trackings = analytics.select_rows(trackings_table, 0, 2)
    Read_trackings = analytics.select_rows(trackings_table, 0, 3)
    Meditation_trackings = analytics.select_rows(trackings_table, 0, 4)
    French_trackings = analytics.select_rows(trackings_table, 0, 5)
    
    Yoga_active_time = analytics.active_time_dict(Yoga_trackings, 2)
    Run_active_time = analytics.active_time_dict(Run_trackings, 2)
    Read_active_time = analytics.active_time_dict(Read_trackings, 2)
    Meditation_active_time = analytics.active_time_dict(Meditation_trackings, 2) 
    French_active_time = analytics.active_time_dict(French_trackings, 2)
    
    Yoga_max_active_time = analytics.max_value(Yoga_active_time)
    Run_max_active_time = analytics.max_value(Run_active_time)
    Read_max_active_time = analytics.max_value(Read_active_time)
    Meditation_max_active_time = analytics.max_value(Meditation_active_time)
    French_max_active_time = analytics.max_value(French_active_time)
    
    assert analytics.most_active_time(Yoga_active_time, Yoga_max_active_time) == ['Morning']
    assert analytics.most_active_time(Run_active_time, Run_max_active_time) == ['Afternoon']
    assert analytics.most_active_time(Read_active_time, Read_max_active_time) == ['Evening', 'Morning']
    assert analytics.most_active_time(Meditation_active_time, Meditation_max_active_time) == ['Overnight']
    assert analytics.most_active_time(French_active_time, French_max_active_time) == ['Afternoon', 'Morning']
    
def test_longest_streak():
    trackings_table = analytics.trackings_table()
    
    Yoga_trackings = analytics.select_rows(trackings_table, 0, 1)
    Run_trackings = analytics.select_rows(trackings_table, 0, 2)
    Read_trackings = analytics.select_rows(trackings_table, 0, 3)
    Meditation_trackings = analytics.select_rows(trackings_table, 0, 4)
    French_trackings = analytics.select_rows(trackings_table, 0, 5)
    
    Yoga_longest_streak = analytics.longest_streak_periodicity(Yoga_trackings, 'daily', 1)
    Run_longest_streak = analytics.longest_streak_periodicity(Run_trackings, 'weekly', 1)
    Read_longest_streak = analytics.longest_streak_periodicity(Read_trackings, 'daily', 1)
    Meditation_longest_streak = analytics.longest_streak_periodicity(Meditation_trackings, 'daily', 1)
    French_longest_streak = analytics.longest_streak_periodicity(French_trackings, 'weekly', 1)
    
    assert Yoga_longest_streak == 9
    assert Run_longest_streak == 4
    assert Read_longest_streak == 7
    assert Meditation_longest_streak == 4
    assert French_longest_streak == 5
      
def test_days_activity():
    trackings_table = analytics.trackings_table()
    
    Yoga_trackings = analytics.select_rows(trackings_table, 0, 1)
    Run_trackings = analytics.select_rows(trackings_table, 0, 2)
    Read_trackings = analytics.select_rows(trackings_table, 0, 3)
    Meditation_trackings = analytics.select_rows(trackings_table, 0, 4)
    French_trackings = analytics.select_rows(trackings_table, 0, 5)
    
    assert analytics.activity('daily', Yoga_trackings, 1) == 17
    assert analytics.activity('weekly', Run_trackings, 1) == 4
    assert analytics.activity('daily', Read_trackings, 1) == 18
    assert analytics.activity('daily', Meditation_trackings, 1) == 15
    assert analytics.activity('weekly', French_trackings, 1) == 5
    
def test_all_habits_registered():
    habits_table = analytics.habits_table()
    assert habits_table ==  [
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-06-25'),
        (2, 'Run', 'weekly', 'Improved fitness', 'Jogging and sprinting', '2021-06-25'),
        (3, 'Read', 'daily', '12 books in a year', 'Classics and dystopian', '2021-06-25'),
        (4, 'Meditation', 'daily', 'Training awareness', '20 minutes', '2021-06-29'),
        (5, 'Learn French', 'weekly', 'Fluent in french', 'Practice the 4 skills', '2021-06-29')
        ]

def test_habits_info_same_periodicity():
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
    habits_trackings_table = analytics.habits_trackings_table()
    habit_info_longest_streak = analytics.habit_info_longest_streak(habits_trackings_table)
    assert analytics.name_habit_longest_streak(habit_info_longest_streak) == [('Yoga', 9)]
    
    
    
 


    




















    


























