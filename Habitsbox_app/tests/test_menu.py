from unittest.mock import patch
from application.analytics import Analytics
from application.menu import Menu



menu = Menu()
analytics = Analytics()





@patch('analytics.habits_table', return_value = [
    (1, 'Yoga', 'daily', 'Be more flexible', 'Preferably in the morning', '2021-07-20'), 
    (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21'), 
    (4, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-23'), 
    (5, 'Try Sth New', 'weekly', 'Living new experiences', 'A new activity', '2021-07-28')
    ])
@patch('builtins.input', return_value = 1)
def test_check_off(mock_db_data, mock_input):
    assert menu.check_off() == """   
                 ------------------------------------------   
                                Good job!       
                              Yoga ✔ is done.
                 ------------------------------------------ 
                 """


    # def check_off(self):
    #     """
    #     Record the date and time in the trackings table when
    #     the user enters the id of the habit to be marked as done.
    #     """
    #     # Clean up the console
    #     self.clear_console()
    #     # Prints the name of the application and instructions to the main menu
    #     self.back_to_menu_info()
    #     print("""
    #                         CHECK A HABIT OFF    
    #         ________________________________________________
    #                         Time to improve!!
    #         ------------------------------------------------
    #         """)
        
    #     # A list of the existing information in the habit table of the DB
    #     habits_info = self.analytics.habits_table()
    #     # [(1, 'Yoga', 'daily', 'Be more flexible', 'Morning if possible', '2021-05-05')]
    #     # A list with all habit identifiers
    #     ids = self.analytics.get_all_ids(habits_info)
            
    #     while True:
    #         print(
    #             """                          
    #              Which habit do you want to check-off?"""
    #             )
    #         # display a table with all the registered habits
    #         self.table_registered_habits()
    #         print('')
    #         id_n = pyip.inputNum("Choose the ID of your habit ")
    #         if id_n == 0:
    #             # back to the main menu
    #             self.run()
    #         elif id_n in ids:
    #             # Insert the day and time when the habit is checked-off
    #             self.analytics.insert_day(id_n)
    #             print(
    #                 """   
    #              ------------------------------------------   
    #                             Good job!       
    #                           {} ✔ is done.
    #              ------------------------------------------ 
    #              """.format(
    #              # Selects the habit name from the row that corresponds to the id
    #              self.analytics.select_rows(habits_info, 0, id_n)[0][1])
    #              )
    #             if len(habits_info) > 1:
    #                 # Return to the main menu or check another habit
    #                 self.choice_stay_return('Check another habit off', self.check_off)
    #             else:
    #                 # Return to the main menu by selecting the number zero
    #                 self.return_menu()
    #         else:
    #             print("Please, choose an ID from the list")