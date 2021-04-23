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
            "9": self.exit,
           
            }
            
    def display_menu(self):
        habits_list = self.analytics.get_all_names()
        habits_names = self.analytics.select_column(habits_list, 1)
        # return []
        # return ['Yoga']
        number_of_habits = len(list(habits_names))
        
        print(
            """
            ----------------------------------------
                    WELCOME TO YOUR HABITSBOX       
            ----------------------------------------
            
                   Everything can be archived 
                with perseverance and commitment
            
            ---------- Let's get started -----------
            
            Choose a number:
                
            1. Add a new habit
            ----------------------------------------
            """)
        
        if number_of_habits == 0:
            print(
            """
            9. Exit
            
            ----------------------------------------
            """)
        elif number_of_habits == 1:
            print(
            """
            2. Check-in a habit
            3. Delete a habit
            
            Analysis -------------------------------
                
            4. See my habit
            ----------------------------------------
            
            9. Exit
            ----------------------------------------
            """)
        else:
            print(
            """            
            Analysis -------------------------------
                
            4. Search a habit
            5. See all habits
            6. See habits with same periodicity
            7. See my longest streaks
            8. Which habits do I struggle at most?
            
            9. Exit
            ----------------------------------------
            """)
            
    
    def run(self):
        """Show three types of menus.
        A two option menu when theres no registered habit
        A menu for one habit
        and a menu with more than one habit.
        If a number is selected it reacts to the option"""
        
        habits_list = self.analytics.get_all_names()
        habits_names = self.analytics.select_column(habits_list, 1)
        # return []
        # return ['Yoga']
        number_of_habits = len(list(habits_names))
        
        habits_names = self.analytics.get_all_names()
        
        while True:
            self.display_menu()
            choice = input("Enter an number: ")
            if (number_of_habits == 0) and (choice in ['1', '9']):
                action = self.menu_options.get(choice)
                action()
            elif (number_of_habits == 1) and choice in ['1', '2', '3', '4', '9']:
                action = self.menu_options.get(choice)
                action()
            elif (number_of_habits > 1):
                action = self.menu_options.get(choice)
                action()
            else:
                print("{} is not a valid choice.".format(choice))
                                                 
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
                  self.analytics.display_list_elements(habits_names))
               
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
                # Display a table with the checked habit
                print(
                    """                 
                                Good job!       
                              {} ✔ is done.
                 """.format(
                 self.analytics.one_habit_info_by_id(habits_info, id_n)[0][1])
                 )
                time.sleep(3)
                break
            else:
                print("Please, choose an ID from the list")

    def delete_habit(self):
        self.back_to_menu()
        habits_names = self.analytics.get_all_names()
        print(self.analytics.habits_table())
        display_habits_names = self.analytics.display_list_elements(habits_names)
        print(
            """             Your registered habits:
                                    {}
            ------------------------------------------------
                   Deleting a habit will also reset
                          all progress on it!
            ------------------------------------------------
            """.format(display_habits_names))

        while True:
            name = input('Which habit do you want to delete? ').title()

            if name.isdigit():
                if int(name) == 0:
                    self.run()
                else:
                    print("""
                          Write the name of the habit you want to delete
                          or press 0 (zero) to return to the main menu
                          """)
            elif name in habits_names:
                self.analytics.remove_habit(name)
                time.sleep(2)
                habits_names = self.analytics.get_all_names()
                if len(habits_names) >= 1:
                    self.show_all_habits()
                    time.sleep(2)
                    self.run()

                else:
                    self.run()
            else:
                print('This habit is not in your list')
        
    def search_habit(self):
        #print(self.analytics.habits_table())
        #print(self.analytics.trackings_table())
        habits_info = self.analytics.habits_table()
        # [(1, 'Yoga', 'weekly', 'Be more flexible', 'Before breakfast', '2021-02-22')]
        habits_trackings = self.analytics.trackings_table()
        # []
        habit = habits_info[0][1]
        periodicity = habits_info[0][2]
        motivation = habits_info[0][3]
        registration_habit = habits_info[0][-1]
        col_date = 1
        col_time = 2
        start = self.analytics.start_habit(habits_trackings, col_date)
        last = self.analytics.last_day(habits_trackings, col_date)
        streak_daily = self.analytics.longest_streak_periodicity(
            habits_trackings, 'daily', col_date)
        streak_weekly = self.analytics.longest_streak_periodicity(
            habits_trackings, 'weekly', col_date)
        activity_daily = self.analytics.activity('daily', habits_trackings, col_date)
        activity_weekly = self.analytics.activity('weekly', habits_trackings, col_date)
        active_time_dictionary = self.analytics.active_time_dict(habits_trackings, col_time)  
        max_value_active_time = self.analytics.max_value(active_time_dictionary)
        most_active_time = self.analytics.most_active_time(active_time_dictionary, max_value_active_time)
        
        if len(habits_trackings) == 0:     
            print(
                """             
                        ___________________________________
                
                                  Start now with
                                      - {} -    
                            and check it off as done
                        -----------------------------------
                      
                          Motivation: {}
                          Periodicity: {}
                      
                          Registration date: {}
                        ___________________________________
                    
            """.format(habit, motivation, periodicity, registration_habit))
        
        else:
            print(
                        """
                        ___________________________________
                                      - {} -
                        ___________________________________
                        Motivation:   {}
                        Periodicity:  {}
                        -----------------------------------
                        
                        Started on:             {}
                        Last day of activity:   {}
                        """.format(habit, motivation, 
                        periodicity, start, last)
                        )
            
            if len(habits_trackings) > 1:

                print(
                        """
                        You are more active during:
                        the {}
                        """.format(self.analytics.display_list_elements(most_active_time))
                    )
                
                if periodicity == 'daily':
                    
                    print(
                        """
                        Longest streak: {}
                        Days of activity: {}
                        """.format(streak_daily, activity_daily)
                        )
                elif periodicity == 'weekly':
                    print(
                        """
                        Longest streak: {}
                        Weeks of activity: {}
                        """.format(streak_weekly, activity_weekly)
                        )

    def show_all_habits(self):
        #self.analytics.see_all_habits()
        """Print a table with all habits and
        its fields"""
        all_habits = self.analytics.habits_table()
        if len(all_habits) >= 1:
            print('-' * 50)
            print('ID'.center(2) + 'HABIT'.center(15) + 'PERIODICITY'.center(15) + 'MOTIVATION'.center(15))
            print('-' * 50)
            for habit in all_habits:
                print(str(habit[0]).ljust(6) + str(habit[1]).ljust(15) + str(habit[2]).ljust(15)+ str(habit[3]))        
        


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