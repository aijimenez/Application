from application.analytics import Analytics
from datetime import datetime
from datetime import timedelta, date, time

habits_table = [(1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-20'), 
               (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21'), 
               (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-22')]

trackings_table = [(1, '2021-07-21', '09:06'), (3, '2021-07-21', '15:26'), 
                   (3, '2021-07-21', '16:00'), (1, '2021-07-22', '17:11')]

habits_trackings_table = [(1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-21', '09:06'), 
                          (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '15:26'), 
                          (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '16:00'), 
                          (1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-22', '17:11')]

analytics = Analytics()
trackings_one_habit = [(1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-21', '09:06'), 
                       (1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-22', '17:11')]

column = 5

ID_1_Week = [(1, '2019-12-24', '09:52'),(1, '2019-12-29', '03:42'),
        (1, '2019-12-31', '03:42'), (1, '2020-01-07', '18:00'),
        (1, '2020-01-16', '19:52'), (1, '2020-01-28', '02:42'),
        (1, '2020-02-01', '19:52'), (1, '2020-02-03', '02:42'), 
        (1, '2020-02-03', '08:25'), (1, '2020-02-11', '00:14'), 
        (1, '2020-02-11', '12:28'), (1, '2020-02-11', '17:07'), 
        (1, '2020-02-12', '16:09'),  (1, '2020-03-01', '06:59'),
        (1, '2020-03-10', '21:32'), (1, '2020-03-14', '06:59')]

col1_ID_1_Week = [('2019-12-24'),('2019-12-29'), ('2019-12-31'), ('2020-01-07'),
                     ('2020-01-16'), ('2020-01-28'), ('2020-02-01'), ('2020-02-03'), 
                     ('2020-02-03'), ('2020-02-11'), ('2020-02-11'), ('2020-02-11'), 
                     ('2020-02-12'), ('2020-03-01'), ('2020-03-10'), ('2020-03-14')]

ID_2_daily = [(2, '2020-02-18', '09:52'),(2, '2020-02-18', '03:42'),
        (2, '2020-02-18', '03:42'), (2, '2020-02-19', '18:00'),
        (2, '2020-02-25', '19:52'), (2, '2020-02-26', '02:42'),
        (2, '2020-02-27', '19:52'), (2, '2020-02-27', '02:42'), 
        (2, '2020-02-29', '08:25'), (2, '2020-03-01', '00:14'), 
        (2, '2020-03-02', '12:28'), (2, '2020-03-03', '17:07'), 
        (2, '2020-03-04', '16:09'),  (2, '2020-03-04', '06:59'),
        (2, '2020-03-11', '21:32'), (2, '2020-03-12', '06:59'),
        (2, '2020-03-13', '21:32'), (2, '2020-03-14', '06:59')]

def test_select_column():
    names_habits_table = analytics.select_column(habits_table, 1)
    ids_habits = analytics.select_column(habits_table, 0)
    ids_trackings = analytics.select_column(trackings_table, 0)
    dates = analytics.select_column(ID_1_Week, 1)
    assert names_habits_table == ['Yoga', 'Read', 'Run']
    assert ids_habits == [1, 3, 4]
    assert ids_trackings == [1, 3, 3, 1]
    assert dates == col1_ID_1_Week
    
def test_select_columns():
    ids_names = analytics.select_columns(habits_table, stop = 2)
    names_periodicity = analytics.select_columns(trackings_table, start = 1, stop = 3)
    names_trackings_one_habit = analytics.select_columns(trackings_one_habit, start = 1, stop = 2)
    assert ids_names == [(1, 'Yoga'), (3, 'Read'), (4, 'Run')]
    assert names_periodicity == [('2021-07-21', '09:06'), ('2021-07-21', '15:26'),
                                ('2021-07-21', '16:00'), ('2021-07-22', '17:11')]
    assert names_trackings_one_habit == [('Yoga',), ('Yoga',)]
    
def test_get_all_ids():
    ids_habits = analytics.get_all_ids(habits_table)
    ids_trackings = analytics.get_all_ids(trackings_table)
    assert ids_habits == [1, 3, 4]
    assert ids_trackings == [1, 3, 3, 1]
    
def test_select_rows():
    rows_name = analytics.select_rows(habits_table, 1, 'Yoga')
    rows_id = analytics.select_rows(habits_trackings_table, 0, 3)
    rows_periodicity = analytics.select_rows(habits_table, 2, 'daily')    
    assert rows_name == [(1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-20')]
    assert rows_id == [(3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '15:26'), 
                      (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '16:00')]
    assert rows_periodicity == [(1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-20'), 
                               (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21')]

def test_display_list_elements():
    names = analytics.display_list_elements(['Yoga', 'Read', 'Run'])
    assert names == 'Yoga\nRead\nRun'

def test_display_elements():
    names = analytics.display_elements(['Yoga', 'Read', 'Run'])
    assert names == 'Yoga, Read, Run'
    
def test_unique_elements():
    unique = analytics.unique_elements(habits_trackings_table, 1)
    assert unique == 'Yoga, Read'

def test_format_to_date():
    dates = analytics.format_to_date([('2021-07-21'), ('2021-07-21'), 
                                      ('2021-07-21'), ('2021-07-22')])
    dates_ID_1_Week = analytics.format_to_date(col1_ID_1_Week)
    assert dates == [date(2021, 7, 21), date(2021, 7, 21), 
                      date(2021, 7, 21), date(2021, 7, 22)]
    assert dates_ID_1_Week ==  [date(2019, 12, 24), date(2019, 12, 29), date(2019, 12, 31),
                             date(2020, 1, 7), date(2020, 1, 16), date(2020, 1, 28),
                             date(2020, 2, 1), date(2020, 2, 3), date(2020, 2, 3), 
                             date(2020, 2, 11), date(2020, 2, 11), date(2020, 2, 11), 
                             date(2020, 2, 12), date(2020, 3, 1), date(2020, 3, 10), 
                             date(2020, 3, 14)]
    
def test_format_to_time():
    times = analytics.format_to_time([('09:06'), ('15:26'), ('16:00'), ('17:11')])
    assert times ==  [time(9, 6), time(15, 26), time(16, 0), time(17, 11)]

def test_to_calender_week():
    calender_week = analytics.to_calender_week([date(2019, 12, 31), date(2020, 1, 1), 
                                                date(2020, 12, 31), date(2021, 12, 25)])
    calender_week1 = analytics.to_calender_week([date(2019, 12, 24), date(2019, 12, 29), date(2019, 12, 31),
                             date(2020, 1, 7), date(2020, 1, 16), date(2020, 1, 28),
                             date(2020, 2, 1), date(2020, 2, 3), date(2020, 2, 3), 
                             date(2020, 2, 11), date(2020, 2, 11), date(2020, 2, 11), 
                             date(2020, 2, 12), date(2020, 3, 1), date(2020, 3, 10), 
                             date(2020, 3, 14)])
    assert calender_week == [1, 1, 53, 51]
    assert calender_week1 == [52, 52, 1, 2, 3, 5, 5, 6, 6, 7, 7, 7, 7, 9, 11, 11]

def test_unique_data():
    unique_times = analytics.unique_data([date(2021, 7, 21), date(2021, 7, 21), 
                                          date(2021, 7, 21), date(2021, 7, 22)])
    unique_cw = analytics.unique_data([52, 52, 1, 2, 3, 5, 5, 6, 6, 7, 7, 7, 7, 9, 11, 11])
    assert unique_times == [date(2021, 7, 21), date(2021, 7, 22)]
    assert unique_cw == [52, 1, 2, 3, 5, 6, 7, 9, 11]

def test_zipping_unique_data():
    zip_times = analytics.zipping_unique_data([date(2021, 2, 1), date(2021, 2, 3), 
                                               date(2021, 2, 5), date(2021, 2, 6)])
    zip_times1 = analytics.zipping_unique_data([date(2021, 2, 1)])
    zip_unique_cw = analytics.zipping_unique_data([52, 1, 2, 3, 5, 6, 7, 9, 11])
    assert zip_times == [(date(2021, 2, 3), date(2021, 2, 1)),
                         (date(2021, 2, 5), date(2021, 2, 3)),
                         (date(2021, 2, 6), date(2021, 2, 5))]
    assert zip_times1 == []
    assert zip_unique_cw == [(1, 52), (2, 1), (3, 2), (5, 3), (6, 5), (7, 6), (9, 7), (11, 9)]
    
def test_differences():
    differences = analytics.differences([(date(2021, 2, 3), date(2021, 2, 1)),
                                          (date(2021, 2, 5), date(2021, 2, 3)),
                                          (date(2021, 2, 6), date(2021, 2, 5))])
    differences_cw = analytics.differences([(1, 52), (2, 1), (3, 2), (5, 3), 
                                            (6, 5), (7, 6), (9, 7), (11, 9)])
    assert differences ==  [timedelta(days=2), 
                            timedelta(days=2), 
                            timedelta(days=1)]
    assert differences_cw == [-51, 1, 1, 2, 1, 1, 2, 2]
    
def test_difference_in_days():
    diff_days = analytics.difference_in_days([timedelta(days=2), 
                                              timedelta(days=2),
                                              timedelta(days=1)])
    assert diff_days == [2, 2, 1]

def test_cw_5152_to_1():
    differences_cw = analytics.cw_5152_to_1([-51, 1, 1, 2, 1, 1, 2, 2])
    assert differences_cw == [1, 1, 1, 2, 1, 1, 2, 2]
    
def unpacking_group_diff(grouping_differences):
    return [[key, len(list(group))] for key, group in grouping_differences]

def test_grouping_differences():
    grouping_cw = analytics.grouping_differences([1, 1, 1, 2, 1, 1, 2, 2])
    assert unpacking_group_diff(grouping_cw) == [[1, 3], [2, 1], [1, 2], [2, 2]]
    
def test_streaks():
    streaks = analytics.streaks([[1, [1, 1, 1]], [2, [2]], [1, [1, 1]], [2, [2, 2]]])
    assert streaks == [3, 2]
    
def test_longest_streak():
    longest_streak = analytics.longest_streak([3, 2])
    assert longest_streak == 4

def test_longest_streak_periodicity():
    longest_streak_weekly = analytics.longest_streak_periodicity(ID_1_Week, 'weekly', 1)
    longest_streak_daily = analytics.longest_streak_periodicity(ID_2_daily, 'daily', 1)
    assert longest_streak_weekly == 4
    assert longest_streak_daily == 5
    
def test_start_date():
    start_date = analytics.start_habit(trackings_one_habit, column)
    assert start_date == datetime.strptime('2021-07-21', "%Y-%m-%d").date()
    





