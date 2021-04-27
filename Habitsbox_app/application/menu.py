import sys
import pyinputplus as pyip


import time
from analytics import Analytics
#from .analytics import Analytics

class Menu:
    """Show a menu and react to the user options when executed."""
          
    def __init__(self):
        self.analytics = Analytics()
        self.menu_options = { 
            "1": self.add_habit,
            "2": self.check_in,
            "3": self.delete_habit,
            "4": self.search_habit,
            "5": self.show_all_habits,
            "6": self.habits_same_periodicity,
            "7": self.habits_longest_streaks,
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
            2. Check-in a habit
            3. Delete a habit
            ----------------------------------------
            """)
            
            if (number_of_trackings == 1) or (number_of_habits == 1):
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
            5. See all habits
            6. See habits with same periodicity
            7. See my longest streaks
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
            choice = input("Enter an number: ")
            if (number_of_habits == 0) and (choice in ['0', '1']):
                action = self.menu_options.get(choice)
                action()
            elif (number_of_habits >=1) and (choice in ['0', '1', '2', '3']):
                action = self.menu_options.get(choice)
                action()
            elif ((number_of_trackings == 1) or (number_of_habits == 1)) and (choice in ['0', '1', '2', '3', '4']):
                action = self.menu_options.get(choice)
                action()
            else:
                action = self.menu_options.get(choice)
                action()               
                                                 
    def back_to_menu(self):
        print(
            """
            ________________________________________________
            
                              HABITSBOX       
            ________________________________________________
            Hint: Press 0 (zero) to return to the main menu
            ------------------------------------------------
            """)
                
    def add_habit(self):
        
        self.back_to_menu()
        habits_names = self.analytics.get_all_names()
        
        if habits_names == []:
             print(
            """
            ----------------Your first habit ---------------
            """)
        else:
            print('Your registered habits:',  
                  self.analytics.display_elements(habits_names))
               
        while True:
            try:
                name_to_check = input('Which habit do you want to add? ').title()
                
                if name_to_check not in habits_names:
                    if name_to_check == '':
                        print("Please, write the name of your habit")
                    elif name_to_check.isdigit():
                        if (int(name_to_check) == 0):
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
                self.run()
            else:
                print('Please, choose number 1 or 2 or \nzero to go back to the menu')
                
        while True:
            motivation = input("Your motivation: ")
            if motivation.isdigit():
                if int(motivation) == 0:
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
                    self.run()
                else:
                    break
            else:
                description = description.capitalize()
                break
                    
        self.analytics.insert_habit(name, periodicity, motivation, description)
        print("\nYour habit has been added.\n")
        time.sleep(2)
        self.run()
             
    def check_in(self):
        """Register the custom as done
        when the user enters the habit-id"""
        # Shows the number to return to the main menu
        self.back_to_menu()
        habits_info = self.analytics.habits_table()
        # A list with all habit identifiers
        ids = self.analytics.get_all_ids(habits_info)
            
        while True:
            print(
                """                 
                          Time to improve!!
                          
                 Which habit do you want to check-off?
                """
                )
            # display a table with all the registered habits
            self.show_all_habits()
            print('')
            id_n = pyip.inputNum("Choose the ID of your habit")
            if id_n == 0:
                # back to the main menu
                self.run()
            elif id_n in ids:
                # Insert the day and time in the database
                self.analytics.insert_day(id_n)
                # Display the checked habit
                print(
                    """                 
                                Good job!       
                              {} ✔ is done.
                 """.format(
                 self.analytics.one_habit_info_by_id(habits_info, id_n)[0][1])
                 )
                time.sleep(3)
                self.run()
            else:
                print("Please, choose an ID from the list")

    def delete_habit(self):
        self.back_to_menu()
        habits_names = self.analytics.get_all_names()
        # ['Run', 'Yoga']
        #print(self.analytics.habits_table())
        # [(1, 'Yoga', 'daily', 'Be more flexible', 'Before lunch', '2021-04-26'), 
        # (2, 'Run', 'weekly', 'Be more healthy', 'At the weekends', '2021-04-26')]
        print(
            """             Your registered habits:
                                    {}
            ------------------------------------------------
                   Deleting a habit will also reset
                          all progress on it!
            ------------------------------------------------
            """.format(self.analytics.display_elements(habits_names))
            )

        while True:
            name = input('Which habit do you want to delete? ').title()

            if name.isdigit():
                if int(name) == 0:
                    self.run()
                else:
                    print("""
                          Write the name of the habit you want to delete
                          """)
            elif name in habits_names:
                self.analytics.remove_habit(name)
                time.sleep(2)
                habits_names = self.analytics.get_all_names()
                if len(habits_names) >= 1:
                    print("""
                          - REMAINING HABITS -
                          """)
                    self.show_all_habits()
                    time.sleep(2)
                    self.run()

                else:
                    self.run()
            else:
                print('This habit is not in your list')
        
    def search_habit(self):
        self.back_to_menu()
        self.show_all_habits()
        habits_trackings = self.analytics.habits_trackings()
        # ID, Name, Periodicity, Motivation,  Description,     t.Date, t.Time
        # [(1, 'Yoga', 'daily', 'Flexibility', 'Mornings', '2021-04-26', '17:38')]
        habits_info = self.analytics.habits_table()
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
             Write the ID of the habit you want to check
             or press zero to go back to the main menu:
                                 """)
            if id_n == 0:
                self.run()
            elif id_n in ids_habits_table:
                if id_n in ids_trackings_table:
                    one_habit_info = self.analytics.one_habit_info_by_id(
                        habits_trackings, 
                        id_n)
                    periodicity = one_habit_info[0][2]
                    if len(one_habit_info) >= 1:
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
                        """.format(one_habit_info[0][1],
                        one_habit_info[0][3],
                        one_habit_info[0][4],
                        periodicity,
                        self.analytics.start_habit(one_habit_info, col_date))
                        )
                        while True:
                            id_n = pyip.inputNum("Press zero to go back to the main menu:")
                            self.run()
                        if len(one_habit_info) > 1:
                            # [(2, 'Run', 'weekly', 'Faster', 'Sundays', '2021-04-27', '10:56'),
                            # (2, 'Run', 'weekly', 'Faster', 'Sundays', '2021-04-27', '11:40')]
                            active_time_dictionary = self.analytics.active_time_dict(
                                one_habit_info, 
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
                        """.format(self.analytics.last_day(one_habit_info, col_date),
                        self.analytics.display_elements(most_active_time))
                            )
                            if periodicity == 'daily':
                                print(
                                    """
                        Longest streak: {}
                        Days of activity: {}
                                    """.format(
                                    self.analytics.longest_streak_periodicity(
                                        one_habit_info, 
                                        'daily', 
                                        col_date),
                                    self.analytics.activity(
                                        'daily', 
                                        habits_trackings, 
                                        col_date))
                                      )
                            elif periodicity == 'weekly':
                                print(
                                    """
                        Longest streak: {}
                        Weeks of activity: {}
                                    """.format(
                                    self.analytics.longest_streak_periodicity(
                                        one_habit_info, 
                                        'weekly',
                                        col_date),
                                    self.analytics.activity(
                                        'weekly',
                                        one_habit_info, 
                                        col_date))
                                    )
                            break
                else:
                    print('No trackings')
            else:
                print("Please, choose an ID from the list")

    def show_all_habits(self):
        #self.analytics.see_all_habits()
        """Print a table with all habits and
        its fields"""
        habits_info = self.analytics.habits_table()
        # [(1, 'Yoga', 'weekly', 'Be more flexible', 'Before breakfast', '2021-02-22')]
        
        lengths = self.analytics.lengths(habits_info)
        strings_format = self.analytics.strings_format(habits_info, lengths)
        table = self.analytics.display_table(strings_format, habits_info)

        print(
            """
----------------------------------------------------------------
ID   HABIT  PERIODICITY  MOTIVATION  DESCRIPTION    START
----------------------------------------------------------------     
            """)
        print(self.analytics.display_list_elements(table))
        
        if len(habits_info) >= 1:
            print(
            """
              ---------------------------------------------------
              ID     HABIT    PERIODICITY    MOTIVATION
              ---------------------------------------------------      
            """)
            for habit in habits_info:
                print(str(habit[0]).rjust(16) + 
                      str(habit[1]).center(15) + 
                      str(habit[2]).ljust(10)+ 
                      str(habit[3]))        
        
    def habits_same_periodicity(self):
        pass
    
    def habits_longest_streaks(self):
        pass
    
    def habits_less_constant(self):
        pass
    
    def exit(self):
        print("\nThank you for using your Habitsbox today.")
        sys.exit(0)
        


Menu().run()