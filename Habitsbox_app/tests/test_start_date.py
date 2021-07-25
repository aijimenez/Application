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

def test_select_column():
    names_habits_table = analytics.select_column(habits_table, 1)
    ids_habits = analytics.select_column(habits_table, 0)
    ids_trackings = analytics.select_column(trackings_table, 0)
    assert names_habits_table == ['Yoga', 'Read', 'Run']
    assert ids_habits == [1, 3, 4]
    assert ids_trackings == [1, 3, 3, 1]   
    
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
    
def test_start_date():
    start_date = analytics.start_habit(trackings_one_habit, column)
    assert start_date == datetime.strptime('2021-07-21', "%Y-%m-%d").date()

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
    assert dates == [date(2021, 7, 21), date(2021, 7, 21), 
                      date(2021, 7, 21), date(2021, 7, 22)]
    # assert dates == [datetime.strptime('2021-07-21', "%Y-%m-%d").date(),
    #                   datetime.strptime('2021-07-21', "%Y-%m-%d").date(),
    #                   datetime.strptime('2021-07-21', "%Y-%m-%d").date(),
    #                   datetime.strptime('2021-07-22', "%Y-%m-%d").date()]
    
def test_format_to_time():
    times = analytics.format_to_time([('09:06'), ('15:26'), ('16:00'), ('17:11')])
    assert times ==  [time(9, 6), time(15, 26), time(16, 0), time(17, 11)]
    # assert times == [datetime.strptime('09:06', "%H:%M").time(),
    #                  datetime.strptime('15:26', "%H:%M").time(),
    #                  datetime.strptime('16:00', "%H:%M").time(),
    #                  datetime.strptime('17:11', "%H:%M").time()]

def test_to_calender_week():
    calender_week = analytics.to_calender_week(
        [datetime.strptime('2019-12-31', "%Y-%m-%d").date(),
         datetime.strptime('2020-01-01', "%Y-%m-%d").date(),
         datetime.strptime('2020-12-31', "%Y-%m-%d").date(),
         datetime.strptime('2021-12-25', "%Y-%m-%d").date()])
    assert calender_week == [1, 1, 53, 51]

def test_unique_data():
    unique_times = analytics.unique_data(
        [datetime.strptime('2021-07-21', "%Y-%m-%d").date(),
          datetime.strptime('2021-07-21', "%Y-%m-%d").date(),
          datetime.strptime('2021-07-21', "%Y-%m-%d").date(),
          datetime.strptime('2021-07-22', "%Y-%m-%d").date()])
    assert unique_times == [datetime.strptime('2021-07-21', "%Y-%m-%d").date(),
                     datetime.strptime('2021-07-22', "%Y-%m-%d").date()]

def test_zipping_unique_data():
    zip_times = analytics.zipping_unique_data(
        [datetime.strptime('2021-02-01', "%Y-%m-%d").date(),
          datetime.strptime('2021-02-03', "%Y-%m-%d").date(),
          datetime.strptime('2021-02-05', "%Y-%m-%d").date(),
          datetime.strptime('2021-02-06', "%Y-%m-%d").date()])
    zip_times1 = analytics.zipping_unique_data(
        [datetime.strptime('2021-02-01', "%Y-%m-%d").date()])
    assert zip_times == [
        (datetime.strptime('2021-02-03', "%Y-%m-%d").date(), datetime.strptime('2021-02-01', "%Y-%m-%d").date()),
        (datetime.strptime('2021-02-05', "%Y-%m-%d").date(), datetime.strptime('2021-02-03', "%Y-%m-%d").date()),
        (datetime.strptime('2021-02-06', "%Y-%m-%d").date(), datetime.strptime('2021-02-05', "%Y-%m-%d").date())
        ]
    assert zip_times1 == []
    
def test_differences():
    differences = analytics.differences ([
        (datetime.strptime('2021-02-03', "%Y-%m-%d").date(), datetime.strptime('2021-02-01', "%Y-%m-%d").date()),
        (datetime.strptime('2021-02-05', "%Y-%m-%d").date(), datetime.strptime('2021-02-03', "%Y-%m-%d").date()),
        (datetime.strptime('2021-02-06', "%Y-%m-%d").date(), datetime.strptime('2021-02-05', "%Y-%m-%d").date())
        ])
    # assert differences == [1, 2, 3]
    assert differences ==  [timedelta(days=2), 
                            timedelta(days=2), 
                            timedelta(days=1)]
    
    # differences = analytics.differences ([
    #     (datetime.date(2021, 2, 3), datetime.date(2021, 2, 1)),
    #     (datetime.date(2021, 2, 5), datetime.date(2021, 2, 3)),
    #     (datetime.date(2021, 2, 6), datetime.date(2021, 2, 5))
    #     ])
    # assert differences == [datetime.timedelta(days=2), 
    #                         datetime.timedelta(days=2), 
    #                         datetime.timedelta(days=1)]
    
    # differences = analytics.differences ([
    #     (datetime.date(2021, 2, 3), datetime.date(2021, 2, 1)),
    #     (datetime.date(2021, 2, 5), datetime.date(2021, 2, 3)),
    #     (datetime.date(2021, 2, 6), datetime.date(2021, 2, 5))
    #     ])
    # assert differences == [datetime.timedelta(days=2), 
    #                         datetime.timedelta(days=2), 
    #                         datetime.timedelta(days=1)]
    

 





