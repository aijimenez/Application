# from unittest.mock import patch
# from application.analytics import Analytics
# from application.menu import Menu



# menu = Menu()
# analytics = Analytics()

# @patch('analytics.habits_table', return_value = [
#     (1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-20'), 
#     (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21'), 
#     (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-23'), 
#     (5, 'Try Sth New', 'weekly', 'Living new experiences', 'A new activity', '2021-07-28')
#     ])
# @patch('builtins.input', return_value = 1)
# def test_check_off(mock_input, mock_db_data):
#     assert menu.check_off() == """   
#                   ------------------------------------------   
#                                 Good job!       
#                               Yoga ✔ is done.
#                   ------------------------------------------ 
#                   """
