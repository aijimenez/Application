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
        
    def display_first_menu(self):
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
            9. Exit
            
            ----------------------------------------
            """)
            
    def display_one_habit_menu(self):
        print(
            """
            ----------------------------------------
                    WELCOME TO YOUR HABITSBOX       
            ----------------------------------------
            
            What do you want to do?
            
            1. Add a new habit
            2. Check-in a habit
            3. Delete a habit
            
            Analysis -------------------------------
                
            4. See my habit
            ----------------------------------------
            
            9. Exit
            ----------------------------------------
            """)
        
             
    def display_full_menu(self):
        print(
            """
            ----------------------------------------
                    WELCOME TO YOUR HABITSBOX       
            ----------------------------------------
            
            What do you want to do?
            
            1. Add a new habit
            2. Check-in a habit
            3. Delete a habit
            
            Analysis -------------------------------
                
            4. Search a habit
            5. See all habits
            6. See habits with same periodicity
            7. See my longest streaks
            8. Which habits do I struggle at most?
            
            9. Exit
            ----------------------------------------
            """)
            
    def choose_menu(self):
        habits_names = self.analytics.get_all_names()
        # return []
        # return ['Yoga']
        number_of_habits = len(habits_names)
        if number_of_habits == 0:
            print('No habits')
        elif number_of_habits == 1:
            print('One habit')
        else:
            print('Many habits')
            
    
    def run(self):
        """Show three types of menus.
        A two option menu when theres no registered habit
        A menu for one habit
        and a menu with more than one habit.
        If a number is selected it reacts to the option"""
        
        habits_names = self.analytics.get_all_names()
        
        if len(habits_names) == 0:
            while True:
                self.display_first_menu()
                choice = input("Enter an number: ")
                if choice in ['1', '9']:
                    action = self.menu_options.get(choice)
                    action()
                else:
                    print("{} is not a valid choice.".format(choice))
                    
        elif len(habits_names) == 1:
            while True:
                self.display_one_habit_menu()
                choice = input("Enter an number: ")
                if choice in ['1', '2', '3', '4', '9']:
                    action = self.menu_options.get(choice)
                    action()
                else:
                    print("{} is not a valid choice.".format(choice))            

        elif len(habits_names) > 1:
            while True:
                self.display_full_menu()
                choice = input("Enter an number: ")
                action = self.menu_options.get(choice)
                if action:
                    action()
                else:
                    print("{} is not a valid choice.".format(choice))
                                
    def back_to_menu(self):
        print(
            """
            ------------------------------------------------
                              HABITSBOX       
            ------------------------------------------------
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
            print('Your registered habits:',  habits_names)
               
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
        # A list with all habit identifiers
        ids = self.analytics.get_all_ids()
            
        while True:
            print('\nTime to improve!\n')
            print('Which habit do you want to check-off')
            # display a table with all the registered habits
            self.show_all_habits()
            print('')
            id_n = pyip.inputNum("Choose the number(ID) of your habit")
            if id_n == 0:
                # back to the main menu
                self.run()
            elif id_n in ids:
                # Insert the day and time in the database
                self.analytics.insert_day(id_n)
                # Display a table with the checked habit
                self.analytics.get_habit_by_id(id_n)
                print('\nGood job!')
                time.sleep(3)
                
                break
            else:
                print('Please, choose a number from the list ' + str(ids))
                
                
        # if len(ids) == 0:
        #     print("""\nYou have not yet registered any habit.
        #           \nLet us return to the main menu""")
        #     time.sleep(3)

    def delete_habit(self):
        self.back_to_menu()
        habits_names = self.analytics.get_all_names()
        print(
            """             Your registered habits:
                                    {}
            ------------------------------------------------
                   Deleting a habit will also reset
                          all progress on it!
            ------------------------------------------------
            """.format(habits_names))

        while True:
            name = input('Which habit do you want to delete? ').title()

            if name.isdigit():
                if int(name) == 0:
                    self.run()
                else:
                    break
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
        
        habits_names = self.analytics.get_all_names()
        if len(habits_names) == 1:
            self.analytics.info_one_habit()
            #self.show_all_habits()
            time.sleep(3)
        else:
            self.back_to_menu()
            print('Your registered habits:',  habits_names)
            name = input("Search for the name: ").title()
            self.analytics.get_habits_by_name(name)
        
    def show_all_habits(self):
        self.analytics.see_all_habits()
        


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