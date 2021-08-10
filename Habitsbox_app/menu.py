import sys
import pyinputplus as pyip
from operator import itemgetter
# import time

# from analytics import Analytics
from application.analytics import Analytics
#from . import Analytics

class Menu:
    """Show a menu and react to the user options when executed."""
          
    def __init__(self):
        self.analytics = Analytics()
        self.menu_options = { 
            "1": self.add_habit,
            "2": self.check_off,
            "3": self.delete_habit,
            "4": self.see_habit,
            "5": self.show_all_habits,
            "6": self.habits_same_periodicity,
            "7": self.habit_longest_streak,
            "0": self.exit,
           
            }
            
    def display_menu(self):
        """
        Display different menus depending on the number of
        habits and trackings registered in the datebase.
        Adding more options to each menu as these numbers
        increase.
        """

        # Gets the number of habits that exist in the habits table
        number_of_habits = len(self.analytics.habits_table())
        # Gets the number of trackings that exist in the trackings table
        number_of_trackings = len(self.analytics.trackings_table())

        
        # Mismas formular pero con list
        #number_of_habits = len(list(self.analytics.habits_table()))
        #number_of_trackings = len(list(self.analytics.trackings_table()))
                
        print(
            """
            ________________________________________
            
                    WELCOME TO YOUR HABITSBOX       
            ________________________________________
            
                   Everything can be archived 
                with perseverance and commitment
            
            ---------- Let's get started -----------
            
            Choose a number
                
            0. Exit
            ----------------------------------------
            1. Add a new habit
            ----------------------------------------
            """)
        
        if number_of_habits >= 1:
            print(
            """
            2. Check a habit off
            3. Delete a habit
            ----------------------------------------
            """)
            
            if (number_of_trackings == 0) or (number_of_habits == 1):
                print("""
            Analysis -------------------------------
                
            4. See my habit
            ----------------------------------------
                    """)
            elif number_of_trackings >= 1:
                print(
                    """            
            Analysis -------------------------------
                
            4. See a habit
            5. See all habits registered
            6. See habits with same periodicity
            7. See my longest streak
            
            ----------------------------------------
                  """)
            
    
    def run(self):
        """
        Restricts or increases the options that can be selected
        by the user and reacts to the selected number.
        """
        
        # Gets the number of habits that exist in the habits table
        number_of_habits = len(self.analytics.habits_table())
        # Gets the number of trackings that exist in the trackings table
        number_of_trackings = len(self.analytics.trackings_table())
        
        while True:
            # Display a menu depending on the number of habits and trackings
            self.display_menu()
            choice = pyip.inputNum("Enter an number: ")
            if (number_of_habits == 0) and (choice in [0, 1]):
                action = self.menu_options.get(str(choice))
                action()
            elif (number_of_habits >=1) and (choice in [0, 1, 2, 3]):
                action = self.menu_options.get(str(choice))
                action()
            elif ((number_of_trackings == 0) or (number_of_habits == 1)) and (choice in [0, 1, 2, 3, 4]):
                action = self.menu_options.get(str(choice))
                action()
            elif (number_of_trackings >= 1) and (choice in [0, 1, 2, 3, 4, 5, 6, 7]):
                action = self.menu_options.get(str(choice))
                action()
            else:
                print('Choose a number from the list')
                                                 
    def back_to_menu_info(self):
        """
        Displays the name of the application and indicates which
        key to press to return to the main menu.
        """
        print(
            """
            ________________________________________________
            
                              HABITSBOX       
            ________________________________________________
            Hint: Press 0 (zero) to return to the main menu
            ------------------------------------------------""")

    def choice_stay_return(self, text, action):
        """
        Asks the user if he/she wants to 
        return to the main menu or to perform the action
        indicated in number 1.
        """
        while True:
            print("""
                  0. Back to the main menu
                  1. {}
                  """.format(text))
            choice = pyip.inputNum('Enter a number: ')
            if choice == 0:
                # Clean up the console
                self.clear_console()
                # Gives the options that can be selected in the menu
                self.run()
            elif choice == 1:
                action == action
                action()
            else:
                print('Please, choose number 0 or 1')
                
    def add_habit(self):
        """
        Allows the user to enter the name, periodicity, motivation,
        and description of the habit to be recorded.
        """
        # Clean up the console
        self.clear_console()
        # Prints the name of the application and instructions to the main menu
        self.back_to_menu_info()
        print("""
                             ADD A HABIT    
            ________________________________________________
            """)

        # A list of names of registered habits
        habits_names = self.analytics.select_column(self.analytics.habits_table(), 1)
        # ['Yoga']
        
        if len(habits_names) == 0:
             print(
            """
            ----------------Your first habit ---------------
            """)
        else:
            # List of the names and ids of the registered habits in table format
            self.analytics.table_registered_habits()
               
        while True:
            try:
                name_to_check = input("""
            Write the name of the habit you want to add """).title()
                
                if name_to_check not in habits_names:
                    if name_to_check == '':
                        print("Please, write the name of your habit")
                    elif name_to_check.isdigit():
                        if (int(name_to_check) == 0):
                            # Clean up the console
                            self.clear_console()
                            # Gives the options that can be selected in the menu
                            self.run()
                        else:
                            break
                    else:
                        name = name_to_check
                        break
                else:
                    print('This habit is already in your list')
                    
            except ValueError:
                pass

        while True:
            print("""
                  How often you want to do this activity?
              
                  1: daily
                  2: weekly
                  """)

            periodicity = pyip.inputNum('Choose a number: ')
        
            if periodicity == 1:
                periodicity = 'daily'
                break
            elif periodicity == 2:
                periodicity = 'weekly'
                break
            elif periodicity == 0:
                # Clean up the console
                self.clear_console()
                # Gives the options that can be selected in the menu
                self.run()
            else:
                print('Please, choose number 1 or 2 or \nzero to go back to the menu')
                
        while True:
            motivation = input("Your motivation: ")
            if motivation.isdigit():
                if int(motivation) == 0:
                    # Clean up the console
                    self.clear_console()
                    # Gives the options that can be selected in the menu
                    self.run()
                else:
                    break
            else:
                motivation = motivation.capitalize()
                break
                
        while True:
            description = input('Description: ')
            if description.isdigit():
                if int(description) == 0:
                    # Clean up the console
                    self.clear_console()
                    # Gives the options that can be selected in the menu
                    self.run()
                else:
                    break
            else:
                description = description.capitalize()
                break
            
        # insert a habit to the DB            
        self.analytics.insert_habit(name, periodicity, motivation, description)        
        # Clean up the console
        self.clear_console()
        # Select the row that contains the information of the newly added habit
        # [(3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-21')]
        added_habit = self.analytics.select_rows(self.analytics.habits_table(), 
                                   1, name)
        # Displays a table with header and column names and information of the added habit
        self.analytics.display_table(('ID', 'HABIT', 'PERIODICITY', 'MOTIVATION', 'DESCRIPTION', 'CREATION DAY'), 
                                    added_habit, 
                                    'ADDED HABIT')
        # Return to the main menu or adds another habit
        self.choice_stay_return('Add another habit', self.add_habit)
            
    def check_off(self):
        """
        Record the date and time in the trackings table when
        the user enters the id of the habit to be marked as done.
        """
        # Clean up the console
        self.clear_console()
        # Prints the name of the application and instructions to the main menu
        self.back_to_menu_info()
        print("""
                            CHECK A HABIT OFF    
            ________________________________________________
                            Time to improve!!
            ------------------------------------------------
            """)
        
        # A list of the existing information in the habit table of the DB
        habits_info = self.analytics.habits_table()
        # [(1, 'Yoga', 'daily', 'Be more flexible', 'Morning if possible', '2021-05-05')]
        # A list with all habit identifiers
        ids = self.analytics.get_all_ids(habits_info)
            
        while True:
            print(
                """                          
                 Which habit do you want to check-off?"""
                )
            # display a table with all the registered habits
            self.analytics.table_registered_habits()
            print('')
            id_n = pyip.inputNum("Choose the ID of your habit ")
            if id_n == 0:
                # back to the main menu
                self.run()
            elif id_n in ids:
                # Insert the day and time when the habit is checked-off
                self.analytics.insert_day(id_n)
                print(
                    """   
                 ------------------------------------------   
                                Good job!       
                              {} ✔ is done.
                 ------------------------------------------ 
                 """.format(
                 # Selects the habit name from the row that corresponds to the id
                 self.analytics.select_rows(habits_info, 0, id_n)[0][1])
                 )
                if len(habits_info) > 1:
                    # Return to the main menu or check another habit
                    self.choice_stay_return('Check another habit off', self.check_off)
                else:
                    # Return to the main menu by selecting the number zero
                    self.return_menu()
            else:
                print("Please, choose an ID from the list")
                
    def delete_habit(self):
        """
        Ask the user for the name of the habit and
        then delete it from the DB.
        """
        # Clean up the console
        self.clear_console()
        # Prints the name of the application and instructions to the main menu
        self.back_to_menu_info()
        print("""
                             DELETE HABIT    
            ________________________________________________
            """)
        # A list of names of registered habits ['Run', 'Yoga']
        habits_names = self.analytics.select_column(self.analytics.habits_table(), 1)
        #habits_names = self.analytics.get_all_names()
        
        print(""" 
            -------------------------------------------------
                            Deleting a habit 
                    will also reset all progress on it!
            -------------------------------------------------""")
        # List of the names and ids of the registered habits in table format
        self.analytics.table_registered_habits()

        while True:
            name = input("""
            Which habit do you want to delete? 
            Please, write just the NAME """).title()
            if name.isdigit():
                if int(name) == 0:
                    # back to the main menu
                    self.run()
                else:
                    print("""
                    - Write the name of the habit you want to delete -
                          """)
            elif name in habits_names:
                # the habit and its respective trackings are removed from the DB
                self.analytics.remove_habit(name)
                # Clean up the console
                self.clear_console()
                print("""
                      _______________________
                              - {} - 
                       ---------------------
                         has been deleted
                      _______________________
                      """.format(name))
                # A list of remaining registered habit names
                habits_names = self.analytics.select_column(self.analytics.habits_table(), 1)
                # habits_names = self.analytics.get_all_names()
                if len(habits_names) >= 1:
                    # List of the names and ids of the remaining habits in table format
                    self.analytics.display_table(('ID', 'HABIT'), 
                                                self.analytics.select_columns(
                                                    self.analytics.habits_table(),
                                                    stop=2), 
                                                'REMAINING HABITS')
                    # Return to the main menu or delete another habit
                    self.choice_stay_return('Delete another habit', self.delete_habit)
                else:
                    print("""
                   ____________________________
                      
                     No more registered habits 
                   ____________________________
                      """)
                    # # Wait 3 seconds before clearing the screen
                    # time.sleep(10)  
                    # # Clean up the console
                    # self.clear_console()
                    # back to the main menu
                    self.run()
            else:
                print("""
                      - This habit is not in your list -
                      """)
        
    def see_habit(self):
        """
        Displays individual information for each recorded habit.
        Habit name, motivation, description, periodicity, the date
        of the first tracking if any, the last day of activity, last
        day of activity, in which part of the day the habit is mostly
        checked off, the longest streak and the number of days or
        weeks of activity.
        """
        # Clean up the console
        self.clear_console()
        # Prints the name of the application and instructions to the main menu
        self.back_to_menu_info()
        print("""
                             SEE A HABIT    
            ________________________________________________
            """)
        # Gets the habits table of the DB
        habits_info = self.analytics.habits_table()
        # print(habits_info)
        # List of the names and ids of the registered habits in table format
        self.analytics.table_registered_habits()
        # Union of the habits table and the trackings table from the DB
        habits_trackings = self.analytics.habits_trackings_table()
        # ID, Name, Periodicity, Motivation,  Description,     t.Date, t.Time
        # [(1, 'Yoga', 'daily', 'Flexibility', 'Mornings', '2021-04-26', '17:38')]
        #habits_info = self.analytics.habits_table()
        # [(1, 'Yoga', 'weekly', 'Be more flexible', 'Before breakfast', '2021-02-22')]
        #number_of_habits = len(habits_info)
        #print(habits_trackings)
        # A list of the trackings that have been recorded in the trackings table of the DB
        trackings = self.analytics.trackings_table()
        #print(trackings)
        # HabitID,  Date,      Time
        # [(1, '2021-04-26', '11:51')]
        # A list with all habit identifiers in the habits table
        ids_habits_table = self.analytics.get_all_ids(habits_info)
        # A list with all habit identifiers in the trackings table
        ids_trackings_table = self.analytics.get_all_ids(trackings)
        col_date = 5
        col_time = 6
       
        while True:
            print('')
            id_n = pyip.inputNum("""
             Write the ID of the habit you want to check :
                                 """)
            if id_n == 0:
                # back to the main menu
                self.run()
            elif id_n in ids_habits_table:
                if id_n in ids_trackings_table:
                    # Select all rows belonging to the given habit id from the join of 
                    # habits table and trackings table
                    one_habit_trackings_info = self.analytics.select_rows(
                        habits_trackings, 0, id_n)
                    # print(one_habit_trackings_info)
                    # [(1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-07-31', '16:41'), 
                    # (1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-08-02', '18:44')]
                    # print(len(one_habit_trackings_info))
                    # Gets the periodicity of the selected habit
                    periodicity = one_habit_trackings_info[0][2]
                    # print(periodicity)
                    if len(one_habit_trackings_info) >= 1:
                        # Clean up the console
                        self.clear_console()
                        # [(2, 'Run', 'weekly', 'Faster', 'Sundays', '2021-04-27', '10:56')]
                        print(
                        """
                        ___________________________________
                                    - {} -
                        ___________________________________
                        Motivation:   {}
                        Description:  {}
                        Periodicity:  {}
                        -----------------------------------
                        
                        First tracking:         {}
                        """.format(one_habit_trackings_info[0][1],
                        one_habit_trackings_info[0][3],
                        one_habit_trackings_info[0][4],
                        periodicity,
                        # Gives the date when the first tracking was recorded
                        self.analytics.start_habit(one_habit_trackings_info, col_date))
                        )
                        
                        if len(one_habit_trackings_info) > 1:
                            # [(2, 'Run', 'weekly', 'Faster', 'Sundays', '2021-04-27', '10:56'),
                            # (2, 'Run', 'weekly', 'Faster', 'Sundays', '2021-04-27', '11:40')]
                            
                            # A dictionary whose keys are the parts of the day in which
                            # the habit was checked and whose values indicate the frecuency
                            active_time_dictionary = self.analytics.active_time_dict(
                                one_habit_trackings_info, 
                                col_time) 
                            # print(active_time_dictionary)
                            # Counter({'Afternoon': 1, 'Evening': 1})
                            # The highest value from the active time dictionary
                            max_value_active_time = self.analytics.max_value(
                                active_time_dictionary)
                            # print(max_value_active_time)
                            # 1
                            # Most frequently part(s) of the day when the habit is checked off.
                            most_active_time = self.analytics.most_active_time(
                                active_time_dictionary, 
                                max_value_active_time)
                            # print(most_active_time)
                            # ['Afternoon', 'Evening']
                            
                            # print(self.analytics.most_active_time(
                            #     self.analytics.active_time_dict(
                            #         one_habit_trackings_info, col_time
                            #         ),
                            #     self.analytics.max_value(
                            #         self.analytics.active_time_dict(
                            #             one_habit_trackings_info, col_time
                            #             )
                            #         )
                            #     ))
                            print(
                            """
                        Last day of activity:   {}
                        
                        You are more active during:
                        {}
                        """.format(
                        # The date of the last tracking
                        self.analytics.last_day(one_habit_trackings_info, col_date),
                        # Parts of the day separated by commas
                        self.analytics.display_elements(most_active_time)
                        )
                            )
                            if periodicity == 'daily':
                                print(
                                    """
                        Longest streak: {}
                        Days of activity: {}
                                    """.format(
                                    # the longest streak of a daily habit
                                    self.analytics.longest_streak_periodicity(
                                        one_habit_trackings_info, 
                                        'daily', 
                                        col_date),
                                    # Number of days in which the habit has been checked off
                                    self.analytics.activity(
                                        'daily', 
                                        one_habit_trackings_info, 
                                        col_date))
                                      )
                            elif periodicity == 'weekly':
                                print(
                                    """
                        Longest streak: {}
                        Weeks of activity: {}
                                    """.format(
                                    # the longest streak of a weekly habit
                                    self.analytics.longest_streak_periodicity(
                                        one_habit_trackings_info, 
                                        'weekly',
                                        col_date),
                                    # Number of weeks in which the habit has been checked off
                                    self.analytics.activity(
                                        'weekly',
                                        one_habit_trackings_info, 
                                        col_date))
                                    )

                        if len(habits_info) > 1:
                            # Return to the main menu or see another habit
                            self.choice_stay_return('See another habit', self.see_habit)
                        else:
                            # Return to the main menu by selecting the number zero
                            self.return_menu()

                else:
                    # Select the row in the habits table that corresponds to the selected id 
                    one_habit_info = self.analytics.select_rows(habits_info, 0, id_n)
                    # Clean up the console
                    self.clear_console()
                    print(
                        """
                        ___________________________________
                                    - {} -
                        ___________________________________
                    
                         You do not have any trackings yet
                           Start today with * {} * 
                               and check it off!
                        ___________________________________
                        Motivation:   {}
                        Description:  {}
                        Periodicity:  {}
                        
                        Creation day: {}
                        ___________________________________
                        """.format(one_habit_info[0][1],
                        one_habit_info[0][1],
                        one_habit_info[0][3],
                        one_habit_info[0][4],
                        one_habit_info[0][2],
                        one_habit_info[0][-1])
                        )
                    if len(habits_info) > 1:
                        # Return to the main menu or see another habit
                        self.choice_stay_return('See another habit', self.see_habit)
                    else:
                        # Return to the main menu by selecting the number zero
                        self.return_menu()
                
    def show_all_habits(self):
        """
        Gives a table with information about all recorded habits.
        ID and name of the habit, periodicity, motivation, description,
        and the day it was first recorded.
        """
        # Clean up the console
        self.clear_console()
        # Prints the name of the application and instructions to the main menu
        self.back_to_menu_info()
        print("""
                          ALL HABITS REGISTERED   
            ________________________________________________
            """)
        # Displays the information contained in the habits table in table format
        self.analytics.display_table(
            ('ID', 'HABIT', 'PERIODICITY', 'MOTIVATION', 'DESCRIPTION', 'CREATION DAY'),
            # Gets the habits table of the DB
            self.analytics.habits_table(), 
            'HABITS INFORMATION'
            )
        print('')
        # Return to the main menu by selecting the number zero
        self.return_menu()
        
    def habits_same_periodicity(self):
        """
        Displays information about all habits that have the same
        periodicity. For habits with trackings: ID and name of
        the habit, date of the first and last tracking, part of 
        the day when the user checks the habit of most often,
        numbers of days or weeks of activity, and the longest streak.
        For habits without trackings it shows the ID, name, periodicity,
        motivation, description, and date when the habit was first
        created.
        """
        # Clean up the console
        self.clear_console()
        # Prints the name of the application and instructions to the main menu
        self.back_to_menu_info()
        print("""
                    HABITS WITH THE SAME PERIODICITY    
            ________________________________________________
            """)
        # Join of the habits table and the trackings table from the DB
        habits_trackings = self.analytics.habits_trackings_table()
        # print('habits trackings')
        # print(habits_trackings)
        # [(1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-07-31', '16:41'), 
        #  (2, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-31', '16:46'), 
        #  (1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-08-02', '18:44'), 
        #  (1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-08-03', '13:43'), 
        #  (2, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-08-03', '14:36'), 
        #  (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-08-03', '15:44')]
        
        while True:
            print("""
                  What periodicity would you like to see?
                  
                  1: daily
                  2: weekly
                  """)

            periodicity = pyip.inputNum('Choose a number: ')
        
            if periodicity == 1:
                periodicity = 'daily'
                break
            elif periodicity == 2:
                periodicity = 'weekly'
                break
            elif periodicity == 0:
                # back to the main menu
                self.run()
            else:
                print('Please, choose number 1, 2 or 0')
        
        # Clean up the console
        self.clear_console()
        # Select all rows that have the same periodicity from the habits table
        habits_table_periodicity = self.analytics.select_rows(
             self.analytics.habits_table(), 
             2, 
             periodicity)
        # print('habits table')
        # print(self.analytics.habits_table())
        # [(1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-07-31'), 
        #  (2, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-31'), 
        #  (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-31'), 
        #  (4, 'Try Sth New', 'weekly', 'New experiences', 'A new activity', '2021-07-31')]
        # print('habits table periodicity')
        # print(habits_table_periodicity)
        # daily
        # [(1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-07-31'), 
        #  (3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-07-31')]
        # weekly
        # [(2, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-31'), 
        #  (4, 'Try Sth New', 'weekly', 'New experiences', 'A new activity', '2021-07-31')]
        
        # IDs of habits with same periodicity from the join of habits and trackings tables
        unique_ids_trackings_periodicity = self.analytics.unique_ids_periodicity(
            habits_trackings, 
            2, 
            periodicity)
        # print(unique_ids_trackings_periodicity)
        # [1, 3] daily
        # [2] weekly
    
        # Gives a list of habits with the same periodicity. Information and
        # trackings for each habit are grouped together in a list.
        habits_trackings_periodicity = self.analytics.lists_periodicity(
            habits_trackings, 
            2, 
            periodicity)
        # print('habits_trackings_periodicity')
        # print(habits_trackings_periodicity)
        # daily
        # [[(1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-07-31', '16:41'), 
        #   (1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-08-02', '18:44'), 
        #   (1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-08-03', '13:43')], 
        #  [(3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-08-03', '15:44')]]
        # weekly
        # [[(2, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-31', '16:46'), 
        #   (2, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-08-03', '14:36')]]

        # print(len(habits_table_periodicity))
        # print(len(habits_trackings_periodicity))
        
        if len(habits_table_periodicity) == 0:
            print("""
                  ________________________________________________
                             You do not have any habits 
                               with {} periodicity
                  ________________________________________________
                      """.format(periodicity.upper()))
            # Return to the main menu or see other periodicity
            self.choice_stay_return('See other periodicity',
                                    self.habits_same_periodicity)
        
        elif len(habits_table_periodicity) != 0:
            #print(len(habits_table_periodicity))
            # IDs of habits with same periodicity
            ids_habits_table = self.analytics.get_all_ids(habits_table_periodicity)
            # print(ids_habits_table)
            # [2, 4]
            # IDs of habits without trackings
            ids_without_trackings = list(set(ids_habits_table)-set(unique_ids_trackings_periodicity))
            # print('without')
            # print(ids_without_trackings)
            # [4]
            # IDs of habits that have trackings
            ids_with_trackings = list(set(ids_habits_table)-set(ids_without_trackings))
            # print('with')
            # print(ids_with_trackings)
            # [2]
            if len(ids_with_trackings) != 0:
                # A list with information on habits with the same periodicity and 
                # with trackings
                table_periodicity = self.analytics.periodicity_info(
                    habits_trackings_periodicity, 
                    periodicity
                    )
                # print('table periodicity')
                # print(table_periodicity)
                col_names = ('ID', 'HABIT', 'FIST TRACKING', 'LAST TRACKING', 'MOST ACTIVE TIME', 'ACTIVITY DAYS', 'LONGEST STREAK')
        
                if periodicity == 'weekly':
                    col_names = ('ID', 'HABIT', 'FIST TRACKING', 'LAST TRACKING', 'MOST ACTIVE TIME', 'ACTIVITY WEEKS', 'LONGEST STREAK')
                
                # Habits with same periodicity and with trackings in tabular form
                self.analytics.display_table(col_names,
                                            table_periodicity, 
                                            periodicity.upper() +
                                            ' PERIODICITY')
            if len(ids_without_trackings) != 0:
                # A list with information of habits with the same periodicity and 
                # without trackings
                habits_without_trackings = [
                    self.analytics.select_rows(habits_table_periodicity, 0, id_n)[0] 
                                            for id_n in ids_without_trackings]
                #print(habits_without_trackings)
                
                # Habits with same periodicity and without trackings in tabular form
                self.analytics.display_table(('ID', 'HABIT', 'PERIODICITY', 'MOTIVATION', 'DESCRIPTION', 'CREATION DAY'), 
                                            habits_without_trackings,
                                            periodicity.upper() + 
                                            ' PERIODICITY: '+ 
                                            ' Habits without trackings')
        
        # Return to the main menu or see other periodicity
        self.choice_stay_return('See other periodicity',
                                self.habits_same_periodicity)
        

    def habit_longest_streak(self):
        """
        Displays a table of the habit(s) with the longest streak.
        """
        # Clean up the console
        self.clear_console()
        # Prints the name of the application and instructions to the main menu
        self.back_to_menu_info()
        print("""
                             MY LONGEST STREAK    
            ________________________________________________
            """)
        
        # Join of the habits table and the trackings table from the DB
        habits_trackings = self.analytics.habits_trackings_table()
        
        # Information and trackings of each habit are grouped in a list and
        # habits with the same periodicity are grouped together.
        lists_periodicity = list(map(self.analytics.lists_periodicity, *zip((habits_trackings, 2, 'daily'),
                                             (habits_trackings, 2, 'weekly'))))
        # print(lists_periodicity)
        # print(lists_periodicity[0])
        
        # [
        #     [
        #         [(1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-07-31', '16:41'), (1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-08-02', '18:44'), 
        #          (1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-08-03', '13:43')
        #          ], 
        #         [(3, 'Read', 'daily', 'Read 12 books a year', 'Afternoons', '2021-08-03', '15:44')
        #          ]
        #     ], 
        #     [
        #         [(2, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-07-31', '16:46'), 
        #          (2, 'Run', 'weekly', 'Be faster', 'At weekends', '2021-08-03', '14:36')
        #          ]
        #     ]
        # ]

        # Habits separated by periodicity with general information about each habit.
        lists_info_periodicity = list(map(self.analytics.periodicity_info, *zip((lists_periodicity[0], 'daily'),
                                              (lists_periodicity[1], 'weekly'))))
        # print('list info periodicity')
        # print(lists_info_periodicity)
        # [[('1', 'Yoga', '2021-07-31', '2021-08-03', 'Afternoon', 3, 2), 
        #   ('3', 'Read', '2021-08-03', '2021-08-03', 'Afternoon', 1, 1)],
        
        #  [('2', 'Run', '2021-07-31', '2021-08-03', 'Afternoon', 2, 2)]
        # ]
        
        # All habits together in one list with general information on each habit
        all_periodicity_habits = [ habit for l in lists_info_periodicity for habit in l ]
        # print(all_periodicity_habits)
        # [('1', 'Yoga', '2021-07-31', '2021-08-03', 'Afternoon', 3, 2), 
        #  ('3', 'Read', '2021-08-03', '2021-08-03', 'Afternoon', 1, 1), 
        #  ('2', 'Run', '2021-07-31', '2021-08-03', 'Afternoon', 2, 2)]
        
        if len(all_periodicity_habits) > 1:
            # get the number of the maximum streak
            max_n = max(all_periodicity_habits, key=itemgetter(-1))[-1]
            # print(max_n)
            # get all habits which have the same number of the maximum streak
            habits_with_maximus = self.analytics.select_rows(all_periodicity_habits, -1, max_n)
            # print(habits_with_maximus)
            
        else:
            habits_with_maximus = all_periodicity_habits
 
        # A list with the name of the habit(s) with the longest streak
        names_streaks = list(zip(self.analytics.select_column(habits_with_maximus, 1),
                                   self.analytics.select_column(habits_with_maximus, -1)))

        col_names = ('HABIT', 'LONGEST STREAK')
        # A table with the name of the habit(s) with the longest streak
        self.analytics.display_table(col_names, 
                                    names_streaks, 
                                    ' ')
        print(' ')
        # Return to the main menu by selecting the number zero
        self.return_menu()
        
    def return_menu(self):
        """
        Return to the main menu by selecting the key with
        the number zero.
        """
        while True:
            number = pyip.inputNum("0. Back to the main menu: ")
            if number == 0:
                # Clean up the console
                self.clear_console()
                # back to the main menu
                self.run() 
            else:
                print('Press the number zero to go back')
                
    def clear_console(self):
        """
        Print several new lines to clean up the console
        """
        print('\n' * 200)
    
    def exit(self):
        """
        The application and the connection to the database are
        closed when the number zero is entered in the main menu.
        A message is displayed to signal the closing of
        the application.
        """
        print("""\n
            ________________________________________
            
                    Thank you for using
                    your HABITSBOX today 
            ________________________________________
              """)
        self.analytics.close()
        sys.exit(0)
        
    # def clear_console(self):
    #     return lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    
    # def clear_console(self):
    #     command = 'clear'
    #     if os.name in ('nt', 'dos'):
    #         print('hola')
    #         command = 'cls'
    #     os.system(command)
    #     print(command)
       
    



Menu().run()