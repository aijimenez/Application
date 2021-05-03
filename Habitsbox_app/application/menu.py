import sys
import pyinputplus as pyip
from operator import itemgetter

import time
from analytics import Analytics
#from .analytics import Analytics

class Menu:
    """Show a menu and react to the user options when executed."""
          
    def __init__(self):
        self.analytics = Analytics()
        self.menu_options = { 
            "1": self.add_habit,
            "2": self.check_off,
            "3": self.delete_habit,
            "4": self.search_habit,
            "5": self.show_all_habits,
            "6": self.habits_same_periodicity,
            "7": self.habit_longest_streak,
            "8": self.habits_less_constant,
            "0": self.exit,
           
            }
            
    def display_menu(self):
        number_of_habits = len(list(self.analytics.habits_table()))
        number_of_trackings = len(list(self.analytics.trackings_table()))
                
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
            elif number_of_trackings > 1:
                print(
                    """            
            Analysis -------------------------------
                
            4. Search a habit
            5. See all habits registered
            6. See habits with same periodicity
            7. See my longest streak
            8. Which habits do I struggle at most?
            
            ----------------------------------------
                  """)
            
    
    def run(self):
        """Show different menus.
        A two option menu when theres no registered habit
        A menu for one habit
        and a menu with more than one habit.
        If a number is selected it reacts to the option"""
        
        number_of_habits = len(list(self.analytics.habits_table()))
        number_of_trackings = len(list(self.analytics.trackings_table()))
        
        while True:
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
            elif (number_of_trackings > 1) and (choice in [0, 1, 2, 3, 4, 5, 6, 7, 8]):
                action = self.menu_options.get(str(choice))
                action()
            else:
                print('Choose a number from the list')
                                                 
    def back_to_menu(self):
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
        stay in the current menu or return to the main menu.
        """
        while True:
            print("""
                  Press number 1 if you want to {} or
                  press zero to go back to the main menu
                  """.format(text))
            choice = pyip.inputNum('Enter a number: ')
            if choice == 0:
                self.analytics.clear_console()
                self.run()
            elif choice == 1:
                action == action
                action()
            else:
                print('Please,  choose number 0 or 1')
                
    def add_habit(self):
        self.analytics.clear_console()
        self.back_to_menu()
        print("""
                             ADD A HABIT    
            ________________________________________________
            """)

        habits_names = self.analytics.get_all_names()
        
        
        if len(habits_names) == 0:
             print(
            """
            ----------------Your first habit ---------------
            """)
        else:
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
                            self.analytics.clear_console()
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
                self.analytics.clear_console()
                self.run()
            else:
                print('Please, choose number 1 or 2 or \nzero to go back to the menu')
                
        while True:
            motivation = input("Your motivation: ")
            if motivation.isdigit():
                if int(motivation) == 0:
                    self.analytics.clear_console()
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
                    self.analytics.clear_console()
                    self.run()
                else:
                    break
            else:
                description = description.capitalize()
                break
                    
        self.analytics.insert_habit(name, periodicity, motivation, description)
        # print("""
        #               _______________________
        #                       - {} - 
        #                ---------------------
        #                 has just been added
        #               _______________________
              
        #       """.format(name))
        # # Press number 1 if you want to check other periodicity or
        # # press zero to go back to the main menu:
        # time.sleep(3)
        # self.choice_stay_return('add another habit', self.add_habit)
        self.analytics.clear_console()
        added_habit = self.analytics.select_rows(self.analytics.habits_table(), 
                                   1, name)
        self.analytics.table_header(('ID', 'HABIT', 'PERIODICITY', 'MOTIVATION', 'DESCRIPTION', 'CREATION DAY'), 
                                    added_habit, 
                                    'ADDED HABIT')
        self.choice_stay_return('add another habit', self.add_habit)

                     
    def check_off(self):
        """Register the custom as done
        when the user enters the habit-id"""
        # Shows the number to return to the main menu
        self.analytics.clear_console()
        self.back_to_menu()
        print("""
                            CHECK A HABIT OFF    
            ________________________________________________
                            Time to improve!!
            ------------------------------------------------
            """)
        habits_info = self.analytics.habits_table()
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
                # Insert the day and time in the database
                self.analytics.insert_day(id_n)
                # Display the checked habit
                print(
                    """   
                 ------------------------------------------   
                                Good job!       
                              {} ✔ is done.
                 ------------------------------------------ 
                 """.format(
                 self.analytics.select_rows(habits_info, 0, id_n)[0][1])
                 )
                self.choice_stay_return('check another habit off', self.check_off)
            else:
                print("Please, choose an ID from the list")
                
    def delete_habit(self):
        self.analytics.clear_console()
        self.back_to_menu()
        print("""
                             DELETE HABIT    
            ________________________________________________
            """)
        habits_names = self.analytics.get_all_names()
        # ['Run', 'Yoga']
        #print(self.analytics.habits_table())
        # [(1, 'Yoga', 'daily', 'Be more flexible', 'Before lunch', '2021-04-26'), 
        # (2, 'Run', 'weekly', 'Be more healthy', 'At the weekends', '2021-04-26')]
        print(""" 
            -------------------------------------------------
                            Deleting a habit 
                    will also reset all progress on it!
            -------------------------------------------------""")
        self.analytics.table_registered_habits()
        # print('REGISTERED HABITS')
        # print('___________________')
        # print(self.analytics.display_list_elements((habits_names)))
        

        while True:
            name = input("""
            Which habit do you want to delete? 
            Please, write just the NAME """).title()
            if name.isdigit():
                if int(name) == 0:
                    self.run()
                else:
                    print("""
                          Write the name of the habit you want to delete
                          """)
            elif name in habits_names:
                self.analytics.remove_habit(name)
                print("""
                      _______________________
                              - {} - 
                       ---------------------
                        has been delated
                      _______________________
                      """.format(name))
                time.sleep(2)
                habits_names = self.analytics.get_all_names()
                if len(habits_names) >= 1:
                    self.analytics.table_header(('ID', 'HABIT'), 
                                                list(self.analytics.select_columns(
                                                    self.analytics.habits_table(),
                                                    stop=2)), 
                                                'REMAINING HABITS')
                    time.sleep(3)
                    self.choice_stay_return('delete another habit', self.delete_habit)
                else:
                    self.run()
            else:
                print('This habit is not in your list')
        
    def search_habit(self):
        self.analytics.clear_console()
        self.back_to_menu()
        print("""
                             SEARCH A HABIT    
            ________________________________________________
            """)
        habits_info = self.analytics.habits_table()
        self.analytics.table_registered_habits()
        habits_trackings = self.analytics.habits_trackings()
        # ID, Name, Periodicity, Motivation,  Description,     t.Date, t.Time
        # [(1, 'Yoga', 'daily', 'Flexibility', 'Mornings', '2021-04-26', '17:38')]
        #habits_info = self.analytics.habits_table()
        # [(1, 'Yoga', 'weekly', 'Be more flexible', 'Before breakfast', '2021-02-22')]
        #number_of_habits = len(habits_info)
        trackings = self.analytics.trackings_table()
        # HabitID,  Date,      Time
        # [(1, '2021-04-26', '11:51')]
        # All ids in the habits table
        ids_habits_table = self.analytics.get_all_ids(habits_info)
        ids_trackings_table = self.analytics.get_all_ids(trackings)
        col_date = 5
        col_time = 6
       
        while True:
            print('')
            id_n = pyip.inputNum("""
             Write the ID of the habit you want to check :
                                 """)
            if id_n == 0:
                self.run()
            elif id_n in ids_habits_table:
                if id_n in ids_trackings_table:
                    one_habit_trackings_info = self.analytics.select_rows(
                        habits_trackings, 0, id_n)
                    periodicity = one_habit_trackings_info[0][2]
                    if len(one_habit_trackings_info) >= 1:
                        self.analytics.clear_console()
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
                        self.analytics.start_habit(one_habit_trackings_info, col_date))
                        )
                        self.choice_stay_return('see another habit', self.search_habit)
                        
                        
                        if len(one_habit_trackings_info) > 1:
                            # [(2, 'Run', 'weekly', 'Faster', 'Sundays', '2021-04-27', '10:56'),
                            # (2, 'Run', 'weekly', 'Faster', 'Sundays', '2021-04-27', '11:40')]
                            active_time_dictionary = self.analytics.active_time_dict(
                                one_habit_trackings_info, 
                                col_time)  
                            max_value_active_time = self.analytics.max_value(
                                active_time_dictionary)
                            most_active_time = self.analytics.most_active_time(
                                active_time_dictionary, 
                                max_value_active_time)
                            print(
                            """
                        Last day of activity:   {}
                        
                        You are more active during:
                        the {}
                        """.format(self.analytics.last_day(one_habit_trackings_info, col_date),
                        self.analytics.display_elements(most_active_time))
                            )
                            if periodicity == 'daily':
                                print(
                                    """
                        Longest streak: {}
                        Days of activity: {}
                                    """.format(
                                    self.analytics.longest_streak_periodicity(
                                        one_habit_trackings_info, 
                                        'daily', 
                                        col_date),
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
                                    self.analytics.longest_streak_periodicity(
                                        one_habit_trackings_info, 
                                        'weekly',
                                        col_date),
                                    self.analytics.activity(
                                        'weekly',
                                        one_habit_trackings_info, 
                                        col_date))
                                    )
                        self.choice_stay_return('see another habit', self.search_habit)

                else:
                    one_habit_info = self.analytics.select_rows(habits_info, 0, id_n)
                    self.analytics.clear_console()
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
                        
                        Registration day: {}
                        ___________________________________
                        """.format(one_habit_info[0][1],
                        one_habit_info[0][1],
                        one_habit_info[0][3],
                        one_habit_info[0][4],
                        one_habit_info[0][2],
                        one_habit_info[0][-1])
                        )
                    self.choice_stay_return('see another habit', self.search_habit)
                
    def show_all_habits(self):
        #self.analytics.see_all_habits()
        """Print a table with all habits and
        its fields"""
        self.analytics.clear_console()
        self.back_to_menu()
        print("""
                            SHOW ALL HABITS    
            ________________________________________________
            """)

        self.analytics.table_header(('ID', 'HABIT', 'PERIODICITY', 'MOTIVATION', 'DESCRIPTION', 'CREATION DAY'), 
                     self.analytics.habits_table(), 
                     'HABITS INFORMATION')
        print('')
        while True:
            number = pyip.inputNum("Press zero to go back to the main menu:")
            if number == 0:
                self.run() 
            else:
                print('Press the number zero to go back')
        
    def habits_same_periodicity(self):
        self.analytics.clear_console()
        self.back_to_menu()
        print("""
                    HABITS WITH THE SAME PERIODICITY    
            ________________________________________________
            """)
        habits_trackings = self.analytics.habits_trackings()
        
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
                self.run()
            else:
                print('Please, choose number 1, 2 or 0')
                
        self.analytics.clear_console()        
        habits_trackings_periodicity = self.analytics.select_rows(habits_trackings, 2, periodicity)
        #print(habits_trackings_periodicity)
        habits_table_periodicity = self.analytics.select_rows(
             self.analytics.habits_table(), 2, periodicity)
        #print(habits_table_periodicity)
        # [(1, 'Yoga', 'daily', 'Be more flexible', 'Mornings', '2021-05-03'), 
        # (2, 'Run', 'daily', 'Be faster', 'Mornings', '2021-05-03'), 
        # (3, 'Meditation', 'daily', 'Concentration', 'Mornings', '2021-05-03')
        ids_periodicity = self.analytics.get_all_ids(habits_trackings_periodicity)
        #print(ids_periodicity)
        unique_ids_periodicity = self.analytics.unique_data(ids_periodicity)
        #print(unique_ids_periodicity)
        habits_trackings_periodicity = self.analytics.lists_periodicity(habits_trackings, periodicity)
        #print(habits_trackings_periodicity)
        table_periodicity = self.analytics.periodicity_info(habits_trackings_periodicity, periodicity)
        
        header = ('HABIT', 'FIST TRACKING', 'LAST TRACKING', 'MOST ACTIVE TIME', 'ACTIVITY DAYS', 'LONGEST STREAK')
        
        if periodicity == 'weekly':
            header = ('HABIT', 'FIST TRACKING', 'LAST TRACKING', 'MOST ACTIVE TIME', 'ACTIVITY WEEKS', 'LONGEST STREAK')
        
        if len(habits_table_periodicity) == 0:
            print("""
                  ________________________________________________
                             You do not have any habits 
                               with {} periodicity
                  ________________________________________________
                  """.format(periodicity.upper()))
            self.choice_stay_return('check other periodicity',
                                self.habits_same_periodicity)
        else:
            self.analytics.table_header(header, 
                                    table_periodicity, 
                                    'PERIODICITY: '+ periodicity.upper())
      
        if len(habits_table_periodicity) != len(habits_trackings_periodicity):
            ids_habits_table = self.analytics.get_all_ids(habits_table_periodicity)
            ids_without_trackings = list(set(ids_habits_table)-set(unique_ids_periodicity))
            print("""
        _____________________________________________________
            Habits without trackings and same periodicity    
        _____________________________________________________                  
                  """)
            for id_n in ids_without_trackings:
                print('         {}'.format(
                    self.analytics.select_rows(habits_table_periodicity, 0, id_n)[0][1]))
        print('_'*96)

        self.choice_stay_return('check other periodicity',
                                self.habits_same_periodicity)
        

    def habit_longest_streak(self):
        self.analytics.clear_console()
        self.back_to_menu()
        print("""
                             MY LONGEST STREAK    
            ________________________________________________
            """)
        
        habits_trackings = self.analytics.habits_trackings()
        
        
        
        habits_max_streak = list(map(self.analytics.max_streak, *zip((habits_trackings, 'daily'),
                                            (habits_trackings, 'weekly'))))
        
        if len(habits_max_streak) > 1:
            max_n = max(habits_max_streak, key=itemgetter(-1))[-1]
            #print(max_n)
            habits_with_maximus = self.analytics.select_rows(habits_max_streak, -1, max_n)
            #print(habits_with_maximus)
            
        else:
            habits_with_maximus = habits_max_streak
            
        names_streaks = list(zip(self.analytics.select_column(habits_with_maximus, 0),
                                 self.analytics.select_column(habits_with_maximus, -1)))
        
        header = ('HABIT', 'LONGEST STREAK')
        
        habits_longest_streaks = self.analytics.add_header(header, names_streaks)
        
        lengths = self.analytics.lengths(habits_longest_streaks)
        strings_format = self.analytics.strings_format(habits_longest_streaks, lengths)
        table = self.analytics.table_including_distances(strings_format, habits_longest_streaks)
        print(self.analytics.display_list_elements(table))
        print('')
               
    def habits_less_constant(self):
        self.analytics.clear_console()
        self.back_to_menu()
        print("""
                           HABITS LESS CONSTANT    
            ________________________________________________
            """)
    
    def exit(self):
        print("\n - Thank you for using your Habitsbox today -")
        sys.exit(0)
        


Menu().run()