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
@patch('menu.input', return_value = 1)
def test_check_off(mock_db_data, mock_input):
    assert menu.check_off() == """   
                 ------------------------------------------   
                                Good job!       
                              Yoga ✔ is done.
                 ------------------------------------------ 
                 """
#         """
#         Record the date and time in the trackings table when
#         the user enters the id of the habit to be marked as done.
#         """
#         # Clean up the console
#         self.clear_console()
#         # Prints the name of the application and instructions to the main menu
#         self.back_to_menu_info()
#         print("""
#                             CHECK A HABIT OFF    
#             ________________________________________________
#                             Time to improve!!
#             ------------------------------------------------
#             """)
        
#         # A list of the existing information in the habit table of the DB
#         habits_info = self.analytics.habits_table()
#         # [(1, 'Yoga', 'daily', 'Be more flexible', 'Morning if possible', '2021-05-05')]
#         # A list with all habit identifiers
#         ids = self.analytics.get_all_ids(habits_info)
            
#         while True:
#             print(
#                 """                          
#                  Which habit do you want to check-off?"""
#                 )
#             # display a table with all the registered habits
#             self.table_registered_habits()
#             print('')
#             id_n = pyip.inputNum("Choose the ID of your habit ")
#             if id_n == 0:
#                 # back to the main menu
#                 self.run()
#             elif id_n in ids:
#                 # Insert the day and time when the habit is checked-off
#                 self.analytics.insert_day(id_n)
#                 print(
#                     """   
#                  ------------------------------------------   
#                                 Good job!       
#                               {} ✔ is done.
#                  ------------------------------------------ 
#                  """.format(
#                  # Selects the habit name from the row that corresponds to the id
#                  self.analytics.select_rows(habits_info, 0, id_n)[0][1])
#                  )
#                 if len(habits_info) > 1:
#                     # Return to the main menu or check another habit
#                     self.choice_stay_return('Check another habit off', self.check_off)
#                 else:
#                     # Return to the main menu by selecting the number zero
#                     self.return_menu()
#             else:
#                 print("Please, choose an ID from the list")




# # def test_add_habit():
    

#     # def add_habit(self):
#     #     """
#     #     Allows the user to enter the name, periodicity, motivation,
#     #     and description of the habit to be recorded.
#     #     """
#     #     # Clean up the console
#     #     self.clear_console()
#     #     # Prints the name of the application and instructions to the main menu
#     #     self.back_to_menu_info()
#     #     print("""
#     #                          ADD A HABIT    
#     #         ________________________________________________
#     #         """)

#     #     # A list of names of registered habits
#     #     habits_names = self.analytics.select_column(self.analytics.habits_table(), 1)
#     #     # ['Yoga']
        
#     #     if len(habits_names) == 0:
#     #          print(
#     #         """
#     #         ----------------Your first habit ---------------
#     #         """)
#     #     else:
#     #         # List of the names and ids of the registered habits in table format
#     #         self.table_registered_habits()
               
#     #     while True:
#     #         try:
#     #             name_to_check = input("""
#     #         Write the name of the habit you want to add """).title()
                
#     #             if name_to_check not in habits_names:
#     #                 if name_to_check == '':
#     #                     print("Please, write the name of your habit")
#     #                 elif name_to_check.isdigit():
#     #                     if (int(name_to_check) == 0):
#     #                         # Clean up the console
#     #                         self.clear_console()
#     #                         # Gives the options that can be selected in the menu
#     #                         self.run()
#     #                     else:
#     #                         break
#     #                 else:
#     #                     name = name_to_check
#     #                     break
#     #             else:
#     #                 print('This habit is already in your list')
                    
#     #         except ValueError:
#     #             pass

#     #     while True:
    #         print("""
    #               How often you want to do this activity?
              
    #               1: daily
    #               2: weekly
    #               """)

    #         periodicity = pyip.inputNum('Choose a number: ')
        
    #         if periodicity == 1:
    #             periodicity = 'daily'
    #             break
    #         elif periodicity == 2:
    #             periodicity = 'weekly'
    #             break
    #         elif periodicity == 0:
    #             # Clean up the console
    #             self.clear_console()
    #             # Gives the options that can be selected in the menu
    #             self.run()
    #         else:
    #             print('Please, choose number 1 or 2 or \nzero to go back to the menu')
                
    #     while True:
    #         motivation = input("Your motivation: ")
    #         if motivation.isdigit():
    #             if int(motivation) == 0:
    #                 # Clean up the console
    #                 self.clear_console()
    #                 # Gives the options that can be selected in the menu
    #                 self.run()
    #             else:
    #                 break
    #         else:
    #             motivation = motivation.capitalize()
    #             break
                
    #     while True:
    #         description = input('Description: ')
    #         if description.isdigit():
    #             if int(description) == 0:
    #                 # Clean up the console
    #                 self.clear_console()
    #                 # Gives the options that can be selected in the menu
    #                 self.run()
    #             else:
    #                 break
    #         else:
    #             description = description.capitalize()
    #             break
            
    #     # insert a habit to the DB            
    #     self.analytics.insert_habit(name, periodicity, motivation, description)        
    #     # Clean up the console
    #     self.clear_console()
    #     # Select the row that contains the information of the newly added habit
    #     # [(3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21')]
    #     added_habit = self.analytics.select_rows(self.analytics.habits_table(), 
    #                                1, name)
    #     # Displays a table with header and column names and information of the added habit
    #     self.display_table(('ID', 'HABIT', 'PERIODICITY', 'MOTIVATION', 'DESCRIPTION', 'CREATION DAY'), 
    #                                 added_habit, 
    #                                 'ADDED HABIT')
    #     # Return to the main menu or adds another habit
    #     self.choice_stay_return('Add another habit', self.add_habit)