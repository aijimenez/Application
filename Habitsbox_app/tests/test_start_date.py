from application.analytics import Analytics
#from datetime import datetime
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
                       (1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-22', '17:11'),
                       (1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-23', '17:11')]

column = 5

ID_1_Week = [(1, '2019-12-24', '09:52'),(1, '2019-12-29', '03:42'),
        (1, '2019-12-31', '03:42'), (1, '2020-01-07', '18:00'),
        (1, '2020-01-16', '19:52'), (1, '2020-01-28', '02:42'),
        (1, '2020-02-01', '19:52'), (1, '2020-02-03', '02:42'), 
        (1, '2020-02-03', '08:25'), (1, '2020-02-11', '00:14'), 
        (1, '2020-02-11', '12:28'), (1, '2020-02-11', '17:07'), 
        (1, '2020-02-12', '16:09'),  (1, '2020-03-01', '06:59'),
        (1, '2020-03-10', '21:32'), (1, '2020-03-14', '06:59')]

dates_weekly = [('2019-12-24'),('2019-12-29'), ('2019-12-31'), ('2020-01-07'),
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
    assert dates == dates_weekly
    
def test_select_columns():
    ids_names = analytics.select_columns(habits_table, stop = 2)
    names_periodicity = analytics.select_columns(trackings_table, start = 1, stop = 3)
    names_trackings_one_habit = analytics.select_columns(trackings_one_habit, start = 1, stop = 2)
    assert ids_names == [(1, 'Yoga'), (3, 'Read'), (4, 'Run')]
    assert names_periodicity == [('2021-07-21', '09:06'), ('2021-07-21', '15:26'),
                                ('2021-07-21', '16:00'), ('2021-07-22', '17:11')]
    assert names_trackings_one_habit == [('Yoga',), ('Yoga',), ('Yoga',)]
    
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
    dates_ID_1_Week = analytics.format_to_date(dates_weekly)
    assert list(dates) == [date(2021, 7, 21), date(2021, 7, 21), 
                      date(2021, 7, 21), date(2021, 7, 22)]
    assert list(dates_ID_1_Week) ==  [date(2019, 12, 24), date(2019, 12, 29), date(2019, 12, 31),
                             date(2020, 1, 7), date(2020, 1, 16), date(2020, 1, 28),
                             date(2020, 2, 1), date(2020, 2, 3), date(2020, 2, 3), 
                             date(2020, 2, 11), date(2020, 2, 11), date(2020, 2, 11), 
                             date(2020, 2, 12), date(2020, 3, 1), date(2020, 3, 10), 
                             date(2020, 3, 14)]
    
def test_format_to_time():
    times = analytics.format_to_time([('09:52'), ('03:42'), ('03:42'), ('18:00'), 
                                       ('19:52'), ('02:42'), ('19:52'), ('02:42'), 
                                       ('08:25'), ('00:14'), ('12:28'), ('17:07'), 
                                       ('16:09'),  ('06:59'), ('21:32'), ('06:59')])
    assert list(times) == [time(9, 52), time(3, 42), time(3, 42), time(18, 0),
                            time(19, 52), time(2, 42), time(19, 52), time(2, 42),
                            time(8, 25), time(0, 14), time(12, 28), time(17, 7),
                            time(16, 9), time(6, 59), time(21, 32), time(6, 59)]

def test_to_calender_week():
    calender_week = analytics.to_calender_week([date(2019, 12, 31), date(2020, 1, 1), 
                                                date(2020, 12, 31), date(2021, 12, 25)])
    cw_dec_march = analytics.to_calender_week([date(2019, 12, 24), date(2019, 12, 29), date(2019, 12, 31),
                             date(2020, 1, 7), date(2020, 1, 16), date(2020, 1, 28),
                             date(2020, 2, 1), date(2020, 2, 3), date(2020, 2, 3), 
                             date(2020, 2, 11), date(2020, 2, 11), date(2020, 2, 11), 
                             date(2020, 2, 12), date(2020, 3, 1), date(2020, 3, 10), 
                             date(2020, 3, 14)])
    assert list(calender_week) == [1, 1, 53, 51]
    assert list(cw_dec_march) == [52, 52, 1, 2, 3, 5, 5, 6, 6, 7, 7, 7, 7, 9, 11, 11]

def test_unique_data():
    unique_times = analytics.unique_data([date(2021, 7, 21), date(2021, 7, 21), 
                                          date(2021, 7, 21), date(2021, 7, 22)])
    unique_cw = analytics.unique_data([52, 52, 1, 2, 3, 5, 5, 6, 6, 7, 7, 7, 7, 9, 11, 11])
    assert unique_times == [date(2021, 7, 21), date(2021, 7, 22)]
    assert unique_cw == [52, 1, 2, 3, 5, 6, 7, 9, 11]

def test_zipping_unique_data():
    zip_times = analytics.zipping_unique_data([date(2021, 2, 1), date(2021, 2, 3), 
                                               date(2021, 2, 5), date(2021, 2, 6)])
    zip_one_date = analytics.zipping_unique_data([date(2021, 2, 1)])
    zip_unique_cw = analytics.zipping_unique_data([52, 1, 2, 3, 5, 6, 7, 9, 11])
    assert list(zip_times) == [(date(2021, 2, 3), date(2021, 2, 1)),
                         (date(2021, 2, 5), date(2021, 2, 3)),
                         (date(2021, 2, 6), date(2021, 2, 5))]
    assert list(zip_one_date) == []
    assert list(zip_unique_cw) == [(1, 52), (2, 1), (3, 2), (5, 3), (6, 5), (7, 6), (9, 7), (11, 9)]
    
def test_differences():
    differences_dates = analytics.differences([(date(2021, 2, 3), date(2021, 2, 1)),
                                          (date(2021, 2, 5), date(2021, 2, 3)),
                                          (date(2021, 2, 6), date(2021, 2, 5))])
    differences_cw = analytics.differences([(1, 52), (2, 1), (3, 2), (5, 3), 
                                            (6, 5), (7, 6), (9, 7), (11, 9)])
    assert list(differences_dates) ==  [timedelta(days=2), 
                            timedelta(days=2), 
                            timedelta(days=1)]
    assert list(differences_cw) == [-51, 1, 1, 2, 1, 1, 2, 2]
    
def test_difference_in_days():
    diff_days = analytics.difference_in_days([timedelta(days=2), 
                                              timedelta(days=2),
                                              timedelta(days=1)])
    assert list(diff_days) == [2, 2, 1]

def test_cw_5152_to_1():
    differences_to_1 = analytics.cw_5152_to_1([-51, 1, 1, 2, 1, 1, 2, 2])
    assert list(differences_to_1) == [1, 1, 1, 2, 1, 1, 2, 2]
    
def unpacking_group_diff(grouping_differences):
    return [[key, len(list(group))] for key, group in grouping_differences]

def test_grouping_differences():
    grouping_cw = analytics.grouping_differences([1, 1, 1, 2, 1, 1, 2, 2])
    assert unpacking_group_diff(grouping_cw) == [[1, 3], [2, 1], [1, 2], [2, 2]]
    
def test_streaks():
    streaks = analytics.streaks([[1, [1, 1, 1]], [2, [2]], [1, [1, 1]], [2, [2, 2]]])
    assert streaks == [3, 2]
    #streaks = analytics.streaks([[1, 3], [2, 1], [1, 2], [2, 2]])   

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
    start_dates_unordered = analytics.start_habit(
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-25', '09:06'), 
         (1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-21', '17:11'),
         (1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-23', '17:11')], 5)
    assert start_date == date(2021, 7, 21)
    assert start_dates_unordered == date(2021, 7, 21)

def test_last_day():
    last_day = analytics.last_day(trackings_one_habit, column)
    assert last_day == date(2021, 7, 23)
    
def test_activity():
    activity_weekly = analytics.activity('weekly', ID_1_Week, 1)
    activity_daily = analytics.activity('daily', ID_2_daily, 1)
    assert activity_weekly == 9
    assert activity_daily == 14

def test_only_hours():
    hours = analytics.only_hours([time(9, 52), time(3, 42), time(3, 42), time(18, 0),
                                  time(19, 52), time(2, 42), time(19, 52), time(2, 42),
                                  time(8, 25), time(0, 14), time(12, 28), time(17, 7),
                                  time(16, 9), time(6, 59), time(21, 32), time(6, 59)])
    assert list(hours) == [9, 3, 3, 18, 19, 2, 19, 2, 8, 0, 12, 17, 16, 6, 21, 6]
    
def test_sort_hours():
    sort_hours = analytics.sort_hours([9, 3, 3, 18, 19, 2, 19, 2, 8, 0, 12, 17, 16, 6, 21, 6])
    assert list(sort_hours) == ['Morning', 'Overnight', 'Overnight', 'Evening', 'Evening',
                                'Overnight', 'Evening', 'Overnight', 'Morning', 'Overnight',
                                'Afternoon', 'Afternoon', 'Afternoon', 'Morning', 'Evening',
                                'Morning'] 

def test_count_sorted_hours():
    count_sorted_hours = analytics.count_sorted_hours(['Morning', 'Overnight', 'Overnight', 
                                                       'Evening', 'Evening', 'Overnight', 
                                                       'Evening', 'Overnight', 'Morning', 
                                                       'Overnight', 'Afternoon', 'Afternoon',
                                                       'Afternoon', 'Morning', 'Evening',
                                                       'Morning'])
    count_sorted_hours1 = analytics.count_sorted_hours(['Overnight', 'Evening', 'Evening', 'Overnight'])
    assert count_sorted_hours == {'Morning': 4, 'Afternoon': 3, 'Evening': 4, 'Overnight': 5}
    assert count_sorted_hours1 == {'Evening': 2, 'Overnight': 2}




    





