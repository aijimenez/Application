from application.analytics import Analytics
from datetime import datetime

habits_info_table = [(1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-20'), 
               (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21'), 
               (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-22')]

trackings_table = [(1, '2021-07-21', '09:06'), (3, '2021-07-21', '15:26'), 
                   (3, '2021-07-21', '16:00'), (1, '2021-07-22', '17:11')]

habits_trackings_table = [(1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-21', '09:06'), 
                          (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '15:26'), 
                          (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21', '16:00'), 
                          (1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-22', '17:11')]

analytics = Analytics()
trackings = [(1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-21', '09:06'), 
             (1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-22', '17:11')]

column = 5

def test_get_all_ids():
    ids = analytics.get_all_ids(habits_info_table)
    assert ids == [1, 3, 4]
    
def test_start_date():
    start_date = analytics.start_habit(trackings, column)
    assert start_date == datetime.strptime('2021-07-21', "%Y-%m-%d").date()
    # assert start_date == 5
    # Error assert datetime.date(2021, 7, 21) == 5
