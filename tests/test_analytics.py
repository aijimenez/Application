"""
Analytics module functions are tested using
different data sets.
"""
from datetime import timedelta, date, time
from Habitsbox_app.application.analytics import Analytics


analytics = Analytics()

habits_table = [(1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-20'),
                (2, 'Play Piano', 'daily', 'Learn more songs', 'Minimum one hour', '2021-07-21'),
                (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21'),
                (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-22'),
                (5, 'Try Sth New', 'weekly', 'Experiences', 'A new activity', '2021-07-28')]

trackings_table = [(1, '2021-07-21', '09:06'), (3, '2021-07-21', '15:26'),
                   (3, '2021-07-21', '16:00'), (1, '2021-07-22', '17:11')]

habits_trackings_table = [
    (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-21', '09:06'),
    (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-21', '14:44'),
    (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '15:26'),
    (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-22', '16:00'),
    (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-22', '17:11'),
    (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-28', '14:56'),
    (5, 'Try Sth New', 'weekly', 'Experiences', 'A new activity', '2021-07-28', '11:56'),
    (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-28', '14:56')]

info_trackings_yoga = [
    (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-21', '09:06'),
    (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-22', '17:11'),
    (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-23', '17:11')]

ID_1_Week = [(1, '2019-12-24', '09:52'), (1, '2019-12-29', '03:42'),
             (1, '2019-12-31', '03:42'), (1, '2020-01-07', '18:00'),
             (1, '2020-01-16', '19:52'), (1, '2020-01-28', '02:42'),
             (1, '2020-02-01', '19:52'), (1, '2020-02-03', '02:42'),
             (1, '2020-02-03', '08:25'), (1, '2020-02-11', '00:14'),
             (1, '2020-02-11', '12:28'), (1, '2020-02-11', '17:07'),
             (1, '2020-02-12', '16:09'), (1, '2020-03-01', '06:59'),
             (1, '2020-03-10', '21:32'), (1, '2020-03-14', '06:59')]

dates_weekly = [('2019-12-24'), ('2019-12-29'), ('2019-12-31'), ('2020-01-07'),
                ('2020-01-16'), ('2020-01-28'), ('2020-02-01'), ('2020-02-03'),
                ('2020-02-03'), ('2020-02-11'), ('2020-02-11'), ('2020-02-11'),
                ('2020-02-12'), ('2020-03-01'), ('2020-03-10'), ('2020-03-14')]

ID_2_daily = [(2, '2020-02-18', '09:52'), (2, '2020-02-18', '03:42'),
              (2, '2020-02-18', '03:42'), (2, '2020-02-19', '18:00'),
              (2, '2020-02-25', '19:52'), (2, '2020-02-26', '02:42'),
              (2, '2020-02-27', '19:52'), (2, '2020-02-27', '02:42'),
              (2, '2020-02-29', '08:25'), (2, '2020-03-01', '00:14'),
              (2, '2020-03-02', '12:28'), (2, '2020-03-03', '17:07'),
              (2, '2020-03-04', '16:09'), (2, '2020-03-04', '06:59'),
              (2, '2020-03-11', '21:32'), (2, '2020-03-12', '06:59'),
              (2, '2020-03-13', '21:32'), (2, '2020-03-14', '06:59')]


def test_select_column():
    """
    Select a column of the indicated table.
    """
    names_habits_table = analytics.select_column(habits_table, 1)
    ids_habits = analytics.select_column(habits_table, 0)
    ids_trackings = analytics.select_column(trackings_table, 0)
    dates = analytics.select_column(ID_1_Week, 1)
    col_dates = analytics.select_column([(1, '2019-12-24', '09:52'),
                                      (1, '2019-12-29', '03:42')], 1)
    assert names_habits_table == ['Yoga', 'Play Piano', 'Read', 'Run', 'Try Sth New']
    assert ids_habits == [1, 2, 3, 4, 5]
    assert ids_trackings == [1, 3, 3, 1]
    assert dates == dates_weekly
    assert col_dates == ['2019-12-24', '2019-12-29']

def test_select_columns():
    """
    Select several columns of the indicated table.
    """
    ids_names = analytics.select_columns(habits_table, stop = 2)
    names_periodicity = analytics.select_columns(trackings_table, start = 1, stop = 3)
    names_trackings_one_habit = analytics.select_columns(info_trackings_yoga, start = 1, stop = 2)
    assert ids_names == [(1, 'Yoga'), (2, 'Play Piano'),
                         (3, 'Read'), (4, 'Run'), (5, 'Try Sth New')]
    assert names_periodicity == [('2021-07-21', '09:06'), ('2021-07-21', '15:26'),
                                 ('2021-07-21', '16:00'), ('2021-07-22', '17:11')]
    assert names_trackings_one_habit == [('Yoga',), ('Yoga',), ('Yoga',)]

def test_get_all_ids():
    """
    First column of a table in a list.
    """
    ids_habits = analytics.get_all_ids(habits_table)
    ids_trackings = analytics.get_all_ids(trackings_table)
    assert ids_habits == [1, 2, 3, 4, 5]
    assert ids_trackings == [1, 3, 3, 1]

def test_unique_ids():
    """
    Unique ids of a table
    """
    unique_ids = analytics.unique_ids(habits_trackings_table)
    assert unique_ids == [1, 4, 3, 5]

def test_ids_without_trackings():
    """
    All habit ids that have no trackings.
    """
    ids_without_trackings = analytics.ids_without_trackings(habits_table, habits_trackings_table)
    no_ids_without_trackings = analytics.ids_without_trackings(
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-20'),
         (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21')],
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-21', '09:06'),
         (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '15:26'),
         (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-22', '16:00')])
    assert ids_without_trackings == [2]
    assert no_ids_without_trackings == []

def test_ids_with_trackings():
    """
    All habit ids that have trackings.
    """
    ids_with_trackings = analytics.ids_with_trackings(habits_table, [2])
    all_ids_with_trackings = analytics.ids_with_trackings(
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-20'),
         (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21')],
        [])
    assert ids_with_trackings == [1, 3, 4, 5]
    assert all_ids_with_trackings == [1, 3]

def test_select_rows():
    """
    Select all rows with the same feature.
    """
    rows_name = analytics.select_rows(habits_table, 1, 'Yoga')
    rows_id = analytics.select_rows(habits_trackings_table, 0, 3)
    rows_periodicity = analytics.select_rows(habits_table, 2, 'daily')
    assert rows_name == [
        (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-20')
        ]
    assert rows_id == [
        (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '15:26'),
        (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-22', '16:00')
        ]
    assert rows_periodicity == [
        (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-20'),
        (2, 'Play Piano', 'daily', 'Learn more songs', 'Minimum one hour', '2021-07-21'),
        (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21')
        ]

def test_display_elements():
    """
    Each item in the list is separated by a separator.
    """
    names_new_lines = analytics.display_elements(['Yoga', 'Read', 'Run'])
    names_comma = analytics.display_elements(['Yoga', 'Read', 'Run'], ', ')
    assert names_new_lines == 'Yoga\nRead\nRun'
    assert names_comma == 'Yoga, Read, Run'

def test_unique_data():
    """
    Give unique values from a list of data.
    """
    unique_times = analytics.unique_data([date(2021, 7, 21), date(2021, 7, 21),
                                          date(2021, 7, 21), date(2021, 7, 22)])
    unique_cw = analytics.unique_data([52, 52, 1, 2, 3, 5, 5, 6, 6, 7, 7, 7, 7, 9, 11, 11])
    assert unique_times == [date(2021, 7, 21), date(2021, 7, 22)]
    assert unique_cw == [52, 1, 2, 3, 5, 6, 7, 9, 11]

def test_display_unique_elements():
    """
    Unique elements of a column are
    separated by commas in a string.
    """
    unique = analytics.display_unique_elements(habits_trackings_table, 1)
    assert unique == 'Yoga, Run, Read, Try Sth New'

def test_format_to_date():
    """
    Items are converted to datetime.date.
    """
    dates = analytics.format_to_date([('2021-07-21'), ('2021-07-21'),
                                      ('2021-07-21'), ('2021-07-22')])
    dates_id1_week = analytics.format_to_date(dates_weekly)
    assert list(dates) == [date(2021, 7, 21), date(2021, 7, 21),
                      date(2021, 7, 21), date(2021, 7, 22)]
    assert list(dates_id1_week) ==  [date(2019, 12, 24), date(2019, 12, 29), date(2019, 12, 31),
                                      date(2020, 1, 7), date(2020, 1, 16), date(2020, 1, 28),
                                      date(2020, 2, 1), date(2020, 2, 3), date(2020, 2, 3),
                                      date(2020, 2, 11), date(2020, 2, 11), date(2020, 2, 11),
                                      date(2020, 2, 12), date(2020, 3, 1), date(2020, 3, 10),
                                      date(2020, 3, 14)]

def test_format_to_time():
    """
    Items are converted to datetime.time.
    """
    times = analytics.format_to_time([('09:52'), ('03:42'), ('03:42'), ('18:00'),
                                      ('19:52'), ('02:42'), ('19:52'), ('02:42'),
                                      ('08:25'), ('00:14'), ('12:28'), ('17:07'),
                                      ('16:09'),  ('06:59'), ('21:32'), ('06:59')])
    assert list(times) == [time(9, 52), time(3, 42), time(3, 42), time(18, 0),
                           time(19, 52), time(2, 42), time(19, 52), time(2, 42),
                           time(8, 25), time(0, 14), time(12, 28), time(17, 7),
                           time(16, 9), time(6, 59), time(21, 32), time(6, 59)]

def test_to_calender_week():
    """
    Give the calendar week number for each date.
    """
    calender_week = analytics.to_calender_week([date(2019, 12, 31), date(2020, 1, 1),
                                                date(2020, 12, 31), date(2021, 12, 25)])
    cw_dec_march = analytics.to_calender_week(
        [date(2019, 12, 24), date(2019, 12, 29), date(2019, 12, 31),
         date(2020, 1, 7), date(2020, 1, 16), date(2020, 1, 28),
         date(2020, 2, 1), date(2020, 2, 3), date(2020, 2, 3),
         date(2020, 2, 11), date(2020, 2, 11), date(2020, 2, 11),
         date(2020, 2, 12), date(2020, 3, 1), date(2020, 3, 10),
         date(2020, 3, 14)]
        )
    assert list(calender_week) == [1, 1, 53, 51]
    assert list(cw_dec_march) == [52, 52, 1, 2, 3, 5, 5, 6, 6, 7, 7, 7, 7, 9, 11, 11]

def test_zipping_unique_data():
    """
    A list is sliced into one list without the first element
    and into another list without the last element.
    The first elements of each list are matched in a tuple,
    then the second and so on.
    """
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
    """
    Differences between numbers or dates.
    """
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
    """
    Number of days from a datetime.timedelta object.
    """
    diff_days = analytics.difference_in_days([timedelta(days=2),
                                              timedelta(days=2),
                                              timedelta(days=1)])
    assert list(diff_days) == [2, 2, 1]

def test_dif_5152_to_1():
    """
    Change the number to 1 if the number in the list
    is -51 o -52.
    """
    differences_to_1 = analytics.dif_5152_to_1([-51, 1, 1, 2, 1, 1, 2, -52])
    assert list(differences_to_1) == [1, 1, 1, 2, 1, 1, 2, 1]

def unpacking_group_diff(grouping_differences):
    """
    Unpack a itertools.groupby object
    """
    return [[key, list(group)] for key, group in grouping_differences]

def test_grouping_differences():
    """
    Same numbers are grouped and designed to a key.
    A new group is formed each time the number(key)
    changes.
    """
    grouping_cw = analytics.grouping_differences([1, 1, 1, 2, 1, 1, 2, 2])
    assert unpacking_group_diff(grouping_cw) == [[1, [1, 1, 1]],
                                                  [2, [2]],
                                                  [1, [1, 1]],
                                                  [2, [2, 2]]]

def test_streaks():
    """
    Count the number of items contained in the group
    if the key is the number one.
    """
    streaks = analytics.streaks([[1, [1, 1, 1]], [2, [2]], [1, [1, 1]], [2, [2, 2]]])
    assert streaks == [3, 2]

def test_longest_streak():
    """
    Give the maximum number in a list of numbers.
    If the list is empty, returns the number one.
    """
    longest_streak = analytics.longest_streak([3, 2])
    longest_streak_empty_list = analytics.longest_streak([])
    assert longest_streak == 4
    assert longest_streak_empty_list == 1

def test_longest_streak_periodicity():
    """
    The longest streak of a habit depending on
    the habit's periodicity.
    """
    longest_streak_weekly = analytics.longest_streak_periodicity(ID_1_Week, 'weekly', 1)
    longest_streak_daily = analytics.longest_streak_periodicity(ID_2_daily, 'daily', 1)
    longest_streak_yoga = analytics.longest_streak_periodicity(info_trackings_yoga, 'daily')
    empty_table = []
    assert longest_streak_weekly == 4
    assert longest_streak_daily == 5
    assert longest_streak_yoga == 3
    assert empty_table == []

def test_start_date():
    """
    The earliest date from a column of dates.
    """
    start_date = analytics.start_habit(info_trackings_yoga, 5)
    start_dates_unordered = analytics.start_habit(
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-25', '09:06'),
         (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-21', '17:11'),
         (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-23', '17:11')],
        )
    empty_table = analytics.start_habit([])
    assert start_date == date(2021, 7, 21)
    assert start_dates_unordered == date(2021, 7, 21)
    assert empty_table == []

def test_last_day():
    """
    The most recent date in a column of dates.
    """
    last_day = analytics.last_day(info_trackings_yoga, 5)
    empty_table = analytics.last_day([], 5)
    assert last_day == date(2021, 7, 23)
    assert empty_table == []

def test_activity():
    """
    Return the number of days or weeks in which the habit
    has been checked off, depending on whether the habit
    is weekly or daily.
    """
    activity_weekly = analytics.activity('weekly', ID_1_Week, 1)
    activity_daily = analytics.activity('daily', ID_2_daily, 1)
    assert activity_weekly == 9
    assert activity_daily == 14

def test_only_hours():
    """
    Get hours without minutes
    """
    hours = analytics.only_hours([time(9, 52), time(3, 42), time(3, 42), time(18, 0),
                                  time(19, 52), time(2, 42), time(19, 52), time(2, 42),
                                  time(8, 25), time(0, 14), time(12, 28), time(17, 7),
                                  time(16, 9), time(6, 59), time(21, 32), time(6, 59)])
    assert list(hours) == [9, 3, 3, 18, 19, 2, 19, 2, 8, 0, 12, 17, 16, 6, 21, 6]

def test_sort_hours():
    """
    Each hour is renamed according to the part of the
    day it corresponds to.
    """
    sort_hours = analytics.sort_hours([9, 3, 3, 18, 19, 2, 19, 2, 8, 0, 12, 17, 16, 6, 21, 6])
    extrem_hours = analytics.sort_hours([5, 12, 18, 24])
    assert list(sort_hours) == ['Morning', 'Overnight', 'Overnight', 'Evening', 'Evening',
                                'Overnight', 'Evening', 'Overnight', 'Morning', 'Overnight',
                                'Afternoon', 'Afternoon', 'Afternoon', 'Morning', 'Evening',
                                'Morning']
    assert list(extrem_hours) == ['Morning', 'Afternoon', 'Evening', 'Overnight']

def test_count_sorted_hours():
    """
    Count the number of times the words of the parts
    of the day appear.
    """
    count_sorted_hours = analytics.count_sorted_hours(['Morning', 'Overnight', 'Overnight',
                                                       'Evening', 'Evening', 'Overnight',
                                                       'Evening', 'Overnight', 'Morning',
                                                       'Overnight', 'Afternoon', 'Afternoon',
                                                       'Afternoon', 'Morning', 'Evening',
                                                       'Morning'])
    assert count_sorted_hours == {'Morning': 4, 'Afternoon': 3, 'Evening': 4, 'Overnight': 5}

def test_active_time_dict():
    """
    A dictionary whose keys are the parts of the day
    (Morning, Afternoon, Evening and Overnight) in which a
    habit was checked and whose values indicate how often
    the activity is performed in these parts of the day.
    """
    active_time_id1 = analytics.active_time_dict(ID_1_Week, 2)
    active_time_yoga = analytics.active_time_dict(
        [
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-06-26', '20:09'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-06-27', '10:44'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-06-29', '08:25'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-06-30', '05:54'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'A low-impact activity', '2021-07-01', '07:17')
        ]
        )
    assert active_time_id1 == {'Morning': 4, 'Afternoon': 3, 'Evening': 4, 'Overnight': 5}
    assert active_time_yoga == {'Morning': 4, 'Evening': 1}

def test_max_value():
    """
    The highest value from a dictionary.
    """
    max_value = analytics.max_value({'Morning': 4, 'Afternoon': 3, 'Evening': 4, 'Overnight': 5})
    empty_dic = analytics.max_value({})
    assert max_value == 5
    assert empty_dic == {}

def test_most_active_time():
    """
    Get the dictionary key(s) with the maximum value.
    """
    most_active_time = analytics.most_active_time(
        {'Morning': 4, 'Afternoon': 3, 'Evening': 4, 'Overnight': 5}, 5)
    empty_dic = analytics.max_value({})
    several_active_times = analytics.most_active_time(
        {'Morning': 4, 'Afternoon': 3, 'Evening': 4, 'Overnight': 2}, 4)
    assert most_active_time == ['Overnight']
    assert empty_dic == {}
    assert several_active_times == ['Morning', 'Evening']

def test_unique_ids_periodicity():
    """
    Get the ids of the habits with the same periodicity.
    """
    unique_ids_daily = analytics.unique_ids_periodicity(habits_trackings_table, 2, 'daily')
    unique_ids_weakly = analytics.unique_ids_periodicity(habits_trackings_table, 2, 'weekly')
    assert unique_ids_daily == [1, 3]
    assert unique_ids_weakly == [4, 5]

def test_grouped_habits():
    """
    Habits grouped by id.
    """
    grouped_habits_daily = analytics.grouped_habits(habits_trackings_table, [1, 3])
    grouped_habits_weekly = analytics.grouped_habits(habits_trackings_table, [1, 5])
    assert grouped_habits_daily == [
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-21', '09:06'),
         (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-22', '17:11'),
         (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-28', '14:56')],
        [(3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '15:26'),
         (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-22', '16:00')]
        ]
    assert grouped_habits_weekly == [
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-21', '09:06'),
         (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-22', '17:11'),
         (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-28', '14:56')],
        [(5, 'Try Sth New', 'weekly', 'Experiences', 'A new activity', '2021-07-28', '11:56')]
        ]

def test_lists_periodicity():
    """
    Information and trackings of the habits with the same
    periodicity are grouped together by id.
    """
    list_daily = analytics.lists_periodicity(habits_trackings_table, 2, 'daily')
    list_weekly = analytics.lists_periodicity(habits_trackings_table, 2, 'weekly')
    assert list_daily == [
        [
            (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-21', '09:06'),
            (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-22', '17:11'),
            (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-28', '14:56')
        ],
        [
            (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '15:26'),
            (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-22', '16:00')
            ]
        ]
    assert list_weekly == [
        [(4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-21', '14:44'),
         (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-28', '14:56')],
        [(5, 'Try Sth New', 'weekly', 'Experiences', 'A new activity', '2021-07-28', '11:56')]
        ]

def test_periodicity_info():
    """
    A list containing information on each habit according
    to its periodicity. ID and name of the habit, date of
    the first and last tracking, part of the day when the
    user is most active to perform this habit, days or weeks
    of activity, and the longest streak.
    """
    daily_info = analytics.periodicity_info(
        [
            [
                (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-21', '09:06'),
                (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-22', '17:11'),
                (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-28', '14:56')
            ],
            [
                (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '15:26'),
                (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-22', '16:00')
                ]
            ],
        'daily')
    weekly_info = analytics.periodicity_info(
        [
            [
                (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-21', '14:44'),
                (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-28', '14:56')
            ],
            [
                (5, 'Try Sth New', 'weekly', 'Experiences', 'A new activity', '2021-07-28', '11:56')
                ]
            ],
        'weekly')
    assert daily_info == [('1', 'Yoga', '2021-07-21', '2021-07-28', 'Afternoon', 3, 2),
                          ('3', 'Read', '2021-07-21', '2021-07-22', 'Afternoon', 2, 2)]
    assert weekly_info == [('4', 'Run', '2021-07-21', '2021-07-28', 'Afternoon', 2, 2),
                            ('5', 'Try Sth New', '2021-07-28', '2021-07-28', 'Morning', 1, 1)]

def test_lists_both_periodicities():
    """
    Habits are separated according to periodicity.
    Information and trackings of each habit are grouped together.
    """
    lists_both_periodicities = analytics.lists_both_periodicities(habits_trackings_table)
    assert lists_both_periodicities == [
        [
            [(1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-21', '09:06'),
             (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-22', '17:11'),
             (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-28', '14:56')
             ],
            [(3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '15:26'),
             (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-22', '16:00')
             ]
        ],
        [
            [(4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-21', '14:44'),
             (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-28', '14:56')
             ],
            [(5, 'Try Sth New', 'weekly', 'Experiences', 'A new activity', '2021-07-28', '11:56')
             ]
        ]]

def test_both_periodicities_info():
    """
    Habits separated by periodicity with general information
    about each habit.
    """
    both_periodicities_info = analytics.both_periodicities_info([
        [
            [(1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-21', '09:06'),
             (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-22', '17:11'),
             (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-28', '14:56')
             ],
            [(3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '15:26'),
             (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-22', '16:00')
             ]
        ],
        [
            [(4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-21', '14:44'),
             (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-28', '14:56')
             ],
            [(5, 'Try Sth New', 'weekly', 'Experiences', 'A new activity', '2021-07-28', '11:56')
             ]
        ]])
    assert both_periodicities_info == [
        [('1', 'Yoga', '2021-07-21', '2021-07-28', 'Afternoon', 3, 2),
         ('3', 'Read', '2021-07-21', '2021-07-22', 'Afternoon', 2, 2)],
        [('4', 'Run', '2021-07-21', '2021-07-28', 'Afternoon', 2, 2),
         ('5', 'Try Sth New', '2021-07-28', '2021-07-28', 'Morning', 1, 1)]]


def test_info_all_habits():
    """
    Information on the habits separated by periodicity
    is merged into a single list.
    """
    info_habits = analytics.info_all_habits(
        [
            [
                ('1', 'Yoga', '2021-07-21', '2021-07-28', 'Afternoon', 3, 2),
                ('3', 'Read', '2021-07-21', '2021-07-22', 'Afternoon', 2, 2)
            ],
            [
                ('4', 'Run', '2021-07-21', '2021-07-28', 'Afternoon', 2, 2),
                ('5', 'Try Sth New', '2021-07-28', '2021-07-28', 'Morning', 1, 1)
            ]
        ]
        )
    assert info_habits == [
        ('1', 'Yoga', '2021-07-21', '2021-07-28', 'Afternoon', 3, 2),
        ('3', 'Read', '2021-07-21', '2021-07-22', 'Afternoon', 2, 2),
        ('4', 'Run', '2021-07-21', '2021-07-28', 'Afternoon', 2, 2),
        ('5', 'Try Sth New', '2021-07-28', '2021-07-28', 'Morning', 1, 1)
        ]

def test_tracked_habits():
    """
    Habits with trackings and their information from
    the habits table of the DB.
    """
    tracked_habits = analytics.tracked_habits(habits_table,
                                              habits_trackings_table)
    assert tracked_habits == [
        (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport', '2021-07-20'),
        (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-22'),
        (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21'),
        (5, 'Try Sth New', 'weekly', 'Experiences', 'A new activity', '2021-07-28')]

def test_habits_without_trackings():
    """
    Untracked habits and their information from
    the habits table of the DB.
    """
    untracked_habits = analytics.habits_without_trackings(habits_table,
                                                          [2])
    assert untracked_habits == [
        (2, 'Play Piano', 'daily', 'Learn more songs', 'Minimum one hour', '2021-07-21')]

def test_habit_info_longest_streak():
    """
    Information of the habit(s) that has(have) the
    maximum streak.
    """
    habit_info_longest_streak = analytics.habit_info_longest_streak(habits_trackings_table)
    one_habit_info_longest_streak = analytics.habit_info_longest_streak(info_trackings_yoga)
    assert habit_info_longest_streak == [
        ('1', 'Yoga', '2021-07-21', '2021-07-28', 'Afternoon', 3, 2),
        ('3', 'Read', '2021-07-21', '2021-07-22', 'Afternoon', 2, 2),
        ('4', 'Run', '2021-07-21', '2021-07-28', 'Afternoon', 2, 2)
        ]
    assert one_habit_info_longest_streak == [
        ('1', 'Yoga', '2021-07-21', '2021-07-23', 'Afternoon', 3, 3)
        ]

def test_name_habit_longest_streak():
    """
    Give the name(s) of the habit(s) with the longest streak
    and the streak.
    """
    names_habits_streaks = analytics.name_habit_longest_streak([
        ('1', 'Yoga', '2021-07-21', '2021-07-28', 'Afternoon', 3, 2),
        ('3', 'Read', '2021-07-21', '2021-07-22', 'Afternoon', 2, 2),
        ('4', 'Run', '2021-07-21', '2021-07-28', 'Afternoon', 2, 2)
        ])
    one_name_streak =  analytics.name_habit_longest_streak(
        [('1', 'Yoga', '2021-07-21', '2021-07-23', 'Afternoon', 3, 3)]
        )
    assert names_habits_streaks == [('Yoga', 2), ('Read', 2), ('Run', 2)]
    assert one_name_streak == [('Yoga', 3)]

def test_lengths():
    """
    Length of each element
    """
    lengths = analytics.lengths(habits_table)
    assert lengths == [[1, 4, 5, 16, 16, 10],
                        [1, 10, 5, 16, 16, 10],
                        [1, 4, 5, 20, 10, 10],
                        [1, 3, 6, 9, 11, 10],
                        [1, 11, 6, 11, 14, 10]]

def test_max_lengths():
    """
    The longest lengths
    """
    max_lengths = analytics.max_lengths([
        [1, 4, 5, 16, 16, 10],
        [1, 10, 5, 16, 16, 10],
        [1, 4, 5, 20, 10, 10],
        [1, 3, 6, 9, 11, 10],
        [1, 11, 6, 11, 14, 10]],
        habits_table)
    assert max_lengths == [1, 11, 6, 20, 16, 10]

def test_distance_format():
    """
    Create a string formating that represents
    the distance to be maintained between each
    element.
    """
    distance_format = analytics.distance_format([1, 11, 6, 20, 16, 10])
    assert distance_format == "%-1s    %-11s    %-6s    %-20s    %-16s    %-10s    "

def test_aligned_columns():
    """
    Elements of a table are separated and
    aligned.
    """
    data_with_distances = analytics.aligned_columns(
        "%-1s    %-11s    %-6s    %-20s    %-16s    %-10s    ",
        habits_table)
    assert list(data_with_distances) == [
      '1    Yoga           daily     Be more flexible        Low-impact sport    2021-07-20    ',
      '2    Play Piano     daily     Learn more songs        Minimum one hour    2021-07-21    ',
      '3    Read           daily     Read 12 books a year    Afternoons          2021-07-21    ',
      '4    Run            weekly    Be faster               At weekends         2021-07-22    ',
      '5    Try Sth New    weekly    Experiences             A new activity      2021-07-28    '
        ]

def test_line():
    """
    Create a line by adding the elements of a list
    of numbers (maximum lengths) and the spaces between
    the elements.
    """
    line = analytics.line([1, 4, 6, 20, 25, 10])
    assert line == '__________________________________________________'\
        '________________________________________'

def test_add_colnames():
    """
    Add the names of each column.
    """
    add_colnames = analytics.add_colnames(
        ('ID', 'Habit', 'Periodicity', 'Motivation', 'Description'),
        [(1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport'),
          (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons'),
          (4, 'Run', 'weekly', 'Be faster', 'At weekends'),
          (5, 'Try Sth New', 'weekly', 'Experiences', 'A new activity')])
    assert add_colnames == [
        ('ID', 'Habit', 'Periodicity', 'Motivation', 'Description'),
        (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport'),
        (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons'),
        (4, 'Run', 'weekly', 'Be faster', 'At weekends'),
        (5, 'Try Sth New', 'weekly', 'Experiences', 'A new activity')]

def test_table_line():
    """
    Adjust the length of the line in relation to
    the data in the table.
    """
    table_line = analytics.table_line(
        [('ID', 'Habit', 'Periodicity', 'Motivation', 'Description'),
          (1, 'Yoga', 'daily', 'Be more flexible', 'Low-impact sport'),
          (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons'),
          (4, 'Run', 'weekly', 'Be faster', 'At weekends'),
          (5, 'Try Sth New', 'weekly', 'Experiences', 'A new activity')]
        )
    assert table_line == '_________________________________________________'\
        '_______________________________'
